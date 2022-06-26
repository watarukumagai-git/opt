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
    my_makedirs(work_path + '\\output\\pro' + str(problem_type))
    dir_base = work_path + '\\output\\pro' + str(problem_type) + '\\N' + str(N)
    my_makedirs(dir_base)
    my_makedirs(dir_base + "\\file")
    my_makedirs(dir_base + "\\fig")
    return dir_base


def get_df_obj_vio(obj_vio_box, clm_list):
    m = obj_vio_box.shape[1]
    num_list = [str(n) for n in range(0, m)]
    for i in range(0, 2):
        num_list_ = [clm_list[i] + n for n in num_list]
        df_ = pd.DataFrame(obj_vio_box[:, :, i], columns=num_list_)
        if i == 0:
            df_obj_vio = df_.copy()
        else:
            df_obj_vio = pd.concat([df_obj_vio, df_], axis=1)
    return df_obj_vio


def get_result(obj_feas_gbest_cbest_box):
    #name_list = ["obj", "vio", "up/low bound vio", "discrete vio"]
    name_list = ["obj", "vio"]
    idx_list = ["ave", "std", "max", "min"]

    df_obj_feas_gbest_final = pd.DataFrame(obj_feas_gbest_cbest_box[-1, :2, :].T, columns=name_list)
    #uplow_vio = np.sum(feas_gbest_vio_box[:M_g, iter_max-1, :], axis=0)
    #discrete_vio = np.sum(feas_gbest_vio_box[M_g:, iter_max-1, :], axis=0)
    #df_obj_feas_gbest["up/low bound vio"] = uplow_vio
    #df_obj_feas_gbest["discrete vio"] = discrete_vio

    df_result = pd.DataFrame(np.zeros((len(idx_list), len(name_list))), index=idx_list, columns=name_list)
    for i in name_list:
        df_result.at["ave", i] = df_obj_feas_gbest_final.loc[:, i].mean()
        df_result.at["std", i] = df_obj_feas_gbest_final.loc[:, i].std()
        df_result.at["max", i] = df_obj_feas_gbest_final.loc[:, i].max()
        df_result.at["min", i] = df_obj_feas_gbest_final.loc[:, i].min()

    #vio_array = df_obj_feas_gbest.loc[:, "vio"].values
    #obj_array = df_obj_feas_gbest.loc[:, "obj"].values
    #if np.any(vio_array == 0) == True:
    #    count = len(vio_array[vio_array == 0])
    #else:
    #    count = 0
    #df_result.at["feas_rate", "obj"] = 100 * count/float(run_max)

    #if np.any(obj_array <= 0.1 + optima) == True:
    #    count = len(obj_array[obj_array <= 0.1 + optima])
    #else:
    #    count = 0
    #df_result.at["sucess_rate", "obj"] = 100 * count/float(run_max)

    print ("result=")
    print (df_result)
    return df_result, df_obj_feas_gbest_final
    
    
