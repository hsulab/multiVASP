#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os 

import numpy as np
import pandas as pd

from sklearn import metrics
from sklearn.linear_model import LinearRegression 

from sklearn.preprocessing import StandardScaler

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


"""
Description:
    Plot classification figure with three kinds of data. 
    True values, BEP predictions and Structural predictions. 
Author:
    Jiayan XU, CCC, ECUST, 2018-2019. 
Notes: 
    paper figure 7.
"""


def ols_with_chosen_features(y, X):
    """Ordinary linear regression with input y and X, 
    return the function and r2.""" 
    # regression setting 
    ols = LinearRegression(fit_intercept=True, normalize=False)

    # fit and predict 
    ols.fit(X, y)
    y_p = ols.predict(X)

    # save model 
    coefs = ols.coef_  
    intercept = ols.intercept_ 
    r2 = metrics.r2_score(y, y_p)
    mse = metrics.mean_squared_error(y, y_p)

    return ols, r2 


def plt_ts_classification(ax, subtitle, Etype, Ets, Etsra):
    """Plot ts-ss energy v.s. ts-ra energy.""" 
    # init dict 
    en_ts = {'ts':[], 'tsra':[]}
    en_tsra = {'ts':[], 'tsra':[]}

    for i in range(len(Etype)):
        if Etype[i] == 'ts':
            en_ts['ts'].append(Ets[i])
            en_ts['tsra'].append(Etsra[i])
        elif Etype[i] == 'tsra':
            en_tsra['ts'].append(Ets[i])
            en_tsra['tsra'].append(Etsra[i])

    # subfigure general setting 
    ax.set_title(subtitle, fontsize=10)
    ax.set_xlabel('$E_{TS-ra}\ /\ eV$')
    ax.set_xlim(0.0, 1.6)
    ax.set_ylabel('$E_{TS-ss}\ /\ eV$')
    ax.set_ylim(0.0, 1.6)

    # plot the line y=x 
    #ax.plot([Etsra.min(), Etsra.max()], [Etsra.min(), Etsra.max()], 'k--', lw=2)
    ax.plot([0.2, 1.4], [0.2, 1.4], 'k--', lw=2)

    # scatter points 
    ax.scatter(en_ts['tsra'], en_ts['ts'], color='royalblue', marker='o')
    ax.scatter(en_tsra['tsra'], en_tsra['ts'], color='salmon', marker='x')


def plot_linear_classification(csv_path):
    """Regression with different methods and plot the classification."""
    # prepare data 
    df = pd.read_csv(csv_path, index_col=0)
    df = df.loc[df.loc[:, 'E_ts'] != 'np.nan', :]
    df = df.loc[df.loc[:, 'E_tsra'] != 'np.nan', :]

    # specific features 
    Etype = df.loc[:, 'mtype'].values 

    Ets = df.loc[:, 'E_ts'].values.astype(np.float64)
    Etsra = df.loc[:, 'E_tsra'].values.astype(np.float64) 
    
    # BEP relations
    Eh = df.loc[:, 'E_Hab3'].values.reshape(-1,1).astype(np.float64) 
    Ech3 = df.loc[:, 'E_CH3ab'].values.reshape(-1,1).astype(np.float64) 

    ols_ts_bep, dummy = ols_with_chosen_features(Ets, Eh+Ech3)
    Ets_bep = ols_ts_bep.predict(Eh+Ech3)

    ols_tsra_bep, dummy = ols_with_chosen_features(Etsra, Eh)
    Etsra_bep = ols_tsra_bep.predict(Eh)

    # Geo relations selected 
    '''
    feanames = ['E_CH3ab', 'E_Hab3', \
            'a_O2-M4-C_CH3ab', 'h_O2-C-M4-H1_CH3ab', 'd_H1-C_CH3ab', \
            'h_O2-H1-M4-C_CH3ab', 'a_O2-M4-H1_Hab3', 'a_O2-C-H1_CH3ab'] 
    '''
    feanames = ['E_CH3ab', 'E_Hab3', \
            'a_O2-M4-C_CH3ab', 'h_O2-C-M4-H1_CH3ab', 'd_H1-C_CH3ab', \
            'h_O2-H1-M4-C_CH3ab', 'a_O2-M4-H1_Hab3'] 
    X = df.loc[:, feanames].values.astype(np.float64) 

    s4y, s4X = StandardScaler().fit(Ets.reshape(-1,1)), StandardScaler().fit(X)
    y_s, X_s = s4y.transform(Ets.reshape(-1,1)), s4X.transform(X)

    ols_ts_geo, r2 = ols_with_chosen_features(y_s, X_s)
    Ets_geo_s = ols_ts_geo.predict(X_s)
    Ets_geo = s4y.inverse_transform(Ets_geo_s)

    # general figure setting 
    fig, ax = plt.subplots(1, 3, figsize=(14,4))
    plt.suptitle('Classification for Methane Activation')
    plt.tight_layout(pad=2.0, w_pad=4.0, h_pad=2.0)
    plt.subplots_adjust(left=0.08, bottom=None, right=0.95, top=0.88, \
            wspace=None, hspace=0.5)

    # true values
    plt_ts_classification(ax[0], '(a) True Values', Etype, Ets, Etsra)

    # bep values 
    plt_ts_classification(ax[1], '(b) BEP Relations', Etype, Ets_bep, Etsra_bep)

    # geo values 
    plt_ts_classification(ax[2], '(c) Structural descriptors corrected Relations', \
            Etype, Ets_geo, Etsra_bep)

    plt.savefig('./figures/fig7.png')
    #plt.show()
    

if __name__ == '__main__':
    plot_linear_classification('../CH4_3.csv')
