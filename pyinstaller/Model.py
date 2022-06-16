#coding: utf-8 
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_decomposition import PLSRegression
from sklearn.linear_model import LinearRegression


class Model:
    def __init__(self, modeling_mode):
        self.modeling_mode = modeling_mode
        if modeling_mode == 'RF':
            self.model = RandomForestRegressor(n_jobs=-1, random_state=2525)
        elif modeling_mode == 'PLS':
            # NUM_LV: number of latent variables
            NUM_LV = 2
            self.model = PLSRegression(n_components=NUM_LV)
        elif modeling_mode == 'MLR':
            self.model = LinearRegression()
        else:
            self.model = 0
            print('modeling-mode does not work.')

    def fit(self, X_tra, y_tra):
        self.model.fit(X_tra, y_tra)

    def predict(self, X_val):
        if self.modeling_mode == 'PLS':
            pre = self.model.predict(X_val).reshape(len(X_val))
        else:
            pre = self.model.predict(X_val)
        return pre