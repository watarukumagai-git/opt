# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import time
import os
from os import path

from pkg.sub_pkg.get_param import get_param_class
from pkg.sub_pkg.figure_save import figure_save_class
from pkg.sub_pkg.get_sol_loop import get_sol_loop_class
from pkg.sub_pkg.get_eval import get_obj_class
from pkg.sub_pkg.get_eval import get_vio_class
from pkg.function.function import function


def make_setfile(dir_base, str_list, num_list):
    f = open(dir_base + '\\set_file.txt', 'w')
    for i in range(0,len(str_list)):
        f.write(str_list[i] + ' = ' + str(num_list[i]) + '\n')
    f.close()

    
def get_path(problem_type, N):
    work_path = path.dirname( path.abspath(__file__) )
    os.chdir(work_path)
    #work_path = os.path.abspath('..\\..\\') 
    dir_base = work_path + '\\output\\pro' + str(problem_type)
    my_makedirs(dir_base)
    my_makedirs(dir_base + "\\file")
    my_makedirs(dir_base + "\\fig")
    return dir_base


def S(w, f, z, scalar_type='weighted sum'):
    # f (num_obj) or (mesh, num_obj) : values in each mesh point
    # w (num_obj) : weight
    # z (num_obj) : ideal point
    # S = (w*(f-z_id)).sum
    if scalar_type == 'weighted sum':
        if f.ndim > 1:
            S = np.sum(w*(f-z), axis=1)
        else:
            S = np.sum(w*(f-z))
    # S = (w*(f-z_id)).max
    elif scalar_type == 'tchebycheff':
        if f.ndim > 1:
            S = np.max(w*(f-z), axis=1)
        else:
            S = np.max(w*(f-z))
    # S = horizon_norm + theta * vertical_norm
    elif scalar_type == 'PBI':
        theta = 10
        if f.ndim > 1:
            S = np.max(w*(f-z), axis=1)
        else:
            w_norm = np.linalg.norm(w, ord=2)
            horizon_norm = np.linalg.norm((f-z)-d1*w, ord=2)/w_norm
            vertical_norm = np.linalg.norm((f-z)-horizon_norm*w/w_norm, ord=2)
            S = horizon_norm + theta * vertical_norm
    return S


def update_weight(m, alpha):
    delta = pow(10,-15)
    w = np.zeros((m, 2))
    w[:,0] = alpha*(np.arange(m))/(m-1)
    #w[:,0] = np.where(w[:,0]==0, delta, w[:,0])
    w[:,1] = 1 - w[:,0]
    return w

def graph_plot(prob, x_ul, w, x, z, type_s, dir_base):
    m = w.shape[0]
    mesh = x.shape[1]
    # pareto
    theta = np.linspace(np.pi, 3*np.pi/2, mesh)
    p_c = prob.pareto_function(theta, 'circle').T
    p_e = prob.pareto_function(theta, 'ellipsoid').T
    
    # [obj_min, obj_max, vio_min, vio_max]
    minmax = [x_ul[0, 0], x_ul[1, 0], x_ul[0, 1], x_ul[1, 1]]
    # position in obj and vio space
    figure_label1 = ["objective: $f(x)$", "violation: $v(x)$", "ideal point"]
    figure_label2 = ["objective: $f(x)$", "violation: $v(x)$", "ideal point", "pareto"]
    Scalar_box = np.zeros((m, mesh, mesh))
    for i in range(0, m):
        Scalar_box[i, :, :] = np.array([S(w[i, :], x[:, ii, :].T, z, type_s) for ii in range(0, mesh)])
        fig_file_name = dir_base + '\\fig\\ideal_'+str(abs(z[0]))+'\\scalar_obj_vio_space_' + type_s + '_weight_'+ str(i) +'.png'
        figure_save_class().scatter_obj_vio_space_contour(figure_label1, minmax, x, Scalar_box[i, :, :], z, w[i, :], fig_file_name)
        
        fig_file_name = dir_base + '\\fig\\ideal_'+str(abs(z[0]))+'\\scalar_obj_vio_space_' + type_s + '_weight_'+ str(i) +'_pareto_circle.png'
        figure_save_class().scatter_obj_vio_space_contour_pareto(figure_label2, minmax, x, Scalar_box[i, :, :], p_c, z, w[i, :], fig_file_name)

        fig_file_name = dir_base + '\\fig\\ideal_'+str(abs(z[0]))+'\\scalar_obj_vio_space_' + type_s + '_weight_'+ str(i) +'_pareto_ell.png'
        figure_save_class().scatter_obj_vio_space_contour_pareto(figure_label2, minmax, x, Scalar_box[i, :, :], p_e, z, w[i, :], fig_file_name)
        
    
    #area_theta = np.linspace(0, np.pi/2, m)
    area_theta = np.arctan2(w[:, 1],w[:, 0])
    angle = np.arctan2(x[1, :, :].reshape(mesh*mesh),x[0, :, :].reshape(mesh*mesh))
    dis = np.array([np.abs(angle - area_theta[i]) for i in range(0, m)]).T
    # 各位置が何番目の角度に入るのか (mesh) {0,...,m}
    idx_min = np.argmin(dis, axis=1)
    # S (m, mesh, mesh)
    SS = Scalar_box.reshape((-1, mesh*mesh)).copy()
    SS = np.array([SS[idx_min[i], i] for i in range(0, mesh*mesh)])
    SS = SS.reshape((mesh, mesh)).copy()
    
    fig_file_name = dir_base + '\\fig\\ideal_'+str(abs(z[0]))+'\\scalar_obj_vio_space_' + type_s + '_weight_all.png'
    figure_save_class().scatter_obj_vio_space_contour(figure_label1, minmax,x, SS, z, w, fig_file_name)

    fig_file_name = dir_base + '\\fig\\ideal_'+str(abs(z[0]))+'\\scalar_obj_vio_space_' + type_s + '_weight_all_pareto_circle.png'
    figure_save_class().scatter_obj_vio_space_contour_pareto(figure_label2, minmax,x, SS, p_c, z, w, fig_file_name)

    fig_file_name = dir_base + '\\fig\\ideal_'+str(abs(z[0]))+'\\scalar_obj_vio_space_' + type_s + '_weight_all_pareto_ell.png'
    figure_save_class().scatter_obj_vio_space_contour_pareto(figure_label2, minmax,x, SS, p_e, z, w, fig_file_name)


