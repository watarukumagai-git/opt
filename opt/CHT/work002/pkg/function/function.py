#coding: utf-8
import numpy as np
import random as rnd
import math

class function:
    def __init__(self, problem_type_, N_, d_, scaling_type):
        self.problem_type = problem_type_
        if problem_type_ <= 5:
            self.xmin = -5
            self.xmax = 5
        self.x_ul = np.ones((2, N_))
        self.x_ul[0,:] = self.x_ul[0,:]*self.xmin
        self.x_ul[1,:] = self.x_ul[1,:]*self.xmax
        self.d = d_
        self.N = N_
        self.scaling_type = scaling_type
        self.g_num = 0

    def get_opt(self):
        if self.problem_type <= 3:
            center = 1
        elif self.problem_type == 4:
            center = self.xmin + 0.25
        return center - math.sqrt(self.d)

        
    def basis_func(self, func_type, x, c):
        # func_type 1: sphere
        if func_type == 1:
            f =  np.sum(np.power(x-c, 2))/self.N
        # func_type 2: exp
        elif func_type == 2:
            f =  np.exp(10*x)-1
        # func_type 3: sqrt
        elif func_type == 3:
            f = np.sign(x)*np.power(np.abs(x), 0.25)
        # func_type 4: cos
        elif func_type == 4:
            f =  -np.sum(np.cos(2*math.pi*(x-c)))/self.N
        # func_type 5: linear
        elif func_type == 5:
            f =  np.sum(x)/self.N
        return f

    def object_function(self, x__):
        # Prob.1~4: linear
        if self.problem_type <= 4:
            return self.basis_func(5, x__, 0)

    def get_vio_minmax(self, x__):
        cen = (self.x_ul[0,:] + self.x_ul[1,:])/2
        gminmax = np.where(cen.T>=x__, self.x_ul[0,:].T - x__, x__ - self.x_ul[1,:].T)
        return gminmax

    def constraint_function(self, x__):
        gminmax = self.get_vio_minmax(x__)
        if self.problem_type == 1:
            g1 = self.basis_func(1, x__, 1) - self.d
        elif self.problem_type == 2:
            g_ = self.basis_func(1, x__, 1) - self.d
            g1 = self.basis_func(2, g_, 0)
        elif self.problem_type == 3:
            g_ = self.basis_func(1, x__, 1) - self.d
            g1 = self.basis_func(3, g_, 0)
        elif self.problem_type == 4:
            g1 = self.basis_func(4, x__, 0.25) + np.cos(2*math.pi*math.sqrt(self.d))
        g = np.concatenate([gminmax, [g1]])
        self.g_num = len(g)
        return g
