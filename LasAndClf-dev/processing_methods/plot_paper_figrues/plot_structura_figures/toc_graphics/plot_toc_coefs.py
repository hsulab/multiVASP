#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os 

import numpy as np
import pandas as pd

from sklearn import metrics
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


"""
paper figure 6.
"""


def generate_dataset_from_csv(target_name='Ea', fea_names='all'):
    """
    Description:
        Return a dictionary with mechanism types, target(activation energy),
        features(adsorption energies and geometrical descriptors) and their names.
    """
    # from csv file to dataframe 
    if os.path.exists(DS_CSV):
        df = pd.read_csv(DS_CSV, index_col=0)
    else:
        raise ValueError('DataSet CSV does not exist.')

    # choose different targets: preferred or specific activation energy (three kinds)
    if target_name == 'Ea':
        df = df
        E = 'mE'
    elif target_name == 'Edelta':
        df = df.loc[df.loc[:,'E_ts']!='np.nan', :]
        df = df.loc[df.loc[:,'E_tsra']!='np.nan', :]
        df.loc[:,'E_ts'] = df.loc[:,'E_ts'].values.astype(np.float64) - \
                df.loc[:,'E_tsra'].values.astype(np.float64)
        E = 'E_ts'
    elif target_name == 'Ets':
        df = df.loc[df.loc[:,'E_ts']!='np.nan', :]
        E = 'E_ts'
    elif target_name == 'Etsra':
        df = df.loc[df.loc[:,'E_tsra']!='np.nan', :]
        E = 'E_tsra'

    # 'name', 'mtype', 'E_ts', 'E_tsra', Ea: min(E_ts, E_tsra)
    nodescriptors = ['name', 'mtype', 'E_ts', 'E_tsra', 'Ea']
    indexs_cols = df.iloc[:, 0:len(nodescriptors)]

    # choose number of descriptors (E_Hab3, E_CH3ab, Geos, ...)
    if fea_names == 'all':
        vals_cols = df.iloc[:,range(len(nodescriptors),len(df.columns))]
    else:
        vals_cols = df.loc[:, fea_names]

    # Get DataSet
    DS = {}

    DS['Etype'] = indexs_cols.loc[:, 'mtype'].values
    DS['target'] = indexs_cols.loc[:,E].values.reshape(-1,1).astype(np.float64)
    DS['fea_names'] = vals_cols.columns.values
    DS['features'] = vals_cols.values.astype(np.float64)

    return DS


def stardard_scaling(y, X):
    """
    Description:
        StandardScaler Data.
    In:
        unnormalized data y and X.
    Out:
        normalized data: y_s and X_s.
        scaler function: s_y and s_X
    """
    # scale y
    scaler4y = StandardScaler().fit(y)
    y_scalered = scaler4y.transform(y)

    # scale X
    scaler4X = StandardScaler()
    X_scalered = scaler4X.fit_transform(X)

    return y_scalered, X_scalered, scaler4y, scaler4X


def randomize_folds(y, splits):
    """"""
    kf = KFold(n_splits=splits, shuffle=True, random_state=0)
    folds_index = []
    for train_index, test_index in kf.split(y):
        folds_index.append([train_index, test_index])

    return folds_index


def linear_regression_with_cv(y, X):
    # generate k-folds 
    n = 5
    folds_index = randomize_folds(y, n)
    MSEs, r2s = [], []
    ols = LinearRegression(fit_intercept=True, normalize=False, n_jobs=-1)
    for i in range(n):
        # get train and test set 
        fold = folds_index[i]
        train_index, test_index = fold[0], fold[1]
        y_train, X_train = y[train_index], X[train_index]
        y_test, X_test = y[test_index], X[test_index]

        # scale data 
        y_s, X_s, s4y, s4X = stardard_scaling(y_train, X_train)

        # train and test 
        ols.fit(X_s, y_s)

        y_test_s, X_test_s = s4y.transform(y_test), s4X.transform(X_test)
        y_p = ols.predict(X_test_s)

        MSE = metrics.mean_squared_error(y_test_s, y_p)
        MSEs.append(MSE)

        r2 = metrics.r2_score(y_test_s, y_p)
        r2s.append(r2)

    # mean MSE and standard MSE 
    MSEs = np.array(MSEs)

    return MSEs, r2s 