def generate_data(mesh, m, x_ul, alpha, dir_base):
    N = x_ul.shape[0]
    x = np.zeros((N, mesh, mesh))
    ff = np.linspace(x_ul[0, 0], x_ul[1, 0], mesh)
    vv = np.linspace(x_ul[0, 1], x_ul[1, 1], mesh)
    # X: [mesh, mesh] xbox in mesh
    # Y: [mesh, mesh] ybox in mesh
    X, Y = np.meshgrid(ff, vv)
    x[0, :, :] = X
    x[1, :, :] = Y

    w = update_weight(m, alpha)
    
    df = pd.DataFrame(w, index=[str(i+1) for i in range(0, m)], columns=['w_1','w_2'])
    print(df)
    df.to_csv(dir_base + '\\file\\weight,csv')    

    return x, w
    
    
def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

        
def main():
    # parameter setting
    (pro_para, alg_para) = get_param_class().get_param()
    #pro_para = [N, problem_type]
    #alg_para = [alg_type, m, "alg_name", **algorithm's other para.**]
    N = pro_para[0]
    problem_type = pro_para[1]

    alg_type = alg_para[0]
    m = alg_para[1]

    # instance
    prob = function(problem_type, N, alg_type)
    #optima = prob.get_opt()

    
    # get path
    dir_base = get_path(problem_type, N)
    str_clm = ['N','problem_type','alg_type','m']
    num_clm = [N,problem_type,alg_type,m]   
    print(str_clm)
    print(num_clm)
    make_setfile(dir_base, str_clm, num_clm)
    
    # time start
    start_time = time.time()
    print ("calculation started.")
    print('-----------------------------------')


    
    # databox gene
    mesh = 1000
    alpha = 1.0
    
    x_ul = prob.x_ul
    x, w = generate_data(mesh, m, x_ul, alpha, dir_base)
    
    # ideal point
    z = np.array([0,0])
    #z = np.array([-0.1,0])
    print('ideal point = ')
    print(z)
    
    type_s_list = ['weighted sum', 'tchebycheff']
    type_s = type_s_list[0]
    print('scalar = ')
    print(type_s)
    
    # time finish
    end_time = time.time()
    cal_time = end_time - start_time
    print('time = %.2f sec = %.2f min' % (cal_time, cal_time/60))

    graph_plot(prob, x_ul, w, x, z, type_s, dir_base)

    # time finish
    end_time = time.time()
    cal_time = end_time - start_time
    print('time = %.2f sec = %.2f min' % (cal_time, cal_time/60))

    
if __name__ == "__main__":
    main()
