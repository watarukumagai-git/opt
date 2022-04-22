#coding: utf-8
import numpy as np
import pandas as pd
import math
import os
from os import path

#from .distance import distance_class

class scaling_class:
    def scaling_values(self, prob_, values_):
        def min_max(x, axis=None):
            eps = pow(10,-15)
            min_ = x.min(axis=axis, keepdims=True)
            max_ = x.max(axis=axis, keepdims=True)
            return (x - min_)/(max_ - min_ + eps)

        if prob_.scaling_type == 1:
            values = values_
        elif prob_.scaling_type == 2:
            # values: (m, g_num)
            if values_.ndim > 1:
                values = np.array([min_max(values_[:, j]) for j in range(0, values_.shape[1])]).T
            # values: (m, 1)
            else:
                values = min_max(values_)
        return values

class get_obj_class:
    def get_obj(self, prob, x_):
        # x_: (m, N)
        if x_.ndim > 1:
            # obj_: (m, 1)
            obj_ = np.array([prob.object_function(x_[i, :]) for i in range(0, x_.shape[0])]).T
        # x_: (N)
        else:
            # obj_: (1)
            obj_ = prob.object_function(x_)
        return obj_

    def get_opt_sol(self, prob):
        opt_sol = []
        for i in range(0, prob.num_of_signs):
            opt_sol.append((-prob.sign_entries[i][0], prob.sign_entries[i][3]))
        return opt_sol

    def get_dist_penalty(self, x_, archive, pena_para):
        epsilon = pena_para[0]
        penalty_coef = pena_para[1]
        penalty = 0
        for sol in archive:
            dis = distance_class().hamming_distance(x_, sol)
            if dis < epsilon:
                penalty = penalty + abs(epsilon - dis) / len(x_)
        penalty = penalty_coef * penalty
        return penalty


    def get_filter_penalty(self, x_, archive, pena_para):
        penalty_coef = pena_para[2]
        penalty = penalty_coef*np.sum(x_) / len(x_)
        return penalty


class get_vio_class:
    def get_rank(self, array_):
        clm = ["value", "rank"]
        df_ = pd.DataFrame(np.zeros((len(array_), 2)), columns=clm)
        df_[clm[0]] = array_
        list_ = list(set(list(array_)))
        list_.sort()
        rank = 0
        for ele_ in list_:
            df_.loc[df_[clm[0]]==ele_, clm[1]] = rank
            rank = rank + len(df_.loc[df_[clm[0]]==ele_, clm[1]])
        rank_ = df_[clm[1]].values
        return rank_

    def get_each_vio(self, prob_, x_):
        # x_: (m, N)
        if x_.ndim > 1:
            # each_g: (m, L)
            each_g = np.array([prob_.constraint_function(x_[i, :]) for i in range(0, x_.shape[0])])
        # x_: (N)
        else:
            # each_g: (L)
            each_g = prob_.constraint_function(x_)
        each_vio = np.where(each_g<0, 0, each_g)
        return each_vio


    # vio = sigma_{j=1, L} orm_j
    # vio = sigma_{j=1, L} (orm_max - orm_j / orm_max - orm_min)
    def get_vio(self, prob_, x_, type_vio = 'sum'):
        each_vio = self.get_each_vio(prob_, x_)
        if type_vio == 'sum':
            if each_vio.ndim > 1:
                vio = np.sum(each_vio, axis=1)
            else:
                vio = np.sum(each_vio)
        elif type_vio == 'max':
            if each_vio.ndim > 1:
                vio = np.max(each_vio, axis=1)
            else:
                vio = np.max(each_vio)
        return vio, each_vio


    def get_const_ranking(self, prob_, x_, delta):
        # num points
        m_ = len(x_)
            
        # constraints violation
        (v, Nv, M_g, M_h) = self.get_vio_each_const(prob_, x_, delta)

        # v: (m_, M_g+M_h)
        # v_sum: (m_, 1) sum violation
        v_sum = np.sum(v, axis=1)

        # num of constraint violation ranking
        rank_Nv = self.get_rank(Nv) + 1

        # constraints violation ranking
        rank_v = np.zeros((m_, M_g+M_h))
        for j in range(0, M_g+M_h):
            rank_v[:, j] = self.get_rank(v[:, j]) + 1

        # rank_v: (m_, M_g+M_h)
        rank_v_df = pd.DataFrame(np.concatenate([rank_Nv.reshape(m_, 1), rank_v], 1))
        rank_v_df["sum v_rank"] = rank_v_df.sum(axis = 1)

        # total ranking
        v_rank = self.get_rank(rank_v_df["sum v_rank"].values)
        rank_v_df["rank"] = v_rank

        return v_rank, v_sum
