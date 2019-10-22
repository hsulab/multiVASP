#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys

import numpy as np
import pandas as pd

from sklearn import metrics
from sklearn.linear_model import LinearRegression

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


"""
Description:
    Plot activation energy with different adsorption energy 
    combinations. 
Author:
    Jiayan XU, CCC, ECUST, 2018-2019. 
Notes:
    Paper figure 4.
"""


def generate_dataset(dstype):
    """Generate X with different adsorption energies."""
    # Get Total DataSet 
    df = pd.read_csv('./fE_data_20190902.csv', index_col = 0)
    feas_E = ['E_ts', 'E_tsra', 'E_Hab2','E_Hab3','E_CH3ab','E_CH3ab2']

    # Get index and values 
    if dstype == 'ts':
        DS = {}
        df = df.loc[df.loc[:,'E_ts']!='np.nan', :]
        #df = df.loc[df.loc[:,'E_CH3ab']!='np.nan', :]
        df = df.loc[df.loc[:,'E_CH3ab2']!='np.nan', :]

        DS['target'] = df.loc[:, 'E_ts'].values.astype('float').reshape(-1,1)

        DS['Hab2_CH3ab'] = (df.loc[:, 'E_Hab2'].values.astype('float') + \
                df.loc[:, 'E_CH3ab'].values.astype('float')).reshape(-1,1)

        DS['Hab2_CH3ab2'] = (df.loc[:, 'E_Hab2'].values.astype('float') + \
                df.loc[:, 'E_CH3ab2'].values.astype('float')).reshape(-1,1)

        DS['Hab3_CH3ab'] = (df.loc[:, 'E_Hab3'].values.astype('float') + \
                df.loc[:, 'E_CH3ab'].values.astype('float')).reshape(-1,1)

        DS['Hab3_CH3ab2'] = (df.loc[:, 'E_Hab3'].values.astype('float') + \
                df.loc[:, 'E_CH3ab2'].values.astype('float')).reshape(-1,1)

    elif dstype == 'tsra':
        DS = {}
        df = df.loc[df.loc[:,'E_tsra']!='np.nan', :]

        DS['target'] = df.loc[:, 'E_tsra'].values.astype('float').reshape(-1,1)

        DS['Hab2'] = df.loc[:, 'E_Hab2'].values.astype('float').reshape(-1,1)

        DS['Hab3'] = df.loc[:, 'E_Hab3'].values.astype('float').reshape(-1,1)

    else: 
        raise ValueError('No such datdtype. Only support ts or tsra.')

    return DS


def bep_regression(dstype, feaname):
    # Pre and Scaler Data 
    DS = generate_dataset(dstype)
    y, X = DS['target'], DS[feaname]

    # LinearRegression 
    model = LinearRegression(fit_intercept=True, normalize=False, n_jobs=-1)
    model.fit(X, y)

    y_p = model.predict(X)
    r2 = metrics.r2_score(y, y_p)
    mse = metrics.mean_squared_error(y, y_p)

    print(model.coef_, model.intercept_)

    return y, y_p, r2, mse


def plt_bep():
    # figure general setting 
    fig, ((ax1, ax2, ax5), (ax3, ax4, ax6)) = plt.subplots(nrows=2, ncols=3, figsize=(16,9))
    #plt.suptitle('BEP for Methane Activation', fontsize=20, fontweight='bold')
    plt.tight_layout(pad=2.0, w_pad=2.0, h_pad=2.0)
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.95, top=0.9, \
            wspace=0.3, hspace=0.3)

    plt.suptitle('Linear Relations using Adsorption Energies of Different Configurations', \
            fontsize=24, fontweight='bold')

    # fuction for plt 
    def plt_subfig(ax, dtype, feaname, subtitle, textloc=(-0.5, 1.2)):
        y, y_p, r2, mse = bep_regression(dtype, feaname)
        print(feaname, r2, mse)
        ax.set_title(subtitle, fontsize=20)
        ax.scatter(y, y_p, edgecolors=(0, 0, 0))
        ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
        ax.text(textloc[0], textloc[1], '${R^2}$=%0.2f, MSE=%0.2f' %(r2, mse), \
                fontsize=16)
        ax.set_xlabel('True Values / eV', fontsize=16)
        ax.set_ylabel('Predicted Values / eV', fontsize=16)

    # bep for ts 
    plt_subfig(ax1, 'ts', 'Hab2_CH3ab', '(a) $E_{ss} \propto E_{H^{ot}} + E_{{{CH}_3}^v}$')
    plt_subfig(ax2, 'ts', 'Hab2_CH3ab2', '(b) $E_{ss} \propto E_{H^{ot}} + E_{{{CH}_3}^p}$')
    plt_subfig(ax3, 'ts', 'Hab3_CH3ab', '(c) $E_{ss} \propto E_{H^{in}} + E_{{{CH}_3}^v}$')
    plt_subfig(ax4, 'ts', 'Hab3_CH3ab2', '(d) $E_{ss} \propto E_{H^{in}} + E_{{{CH}_3}^p}$')

    # bep for tsra 
    plt_subfig(ax5, 'tsra', 'Hab2', '(e) $E_{ra} \propto E_{H^{ot}}$', (0.0, 1.5))
    plt_subfig(ax6, 'tsra', 'Hab3', '(f) $E_{ra} \propto E_{H^{in}}$', (0.0, 1.5))

    plt.savefig('./figures/fig4.png')
    #plt.show()


if __name__ == '__main__':
    plt_bep()