def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

        
def main():
    # parameter setting
    (pro_para, alg_para, run_max) = get_param_class().get_param()
    #pro_para = [N, problem_type, delta]
    #alg_para = [alg_type, iter_max, m, "alg_name", **algorithm's other para.**]
    N = pro_para[0]
    problem_type = pro_para[1]
    d_exp = pro_para[2]
    d = pow(10, d_exp)

    alg_type = alg_para[0]
    iter_max = alg_para[1]
    m = alg_para[2]

    # instance
    prob = function(problem_type, N, d, alg_type)
    g_ = prob.constraint_function(np.zeros(N))
    optima = prob.get_opt()

    
    # get path
    dir_base = get_path(problem_type, N)
    str_clm = ['N','problem_type','alg_type','d','iter_max','m','run_max','g_num','optima']
    num_clm = [N,problem_type,alg_type,d,iter_max,m,run_max,len(g_),optima]   
    print(str_clm)
    print(num_clm)
    make_setfile(dir_base, str_clm, num_clm)
    

    # databox gene
    obj_gbest_box = np.zeros((iter_max, 2, run_max))
    time_box = np.zeros((run_max+1, 3))
    # [gbest_obj, gbest_vio, cbest_obj, cbest_vio, frequency update]
    obj_feas_gbest_cbest_box = np.zeros((iter_max, 5, run_max))
    obj_vio_box = np.zeros((iter_max, m, 2, run_max))

    # run loop    
    # time start
    start_time = time.time()
    print ("calculation started.")
    print('-----------------------------------')

    for run in range(0, run_max):    
        print('run/run_max = %d / %d' % (run+1, run_max))
        print('loop start')
        # get solution
        (x, obj_vio_box[:, :, :, run], obj_feas_gbest_cbest_subbox, fre_update_box) = get_sol_loop_class().main_loop(prob, alg_para, run, start_time)

        obj_feas_gbest_cbest_box[:, :4, run] = obj_feas_gbest_cbest_subbox
        obj_feas_gbest_cbest_box[:, -1, run] = fre_update_box
        
        now_time = time.time() 
        if run == 0:
            loop_cal_time = now_time - start_time
        else:
            loop_cal_time = now_time - cal_time - start_time
        cal_time = now_time - start_time 
        time_box[run, :] = np.array([loop_cal_time, loop_cal_time/60, loop_cal_time/3600])
        print('calculation time = %.3f sec = %.3f min' % (cal_time, cal_time/60))
        print ("feas_gbest: ", np.round(obj_feas_gbest_cbest_box[iter_max-1, [0, 1, -1], run], 3))
        print('loop end')
        print('-----------------------------------')

    print ("calculation finished")
    time_box[-1, :] = np.mean(time_box[:run_max, :], axis=0)
    time_box = np.round(time_box, decimals=4)
    print('mean time = %.3f sec = %.3f = min = %.3f = hour' % (time_box[-1, 0], time_box[-1, 1], time_box[-1, 2]))


    # result save
    # df_result: [[ave, std, max, min], [obj, vio]]
    # df_obj_feas_gbest_final: [run_max, [obj, vio]]
    idx = ['run'+str(i+1) for i in range(0, run_max)] + ['average']
    df_time = pd.DataFrame(time_box, index=idx, columns=['sec','min','hour'])
    df_time.to_csv(dir_base + "\\file\\time.csv")
    (df_result, df_obj_feas_gbest_final) = get_result(obj_feas_gbest_cbest_box[:, :3, :])
    df_result.to_csv(dir_base + "\\file\\result.csv")

    # obj_feas_gbest_cbest_box: (iter_max, 5, run_max)
    # [gbest_obj, gbest_vio, cbest_obj, cbest_vio, frequency update]
    run_list = ['run'+str(i+1) for i in range(0, run_max)]
    gbest_list = ['gbest_obj', 'gbest_vio', 'cbest_obj', 'cbest_vio', 'frequency update']
    df_final = pd.DataFrame(obj_feas_gbest_cbest_box[-1, :, :].T, index = run_list, columns=gbest_list)
    df_final.to_csv(dir_base + "\\file\\obj_feas_gbest_cbest_final.csv")

    # fre_update_array: (iter_max, run_max)
    fre_update_array = obj_feas_gbest_cbest_box[:, -1, :]
    df_fre_update = pd.DataFrame(fre_update_array, columns=run_list)
    df_fre_update.to_csv(dir_base + "\\file\\fre_update.csv")

    # obj_feas_gbest
    clm_list = ["obj", "vio"]
    #for i in range(0, 2):
    #    for run in range(0, run_max):
    #        df_ = pd.DataFrame(obj_feas_gbest_cbest_box[:, i, run], columns=[clm_list[i] + str(run)])
    #        if i == 0 and run == 0:
    #            df_obj_feas_gbest = df_.copy()
    #        else:
    #            df_obj_feas_gbest = pd.concat([df_obj_feas_gbest, df_], axis=1)            
    #df_obj_feas_gbest.to_csv(dir_base + "obj_feas_gbest.csv")
    

    #obj_vio_box ((iter_max, m, 2, run_max))
    for run in range(0, run_max):
        df_obj_vio = get_df_obj_vio(obj_vio_box[:, :, :, run], ["obj", "vio"])
        df_obj_vio.to_csv(dir_base + "\\file\\obj_vio_run" + str(run) + ".csv")
        df_feas_gbest = pd.DataFrame(obj_feas_gbest_cbest_box[:, :, run], columns=gbest_list)
        df_feas_gbest.to_csv(dir_base + "\\file\\gbest_run" + str(run) + ".csv")
        #df_x = pd.DataFrame(x_final_box[:, :, run])
        #df_x.to_csv(dir_base + "\\file\\x_run" + str(run) + ".csv")
   
    print ("file saving finished.")


    # figure save
    # [obj_min, obj_max, vio_min, vio_max]
    obj_max = np.amax(obj_feas_gbest_cbest_box[:, 0, :])
    obj_min = np.amin(obj_feas_gbest_cbest_box[:, 0, :])
    vio_max = np.amax(obj_feas_gbest_cbest_box[:, 1, :])
    minmax_abs = [0, np.abs(obj_max - optima), 0, vio_max]
    minmax = [0, obj_max/2, 0, vio_max/2]

    figure_label1 = ["iteration: $k$", "$|f(x)-f(x*)|$", "$v(x)$", "$|f(x)-f(x*)|$", "$v(x)$"] + minmax_abs
    figure_label2 = ["iteration: $k$", "update frequency", 0, iter_max]
    figure_label3 = ["objective: $f$", "violation: $v$", "$(f(xi), v(xi))$"] + minmax
    figure_label4 = ["objective: $f$", "violation: $v$", "$(f(x^1), v(x^1))$", "$(f(x^m), v(x^m))$"] + minmax
    figure_label33 = ["$x_1$", "$x_2$", "$xi$", "$xgbest$", prob.x_ul[0, 0], prob.x_ul[1, 0], prob.x_ul[0, 1], prob.x_ul[1, 1]]
    figure_label44 = ["iteration: $k$", "objective: $f(x)$", "violation: $g(x)$", "$f(x)$", "$g(x)$"] + minmax
    figure_label5 = ["objective: $f(x)$", "violation: $g(x)$", "$(f(xi), g(xi))$", "$(f(xgbest), g(xgbest))$"] + minmax
    figure_label6 = ["iteration: $k$", "feasible solution rate", 0, 1]
    figure_label7 = ["iteration: $k$", "gbest objective $f(x)$", "gbest violation: $g(x)$", "$f(x)$", "total $g(x)$", "up/low $g(x)$", "discrete $g(x)$"] + minmax

    for run in range(0, run_max):
        # obj and vio gbest trend
        # obj_feas_gbest_cbest_box = np.zeros((iter_max, 4, run_max))
        fig_file_name = dir_base + '\\fig\\obj_vio_feas_gbest_'+ str(run) + '.png'
        figure_save_class().gbest_trend(figure_label1, 
                                        range(0, iter_max), 
                                        np.abs(obj_feas_gbest_cbest_box[:, 0, run] - optima), 
                                        obj_feas_gbest_cbest_box[:, 1, run], 
                                        fig_file_name,
                                        scale = 'log')

        # fre_update trend
        fig_file_name = dir_base + '\\fig\\fre_update_'+ str(run) + '.png'
        figure_save_class().trend(figure_label2, range(0, iter_max), df_fre_update.iloc[:, run].values, fig_file_name)
        
