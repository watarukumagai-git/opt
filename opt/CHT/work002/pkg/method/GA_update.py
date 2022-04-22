#coding: utf-8
import numpy as np
import pandas as pd
import random as rnd
import math
from ..sub_pkg.get_eval import get_obj_class
from ..sub_pkg.get_eval import get_vio_class
from ..sub_pkg.get_eval import scaling_class
from .crossover import crossover_class
from .mutation import mutation_class

class GA_class:
    def __init__(self, m, N, w):
        self.m = m
        self.N = N
        self.T = int(np.floor(m/10))
        self.w = w
            
    def get_B(self, w_, T):
        #initialize neighborhood
        B = np.zeros((self.m,T));
        
        #calculate distances between weighed vectors
        for i in range(0,self.m):
            dw = np.linalg.norm(w_[i,:]-w_, axis=1, ord=2)
            dw_index = np.argsort(dw)
            B[i,:] = dw_index[:T]
        B = B.astype('int64')
        return B
    
    def modified_x(self, x_, x_ul):
        m_ = len(x_)
        #for i in range(0, m_):
        #    (~,clm1) = find(x[i,:]>xu)
        #    (~,clm2) = find(x[i,:]<xl)
        #    x[i,clm1]=rem(x[i,clm1]-xl[clm1],xu[clm1]-xl[clm1])+xl[clm1]
        #    x[i,clm2]=rem(x[i,clm2]-xu[clm2],xu[clm2]-xl[clm2])+xu[clm2]
        return x_
    
    def neighbor_gene(self, x12, x_ul):
        # 1: SBX
        # 2: BLX-alpha
        # 3: uniform
        crossover_type = 1
        # 1: PM
        mutation_type = 1
        
        #crossover
        xover = crossover_class(x12[0, :],x12[1, :])
        if crossover_type == 1:
            Pcr = 1
            [u, temp] = xover.SBX(Pcr)
        elif crossover_type == 2:
            Pcr = 1
            [u, temp] = xover.Uniform(Pcr)
        elif crossover_type == 3:
            alpha_Xover = 0.25
            u = xover.BLX_alpha(alpha_Xover)
        
        #mutation
        mutate = mutation_class(u)
        if mutation_type == 1:
            Pm = 1/self.N
            u = mutate.PM(Pm,x_ul)

        #modify
        mod_x = self.modified_x(u,x_ul)
        
        return mod_x

    
    def S(self, w, f, scalar_type='weighted sum'):
        # f : (num_obj) or (m, num_obj)
        # w : (num_obj) or (m, num_obj)
        # S = (w*(z_nad-f)).sum
        if scalar_type == 'weighted sum':
            if w.ndim > 1:
                S = np.sum(w*f, axis=1)
            else:
                S = np.sum(w*f)
        # S = (w*(f-z_id)).max
        elif scalar_type == 'weighted tchebycheff':
            if w.ndim > 1:
                S = np.max(w*f, axis=1)
            else:
                S = np.max(w*f)
        # S = horizon_norm + theta * vertical_norm
        elif scalar_type == 'PBI':
            theta = 10
            if w.ndim > 1:
                S = np.max(w*f, axis=1)
            else:
                w_norm = np.linalg.norm(w, ord=2)
                horizon_norm = np.linalg.norm(f-d1*w, ord=2)/w_norm
                vertical_norm = np.linalg.norm(f-horizon_norm*w/w_norm, ord=2)
                S = horizon_norm + theta * vertical_norm
        return S


    def selection(self, prob, x, obj, each_vio, w, B, x_nei):
        def get_scaling(prob, ori_value):
            values_eval_add = scaling_class().scaling_values(prob, ori_value)
            return values_eval_add[:self.m], values_eval_add[-1]

        # calculate objective function and constraint violation of xnei
        # obj_nei: [f, f_eval, v_sum, v_eval]
        obj_nei = np.zeros(4)
        obj_nei[0] = get_obj_class().get_obj(prob, x_nei)
        (obj_nei[2], each_vio_nei) = get_vio_class().get_vio(prob, x_nei)
        if prob.scaling_type == 1:
            obj_nei[[1,3]] = obj_nei[[0,2]].copy()
        elif prob.scaling_type == 2:
            (obj[:, 1], obj_nei[1]) = get_scaling(prob, np.append(obj[:, 0], obj_nei[0]))
            (obj[:, 3], obj_nei[3]) = get_scaling(prob, np.append(each_vio, each_vio_nei))

        for idx in B:
            # S(w[idx], values_eval[idx]) > S(w[idx], values_nei_eval)
            if self.S(w[idx,:],obj[idx, [1,3]])>self.S(w[idx,:],obj_nei[[1,3]]):
                x[idx,:] = x_nei.copy()
                obj[idx, :] = obj_nei.copy()
                each_vio[idx, :] = each_vio_nei.copy()
        return x, obj, each_vio


    def GA_update(self, prob, x, obj, each_vio):
        B = self.get_B(self.w, self.T)
        #f_old = f.copy()
        
        T_list = np.arange(self.T).tolist()

        for i in range(0, self.m):
            # parent selction
            p = B[i,rnd.sample(T_list, 2)]

            # neiborhood generation
            x_nei = self.neighbor_gene(x[p,:],prob.x_ul)

            # survival choice
            (x, obj, each_vio) = self.selection(prob,x,obj,each_vio,self.w,B[i, :],x_nei)

        # if all element is same, output is True
        #if (f==f_old).all():
        #    print('f is not updated')
        #else:
        #    print('f is updated')

        return x, obj, each_vio