#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from DataOperators import GetDS
from DataOperators import pkload
from DataOperators import pkdump
from DataOperators import pltsave

def FeaSelection():
    'Pre Data'
    print('Preparing Data...')
    #fea_names = ['E_CH3ab', 'h_O5-M2-O6-M1_hab3']
    fea_names = ['E_CH3ab', 'h_O1-O2-O3-M1_hab3', \
            'a_O2-O6-M2_hab3']

    DS = GetDS('Ets', fea_names)
    y, X = DS['target'], DS['features']

    X.T[1] = np.sin(X.T[1])
    X.T[2] = np.sin(X.T[2])

    'Feature Selection'
    ols = LinearRegression(fit_intercept=True, normalize=False)
    ols.fit(X, y)

    y_p = ols.predict(X)

    'Save Model'
    print(ols.coef_)
    print(ols.intercept_)
    print(ols.score(X, y))
    print(metrics.mean_squared_error(y_p, y))

def OldSS():
    ''
    DS = GetDS('Ets', ['E_Hab3', 'E_CH3ab'])
    y = DS['target']
    X = DS['features']

    X = (X.T[0]+X.T[1]).reshape(-1,1)
    
    ols=LinearRegression()
    ols.fit(X, y)

    print(ols.coef_)
    print(ols.intercept_)
    print(ols.score(X, y))

def OldRA():
    ''
    DS = GetDS('Etsra', ['E_Hab3'])
    y = DS['target']
    X = DS['features']
    
    ols=LinearRegression()
    ols.fit(X, y)

    print(ols.coef_)
    print(ols.intercept_)
    print(ols.score(X, y))

def Clf():
    'Pre Data'
    df = pd.read_csv('../Data/CH4_neo.csv', index_col=0)
    df = df.loc[df.loc[:,'E_ts']!='np.nan', :]
    df = df.loc[df.loc[:,'E_tsra']!='np.nan', :]

    #n_feas = ['E_Hab3', 'E_CH3ab', 'h_O5-M2-O6-M1_hab3']
    n_feas = ['E_Hab3', 'E_CH3ab', \
            'h_O1-O2-O3-M1_hab3', 'a_O2-O6-M2_hab3']
    indexs_cols = df.iloc[:,range(5)]
    vals_cols = df.loc[:, n_feas]

    DS = {}
    DS['Etype'] = indexs_cols.loc[:, 'mtype'].values
    En = ['E_ts','E_tsra']
    DS['target'] = indexs_cols.loc[:,En].values.astype(np.float64)
    DS['features'] = vals_cols.values.astype(np.float64)
    DS['fea_names'] = vals_cols.columns.values

    Etype = DS['Etype']
    Ets = DS['target'].T[0]
    Etsra = DS['target'].T[1]

    Eh = DS['features'].T[0]
    Ech3 = DS['features'].T[1]
    Dihe = DS['features'].T[2]
    Ange = DS['features'].T[3]

    def tsclf(Ets, Etsra):
        ts = {'ts':[],'tsra':[]}
        tsra = {'ts':[],'tsra':[]}
        for i in range(len(Etype)):
            if Etype[i] == 'ts':
                ts['ts'].append(Ets[i])
                ts['tsra'].append(Etsra[i])
            elif Etype[i] == 'tsra':
                tsra['ts'].append(Ets[i])
                tsra['tsra'].append(Etsra[i])

        return ts, tsra

    # BEP relations
    #Ets_bep = 0.39*(Eh+Ech3)+2.11
    Ets_bep = 0.40*(Eh+Ech3)+2.13
    Etsra_bep = 0.90*Eh+3.73

    # Geo relations
    #Ets_geo = 0.30*Ech3+14*np.sin(Dihe)+0.63
    Ets_geo = 0.37*Ech3+4.69*np.sin(Dihe)+11.54*np.sin(Ange)+0.52
    Etsra_geo = 0.90*Eh+3.73

    ''
    fig, ax = plt.subplots(1,3, figsize=(14,4))
    plt.suptitle('Classification for Methane Activation')
    plt.tight_layout(pad=2.0, w_pad=4.0, h_pad=2.0)
    plt.subplots_adjust(left=0.08, bottom=None, right=0.95, top=0.88, \
            wspace=None, hspace=0.5)

    # true values
    ts, tsra = tsclf(Ets, Etsra)
    #print(len(ts['tsra']), len(ts['ts']))
    #print(len(tsra['tsra']), len(tsra['ts']))
    print(tsra)
    ax[0].scatter(ts['tsra'], ts['ts'], color='royalblue', marker='o')
    ax[0].scatter(tsra['tsra'], tsra['ts'], color='salmon', marker='o')
    ax[0].plot([Etsra.min(), Etsra.max()], [Etsra.min(), Etsra.max()], 'k--', lw=2)
    ax[0].set_title('(a) True Values', fontsize=10)
    ax[0].set_xlabel('$E_{TS-ra}\ /\ ev$')
    ax[0].set_ylabel('$E_{TS-ss}\ /\ ev$')

    # bep values
    ts, tsra = tsclf(Ets_bep, Etsra_bep)
    ax[1].scatter(ts['tsra'], ts['ts'], color='royalblue', marker='o')
    ax[1].scatter(tsra['tsra'], tsra['ts'], color='salmon', marker='o')
    ax[1].plot([Etsra.min(), Etsra.max()], [Etsra.min(), Etsra.max()], 'k--', lw=2)
    ax[1].set_title('(b) BEP Relations', fontsize=10)
    ax[1].set_xlabel('$E_{TS-ra}\ /\ ev$')
    ax[1].set_ylabel('$E_{TS-ss}\ /\ ev$')
    
    # geo values
    ts, tsra = tsclf(Ets_geo, Etsra_geo)
    ax[2].scatter(ts['tsra'], ts['ts'], color='royalblue', marker='o')
    ax[2].scatter(tsra['tsra'], tsra['ts'], color='salmon', marker='o')
    ax[2].plot([Etsra.min(), Etsra.max()], [Etsra.min(), Etsra.max()], 'k--', lw=2)
    ax[2].set_title('(c) Relations including Geometrical Descriptors', fontsize=10)
    ax[2].set_xlabel('$E_{TS-ra}\ /\ ev$')
    ax[2].set_ylabel('$E_{TS-ss}\ /\ ev$')
    
    pltsave('clf.png')
    

if __name__ == '__main__':
    #FeaSelection()
    #OldSS()
    Clf()