#        if problem_type == 3 or problem_type == 5:
#            fig_file_name = dir_base + 'obj_vio_feas_gbest_uplow_dis'+ str(run) + '.png'
#            figure_save_class().gbest_trend_uplow_dis(figure_label6, range(0, iter_max), df_obj_feas_gbest.iloc[:, run].values, df_obj_feas_gbest.iloc[:, run + run_max].values, np.sum(feas_gbest_vio_box[:M_g, :, run], axis=0), np.sum(feas_gbest_vio_box[M_g:, :, run], axis=0), fig_file_name)


#        if problem_type == 1 or problem_type == 2:
            # position in solution space with contour
#            fig_file_name = dir_base + 'position_solution_space'+ str(run) + '.png'
#            figure_save_class().scatter_solution_space_contour(figure_label2, x_final_box[:, 0, run], x_final_box[:, 1, run], x_feas_gbest_final_box[:, run], X, Y, obj_mesh_box, feas_mesh_box, fig_file_name)
#        elif problem_type == 3 or problem_type == 4 or problem_type == 5:
            # position in solution space
#            for n in range(0, N-1):
#                figure_label2 = ["$x_{"+ str(n+1) + "}$", "$x_{"+ str(n+2) + "}$", "$xi$", "$xgbest$", x_ul[0, n], x_ul[1, n], x_ul[0, n+1], x_ul[1, n+1]]
#                fig_file_name = dir_base + 'position_solution_space'+ str(run) + '_' + str(n) + '_' + str(n+1) + '.png'
#                figure_save_class().scatter_solution_space(figure_label2, x_final_box[:, n, run], x_final_box[:, n+1, run], x_feas_gbest_final_box[n:n+2, run], fig_file_name)

        # all obj and vio trend
#        fig_file_name = dir_base + '\\fig\\obj_vio_all'+ str(run) + '.png'
#        figure_save_class().all_trend(figure_label3, range(0, iter_max), obj_vio_box[:, :, 0, run], obj_vio_box[:, :, 1, run], fig_file_name)

        # position in obj and vio space
#        fig_file_name = dir_base + 'position_obj_vio_space'+ str(run) + '.png'
#        figure_save_class().scatter_obj_vio_space(figure_label4, obj_vio_box[iter_max-1, :, 0, run], obj_vio_box[iter_max-1, :, 1, run], obj_feas_gbest_cbest_box[iter_max-1, :2, run], fig_file_name)

#        if problem_type == 1 or problem_type == 2:
            # position in obj and vio space with contour
#            fig_file_name = dir_base + 'position_obj_vio_space'+ str(run) + '.png'
#            figure_save_class().scatter_obj_vio_space_contour(figure_label4, obj_vio_box[iter_max-1, :, 0, run], obj_vio_box[iter_max-1, :, 1, run], obj_feas_gbest_cbest_box[iter_max-1, :2, run], obj_mesh_box, vio_mesh_box, feas_mesh_box, fig_file_name)
#        elif problem_type == 3 or problem_type == 4 or problem_type == 5:
            # position in obj and vio space
#            fig_file_name = dir_base + 'position_obj_vio_space'+ str(run) + '.png'
#            figure_save_class().scatter_obj_vio_space(figure_label4, obj_vio_box[iter_max-1, :, 0, run], obj_vio_box[iter_max-1, :, 1, run], obj_feas_gbest_cbest_box[iter_max-1, :2, run], fig_file_name)

        # feasible solution rate trend
#        fig_file_name = dir_base + 'feas_rate'+ str(run) + '.png'
#        figure_save_class().trend(figure_label5, range(0, iter_max), feas_rate_box[:, run], fig_file_name)

    print ("figure saving finished.")

    # time finish
    end_time = time.time()
    cal_time = end_time - start_time
    print('time = %f sec = %f min' % (cal_time, cal_time/60))

    
if __name__ == "__main__":
    main()
