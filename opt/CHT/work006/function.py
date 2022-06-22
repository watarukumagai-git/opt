#coding: utf-8
import numpy as np
import random as rnd
import math

class Function:
    def __init__(self, load_pro, scaling_type, cost, demand, fac_coef):
        self.load_pro = load_pro
        self.problem_type = load_pro.problem_type
        self.N = load_pro.N
        self.xmin = load_pro.xmin
        self.xmax = load_pro.xmax
        self.scaling_type = scaling_type
        self.g_num = 0
        self.cost = cost
        self.demand = demand
        self.fac_coef = fac_coef

    def get_opt(self):
        if self.problem_type == 1 or self.problem_type == 2 or self.problem_type == 3:
            ep_f1_list = [0.5, 0.01, 0]
            ep_f1 = ep_f1_list[self.problem_type-1]
            ep_f2 = 0.1
            ep_d = 0.01
            de = 3
            eta = (de-ep_d)/6
            x_opt = np.zeros((self.load_pro.num_feat_total, self.load_pro.Time))
            for i in range(0, self.load_pro.num_feat_total):
                if i == 0 or i == 3:
                    x_opt[i, :] = 2*eta - (2*ep_f1 + ep_f2)/3
                elif i == 1 or i == 4:
                    x_opt[i, :] = eta + (ep_f2 - ep_f1)/3
                else:
                    x_opt[i, :] = 3*eta
            #obj_opt = 15.12, 22.96, 23.12
            obj_opt = (x_opt[0, :] + x_opt[3, :]).sum()
            x_opt = x_opt.reshape(self.N)
        else:
            obj_opt = 0
            x_opt = np.zeros(self.N)
            print('problem number is not preset.')
        return obj_opt, x_opt

    def basis_func(self, func_type, x, c):
        # func_type 1: linear
        if func_type == 1:
            f =  np.sum(c*x)
        return f

    def object_function(self, x__):
        # f = (x1[t] + x4[t]).sum(t=1:Time)
        # x__ = x__.reshape(self.N)
        c = self.cost.reshape(len(x__))
        return self.basis_func(1, x__, c)

    def get_oneside_vio(self, g_equal, lower, upper):
        return np.where((lower + upper)/2>=g_equal, lower - g_equal, g_equal - upper)

    def relax_const(self, eval_const, x, coef, lower, upper):
        """
        relax for constarint functions.

        Parameters
        ----------
        eval_const : object
            constraint function
        x : double (num_feat, Time)
            solution
        coef : double (num_feat,)
            coefficient for x
        lower : double (Time,)
            lower for x
        upper : double (Time,)
            upper for x

        Returns
        -------
        g_inequal : double (Time,)
            inequality constarints relaxed by lower/upper
        """
        # g_equal: (Time,)
        if x.ndim > 1:
            g_equal = np.array([eval_const(1, x[:, t], coef) for t in range(0, x.shape[1])])
        g_inequal = self.get_oneside_vio(g_equal, lower, upper)
        return g_inequal

    def get_vio_minmax(self, x__):
        # x__ : (N,)
        g_minmax = self.get_oneside_vio(x__, self.load_pro.x_ul[:,0], self.load_pro.x_ul[:,1])
        return g_minmax

    def get_vio_fac(self, x_2D, coef, epsilon):
        # x_2D: (num_feat, Time)
        # coef: (num_feat,)
        lower = -epsilon*np.ones(self.load_pro.Time)
        upper = epsilon*np.ones(self.load_pro.Time)
        # g_inequal : (Time,)
        g_inequal = self.relax_const(self.basis_func, x_2D, coef, lower, upper)
        return g_inequal

    def get_vio_demand(self, x_2D, coef, epsilon, demand):
        # x_2D: (num_feat, Time)
        # coef: (num_feat,)
        # demand: (Time,)
        lower = demand - epsilon
        upper = demand + epsilon
        # g_inequal : (Time,)
        g_inequal = self.relax_const(self.basis_func, x_2D, coef, lower, upper)
        return g_inequal

    def constraint_function(self, x__):
        def _get_const_facility(x_2D, epsilon_fac):
            # facility coef: array-(num_fac, num_unit_feat)
            # g_fac : (Time*num_fac,)
            g_fac = []
            for j in range(0, self.load_pro.num_fac):
                idx_x = self.load_pro.no_feat_fac[j]
                for i in range(0, len(self.fac_coef[j, :, 0])):
                    g_fac.append(self.get_vio_fac(x_2D[idx_x, :], self.fac_coef[j, i, :], epsilon_fac[i]))
            return np.array(g_fac)

        def _get_const_facility_diff(x_2D, epsilon_fac):
            # x_2D: array-(num_feat_total, Time)
            # facility coef: array-(num_fac, num_unit_feat)
            # g_fac : (Time*num_fac,)
            g_fac = []
            for j in range(0, self.load_pro.num_fac):
                idx_x = self.load_pro.no_feat_fac[j]
                for i in range(0, len(self.fac_coef[j, :, 0])):
                    g_fac.append(self.get_vio_fac(x_2D[idx_x, :], self.fac_coef[j, i, :], epsilon_fac[i]))
            return np.array(g_fac)

        def _get_const_demand(x_2D, epsilon_demand, coef_demand):
            # demand: (num_demand, Time)
            # g_demand : (Time*num_demand,)
            g_demand = []
            for j in range(0, self.load_pro.num_demand):
                idx_x = self.load_pro.no_feat_demand[j]
                g_demand.append(self.get_vio_demand(x_2D[idx_x, :], coef_demand[j, :], epsilon_demand, self.demand[j, :]))
            return np.array(g_demand)
            
        if self.problem_type == 1:
            epsilon_fac = [0.4608, 0.391646879364331, 3.6861]
            epsilon_demand = 0.01
        elif self.problem_type == 2:
            epsilon_fac = [1, 1, 4]
            epsilon_demand = 0.01
            
        if self.problem_type == 1 or self.problem_type == 2:
            x_2D = x__.reshape(self.load_pro.num_feat_total, self.load_pro.Time)
            # facility_violation
            # g11(x[t]) = (x2[t]-x2[t-1]+50) + (x3[t]-x3[t-1]+50) + (x4[t]-x4[t-1]+50)-b; t=2:Time
            # g12(x[t]) = x1[t] - 2*x2[t] + x3[t] + x4[t] + 0*x5[t]; t=1:Time
            # -ep_f1 <= g11(x[t]) <= ep_f1; t=1:Time
            # -ep_f2 <= g12(x[t]) <= ep_f2; t=1:Time
            g_fac_diff = _get_const_facility_diff(x_2D, epsilon_fac)
            g_fac = _get_const_facility(x_2D, epsilon_fac)
            # demand_violation
            # g3(x[t]) = x1[t] - demand[t]; t=1:Time
            # -ep_d+demand[t] <= g3(x[t])+demand[t] <= ep_d+demand[t]; t=1:Time
            coef_demand = np.ones((self.load_pro.num_demand, len(self.load_pro.no_feat_demand[0])))
            g_demand = _get_const_demand(x_2D, epsilon_demand, coef_demand)
            # because x is modified upper/lower
            # gminmax = self.get_vio_minmax(x__)
            # g = np.concatenate([gminmax, g_fac, g_demand])
            g = np.ravel(np.concatenate([g_fac, g_demand]))
        else:
            g = [0]
        return g