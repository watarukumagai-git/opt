#coding: utf-8
import numpy as np
import pandas as pd
import random as rnd
import time
import os
from os import path
import sys
import gc

from .import_data import import_data_class
from ..method.GA_update import GA_class
from ..method.weight_update import weight_update_class
#from .distance import distance_class
from .get_eval import get_obj_class
from .get_eval import get_vio_class
from .get_eval import scaling_class
from .figure_save import figure_save_class

class get_sol_loop_class:
    def get_rank(self, array_):
        clm = ["value", "rank"]
        df_ = pd.DataFrame(np.zeros((len(array_), 2)), columns=clm)
        df_[clm[0]] = array_
        list_ = list(set(list(array_)))
        list_.sort()
        rank = 0
        for ele_ in list_:
            df_.loc[df_[clm[0]]==ele_, clm[1]] = rank
            rank = rank + 1
        rank_ = df_[clm[1]].values
        return rank_
        
    def ave_dist_eval(self, x):
        (dist_matrix, d_max) = distance_class().distance_matrix(x)
        del x
        ave_dist = distance_class().average_distance(dist_matrix, d_max)
        return ave_dist, d_max

    
    def gbest_eval_(self, x, x_gbest, obj, vio, obj_gbest_current, iter):
        # obj: (m, 1)
        # vio: (m, 1)
        # obj_gbest_box: [obj, vio_sum]
        obj_cbest = min(obj)
        if iter == 0 or obj_cbest < obj_gbest_current[0]:
            cbest_i = np.argmin(obj)
            vio_cbest = vio[cbest_i]
            obj_gbest_array = np.array([obj_cbest, vio_cbest])
            x_gbest = x[cbest_i, :]
        else:
            obj_gbest_array = np.copy(obj_gbest_current)
        return x_gbest, obj_gbest_array

    
    def get_feas_gbest(self, obj_feas_gbest_old, obj_feas_cbest_new):
        feas_gbest_obj = obj_feas_gbest_old[0]
        feas_gbest_vio = obj_feas_gbest_old[1]
        feas_cbest_obj = obj_feas_cbest_new[0]
        feas_cbest_vio = obj_feas_cbest_new[1]

        flag_ = 0
        if feas_gbest_vio > 0:
            if feas_cbest_vio < feas_gbest_vio or (feas_cbest_obj < feas_gbest_obj and feas_cbest_vio == feas_gbest_vio):
                flag_ = 1
        else:
            if feas_cbest_obj < feas_gbest_obj and feas_cbest_vio == 0:
                flag_ = 1
        if flag_ == 1:
            feas_gbest_obj = feas_cbest_obj
            feas_gbest_vio = feas_cbest_vio
            
        return [feas_gbest_obj, feas_gbest_vio]
    
    
    def get_feas_cbest(self, obj):
        # obj: (m, 4) [obj, vio]
        feas_flag = np.where(obj[:, 1]==0, 1, 0)
        obj_df = pd.DataFrame(obj, columns = ["obj", "vio_sum"])
        obj_df.loc[:, "num"] = np.arange(len(obj_df))
        # a feasible solution exists
        if np.any(feas_flag==1) == True:
            # only feasible solution
            feas_df = obj_df.loc[obj_df["vio_sum"]==0, :]
            # index minimum objective function in feasible solution
            index_ = feas_df["obj"].idxmin()
        else:
            # index minimum violation
            index_ = obj_df["vio_sum"].idxmin()
        num_feas_cbest = obj_df.loc[index_, "num"]
        return obj[num_feas_cbest, :], num_feas_cbest

    
    def update_obj_feas_gbest_cbest(self, obj, obj_feas_gbest_old, iter):
        # obj_feas_gbest_cbest_box: [feas_gbest, feas_gbest_vio_sum, feas_cbest, feas_cbest_vio_sum]
        (obj_feas_cbest_new, num_feas_cbest) = self.get_feas_cbest(obj)
        if iter == 0:
            obj_feas_gbest_new = obj_feas_cbest_new
        else:
            obj_feas_gbest_new = self.get_feas_gbest(obj_feas_gbest_old, obj_feas_cbest_new)
        return np.concatenate([obj_feas_gbest_new, obj_feas_cbest_new]), num_feas_cbest

    
    def draw_figure(self, prob, x, x_feas_gbest, run, iter):
        # get path
        work_path = path.dirname( path.abspath(__file__) )
        os.chdir(work_path)
        work_path = os.path.abspath('..\\..\\') 
        dir_base = work_path + '\\output\\'

        (X, Y, obj_mesh_box, vio_mesh_box, feas_mesh_box, x_ul) = figure_save_class().get_contour_data(prob)
        # position in solution space
        figure_label2 = ["$x_1$", "$x_2$", "$xi$", "$xgbest$", x_ul[0, 0], x_ul[1, 0], x_ul[0, 1], x_ul[1, 1]]
        fig_file_name = dir_base + 'position_solution_space' + str(run) + '_iter'+ str(iter) + '.png'
        figure_save_class().scatter_solution_space(figure_label2, x[:, 0], x[:, 1], x_feas_gbest, X, Y, obj_mesh_box, feas_mesh_box, fig_file_name)


    def main_loop(self, prob, alg_para, run, start_time):
        # get parameters
        # problem parameters
        N = prob.N
        problem_type = prob.problem_type
        # algorithm parameters
        iter_max = alg_para[1]
        m = alg_para[2]
        

        # 1. databox gene
        # obj: [obj, obj_eval, vio_sum, vio_eval]
        obj = np.zeros((m, 4))
        obj_box = np.zeros((m, iter_max))
        vio_box = np.zeros((m, iter_max))
        alpha_box = np.zeros(iter_max)

        #(g, h) = get_vio_class().get_vio(prob, np.ones(N))
        #M_g = len(g)
        #gbest_vio_box = np.zeros((M_g+M_h, iter_max))

        # obj_feas_gbest_cbest_box: [feas_gbest, feas_gbest_vio_sum, feas_cbest, feas_cbest_vio_sum]
        obj_feas_gbest_cbest_box = np.zeros((iter_max, 4))


        # 2. initial solution
        data = import_data_class().get_dataset(run, 2)
        x = data[0:m, 0:N]*(prob.xmax-prob.xmin) + prob.xmin
        
        del data
        gc.collect()


        work_path = path.dirname( path.abspath(__file__) )
        os.chdir(work_path)
        dir_name = path.abspath('..\\') + '\\function\\'


        # get obj: (m)
        obj[:, 0] = get_obj_class().get_obj(prob, x)
        obj[:, 1] = np.copy(obj[:, 0])
        # get vio_sum: (m)
        # each_vio: (m, g_num)
        (obj[:, 2], each_vio) = get_vio_class().get_vio(prob, x)
        obj[:, 3] = np.copy(obj[:, 2])

        # vio = sigma_{j=1, L} orm_j
        # vio_eval = sigma_{j=1, L} orm_j
        # vio_eval = sigma_{j=1, L} (orm_max - orm_j / orm_max - orm_min)
        # orm_max = max_{i=1,...,m} orm_j
        # orm_min = min_{i=1,...,m} orm_j
        # orm_j : (m, L) [0, g_j(x)]


        iter = 0
        obj_box[:, iter] = np.copy(obj[:, 0])
        vio_box[:, iter] = np.copy(obj[:, 2])

        obj_feas_gbest_old = [0, 0]
        (obj_feas_gbest_cbest_box[iter, :], num_feas_cbest) = self.update_obj_feas_gbest_cbest(obj[:, [0,2]], obj_feas_gbest_old, iter)
        x_feas_cbest = x[num_feas_cbest, :]
        x_feas_gbest = np.copy(x_feas_cbest)

        #(ave_dist_box[iter, run], d_max) = self.ave_dist_eval(x)


        # 3. iteration loop
        #print ("iteration: ", iter)
        #print ("gbest: ", obj_gbest_box[0, :])
        #print ("run: ", run)
        #now_time = time.time() 
        #cal_time = now_time - start_time 
        #print ("calculation time = {:.2f} sec".format(cal_time))
        
        w_update_const = weight_update_class(m)
        alpha = 1.0
        w = w_update_const.update_weight(alpha)
        x_update_const = GA_class(m, N, w)


        while True:
            # 4. solution update
            (x, obj, each_vio) = x_update_const.GA_update(prob, x, obj, each_vio)
            # 5. update alpha and weight vector
            alpha = w_update_const.update_alpha(alpha, obj[:, [0,2]])
            x_update_const.w = w_update_const.update_weight(alpha)
            
            # other data update
            obj_box[:, iter] = np.copy(obj[:, 0])
            vio_box[:, iter] = np.copy(obj[:, 2])
            obj_feas_gbest_old = obj_feas_gbest_cbest_box[iter-1, :2]
            (obj_feas_gbest_cbest_box[iter, :], num_feas_cbest) = self.update_obj_feas_gbest_cbest(obj[:, [0,2]], obj_feas_gbest_old, iter)
            alpha_box[iter] = alpha

            #(gbest_vio_box[:, iter], tmp, tmp, tmp) = get_vio_class().get_vio_each_const(prob, x_feas_gbest.reshape(1, N), delta)

            # 6. check termination
            if iter == iter_max - 1:
                 break
            else:
                 iter = iter + 1
                 #now_time = time.time() 
                 #cal_time = now_time - start_time 
                 #print ("loop times: ", run)
                 #print ("calculation time = {:.2f} sec".format(cal_time))
                 #print ("gbest: ", obj_gbest_box[iter-1, :])
                 #print ("iteration: ", iter)

        #return x, obj_box, vio_box, x_feas_gbest, obj_feas_gbest_cbest_box, feas_rate_box, gbest_vio_box
        return x, obj_box, vio_box, obj_feas_gbest_cbest_box, alpha_box