def feature_selection(Etype, features):
    """""" 
    # prepare data 
    DS = generate_dataset_from_csv(Etype, features.keys())
    y, X = DS['target'], DS['features']

    # feature selection 
    mean_MSEs, std_MSEs, mean_r2s, std_r2s = [], [], [], [] 
    feas_number = len(X[0])

    for i in range(feas_number):
        X_slice = []
        for j in range(i+1):
            X_slice.append(X.T[j])
        X_slice = np.array(X_slice).T
        MSEs, r2s = linear_regression_with_cv(y, X_slice)

        mean_MSEs.append(np.mean(MSEs)) 
        std_MSEs.append(np.var(MSEs)) 

        mean_r2s.append(np.mean(r2s)) 
        std_r2s.append(np.var(r2s))

    return mean_MSEs, std_MSEs, mean_r2s, std_r2s 


def plot_selected_features(ax, features, feanames):
    """"""
    # figure general setting 
    nfeatures = len(features.keys())

    ax.set_yticks(np.arange(nfeatures))
    ax.set_yticklabels(feanames, fontsize=10, fontweight='black')

    ax.set_xlabel('Coefficient', fontsize=16)
    ax.set_xlim(0, 1.0)
    #ax.invert_xaxis()

    # horizental bar 
    coefs = np.array(list(features.values()))
    pos1 = ax.barh(np.arange(nfeatures), np.fabs(coefs), 0.2, \
            color='b', label='Positive', alpha=0.8)

    neg_features = {}
    for i, coef in enumerate(coefs):
        if coef <= 0e-6:
            neg_features[i] = np.fabs(coef)

    neg1 = ax.barh([int(i) for i in neg_features.keys()], \
            list(neg_features.values()), 0.2, \
            color='r', label='Negative', alpha=0.8)

    for i, coef in enumerate(features.values()):
        ax.text(np.fabs(coef), i, '%s (%.2f)' %(feanames[i], coef), \
                fontsize=24, fontweight='bold')

    ax.set_axis_off()


def plot_main():
    """"""
    # figure general setting 
    fig, ax = plt.subplots(1, 4, figsize=(16, 5))

    plt.tight_layout(pad=2.0, w_pad=1.0, h_pad=2.0)
    plt.subplots_adjust(left=0.05, bottom=0.1, right=0.90, top=0.9, \
            wspace=0.3, hspace=0.3)

    # ts-ss part 
    features = {'a_O2-C-H1_CH3ab': -0.12, \
            'a_M4-C-H1_CH3ab': 0.11, 'a_O2-H1-M4_Hab3': 0.05, \
            'd_O2-C_CH3ab': 0.01}

    feanames = [r'$\bf{A_{O_{br}CH}^{CH_3^*}}$', \
            r'$\bf{A_{M_{cus}CH}^{CH_3^*}}$',\
            r'$\bf{A_{O_{br}HM_{cus}}^{H^*}}$', \
            r'$\bf{D_{O_{br}C}^{{CH}_3^*}}$']

    plot_selected_features(ax[0], features, feanames)

    # important features for ss 
    features = {'a_O2-M4-C_CH3ab': 0.40, 'd_H1-C_CH3ab': -0.31, \
            'h_O2-C-M4-H1_CH3ab': 0.30, 'h_O2-H1-M4-C_CH3ab': -0.29, \
            'a_O2-M4-H1_Hab3': -0.24}

    feanames = [r'$\bf{A_{O_{br}M_{cus}C}^{CH_3^*}}$', \
            r'$\bf{D_{HC}^{CH_3^*}}$', \
            r'$\bf{H_{O_{br}CM_{cus}H}^{CH_3^*}}$', \
            r'$\bf{H_{O_{br}HM_{cus}C}^{CH_3^*}}$', \
            r'$\bf{A_{O_{br}M_{cus}H}^{H^*}}$']

    plot_selected_features(ax[1], features, feanames)
    
    # ax2
    ax[2].text(0.3, 0.5, 'Geometrical\nDescriptors', fontsize=24, fontweight='bold')
    ax[2].text(0.1, 0.6, r'$\bf{\stackrel{ss}{\longleftarrow}}$', fontsize=36)
    ax[2].text(1.1, 0.6, r'$\bf{\stackrel{ra}{\longrightarrow}}$', fontsize=36)
    ax[2].set_axis_off()

    # ts-ra part 
    features = {'d_O2-H1_Hab3': -0.02, 'd_O2-M4_suf': 0.01}

    feanames = [r'$\bf{D_{O_{br}H}^{H^*}}$', \
            r'$\bf{D_{O_{br}M_{cus}}^{surface}}$']

    # ts-ra ax4 features selected by lasso 
    plot_selected_features(ax[3], features, feanames)

    #plt.show()
    plt.savefig('coefs.png', transparent=True)


if __name__ == '__main__':
    plot_main()
