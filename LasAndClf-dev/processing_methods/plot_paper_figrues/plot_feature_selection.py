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

    ax.set_title('Descriptors Selected by Lasso', fontsize=16)

    ax.set_yticks(np.arange(nfeatures))
    ax.set_yticklabels(feanames, fontsize=10, fontweight='black')

    ax.set_xlabel('Coefficient', fontsize=16)
    ax.set_xlim(0, 1.0)

    # horizental bar 
    coefs = np.array(list(features.values()))
    pos1 = ax.barh(np.arange(nfeatures), np.fabs(coefs), 0.5, \
            color='b', label='Positive', alpha=0.8)

    neg_features = {}
    for i, coef in enumerate(coefs):
        if coef <= 0e-6:
            neg_features[i] = np.fabs(coef)

    neg1 = ax.barh([int(i) for i in neg_features.keys()], \
            list(neg_features.values()), 0.5, \
            color='r', label='Negative', alpha=0.8)

    for i, coef in enumerate(features.values()):
        ax.text(np.fabs(coef), i, '%.2f' %coef, \
                fontsize=12, fontweight='bold')

    ax.legend(handles=[pos1, neg1], loc=1)


def plot_feature_selection(ax, Etype, features):
    """"""
    ax.set_title('Feature Selection by Linear Regression', fontsize=16)

    ax.set_xlabel('First N Features', fontsize=16)

    ax.set_ylabel('Statistics', fontsize=16)
    ax.set_ylim(-0.2, 1.0)

    mean_MSEs, std_MSEs, mean_r2s, std_r2s = feature_selection(Etype, features) 

    mr2 = ax.scatter(range(1, len(mean_r2s)+1), mean_r2s, \
            color='g', marker='o', label='Mean $R^2$')
    mmse = ax.scatter(range(1, len(mean_MSEs)+1), mean_MSEs, \
            color='r', marker='o', label='Mean MSE')

    '''
    sr2 = ax.scatter(range(1, len(std_r2s)+1), std_r2s, \
            color='b', marker='x', label='Variance $R^2$')
    smse = ax.scatter(range(1, len(std_MSEs)+1), std_MSEs, \
            color='r', marker='x', label='Variance MSE')
    '''

    ax.legend(handles=[mr2, mmse], loc=5)


def plot_best_regression(ax, Etype, features, first_n):
    """"""
    DS = generate_dataset_from_csv(Etype, list(features.keys())[:first_n])
    y, X = DS['target'], DS['features']
    y_s, X_s, s4y, s4X = stardard_scaling(y, X)

    ols = LinearRegression(fit_intercept=True, normalize=False, n_jobs=-1)
    ols.fit(X_s, y_s)

    y_p = s4y.inverse_transform(ols.predict(X_s))
    r2 = metrics.r2_score(y, y_p)
    mse = metrics.mean_squared_error(y, y_p)

    ax.set_title('First %d Descriptors Linear Regression' %first_n, fontsize=16)

    ax.set_xlabel('True Values / eV', fontsize=16)
    ax.set_xlim(-0.75, 1.75)

    ax.set_ylabel('Predicted Values / eV', fontsize=16)
    ax.set_ylim(-0.75, 1.75)

    ax.scatter(y, y_p)
    ax.plot([-0.5, 1.5], [-0.5, 1.5], 'k--', lw=4)
    ax.text(-0.5, 1.0, '${R^2}$=%0.2f, MSE=%0.2f' %(r2, mse), \
            fontsize=12)


def plot_main():
    """"""
    # figure general setting 
    fig, ax = plt.subplots(2, 3, figsize=(16, 9))
    plt.tight_layout(pad=2.0, w_pad=2.0, h_pad=2.0)
    plt.subplots_adjust(left=0.1, bottom=None, right=0.90, top=0.85, \
            wspace=0.3, hspace=0.5)

    plt.suptitle('Feature Selection of Geometrical Descriptors', \
            fontsize=24, fontweight='bold')

    # ts-ss part 
    ''' old
    features = {'E_CH3ab': 0.84, 'E_Hab3': 0.50, \
            'a_O2-M4-C_CH3ab': 0.41, 'd_H1-C_CH3ab': -0.32, \
            'h_O2-C-M4-H1_CH3ab': 0.30, 'h_O2-H1-M4-C_CH3ab': -0.29, \
            'a_O2-M4-H1_Hab3': -0.24, 'a_O2-C-H1_CH3ab': -0.13, \
            'a_M4-C-H1_CH3ab': 0.11, 'a_O2-H1-M4_Hab3': 0.05, \
            'd_O2-C_CH3ab': 0.02}

    feanames = ['$E_{{CH}_3^*}$', '$E_{H^*}$', \
            '$A_{O_{br}-M_{cus}-C}^{CH_3^*}$', '$D_{H-C}^{CH_3^*}$', \
            '$H_{O_{br}-C-M_{cus}-H}^{CH_3^*}$', \
            '$H_{O_{br}-H-M_{cus}-C}^{CH_3^*}$', \
            '$A_{O_{br}-M_{cus}-H}^{H^*}$', '$A_{O_{br}-C-H}^{CH_3^*}$', \
            '$A_{M_{cus}-C-H}^{CH_3^*}$', '$A_{O_{br}-H-M_{cus}}^{H^*}$', \
            '$D_{O_{br}-C}^{{CH}_3^*}$']
    '''
    features = {'E_CH3ab': 0.84, 'E_Hab3': 0.50, \
            'a_O2-M4-C_CH3ab': 0.40, 'd_H1-C_CH3ab': -0.31, \
            'h_O2-C-M4-H1_CH3ab': 0.30, 'h_O2-H1-M4-C_CH3ab': -0.29, \
            'a_O2-M4-H1_Hab3': -0.24, 'a_O2-C-H1_CH3ab': -0.12, \
            'a_M4-C-H1_CH3ab': 0.11, 'a_O2-H1-M4_Hab3': 0.05, \
            'd_O2-C_CH3ab': 0.01}

    feanames = ['$E_{{CH}_3^*}$', '$E_{H^*}$', \
            '$A_{O_{br}-M_{cus}-C}^{CH_3^*}$', '$D_{H-C}^{CH_3^*}$', \
            '$H_{O_{br}-C-M_{cus}-H}^{CH_3^*}$', \
            '$H_{O_{br}-H-M_{cus}-C}^{CH_3^*}$', \
            '$A_{O_{br}-M_{cus}-H}^{H^*}$', '$A_{O_{br}-C-H}^{CH_3^*}$', \
            '$A_{M_{cus}-C-H}^{CH_3^*}$', '$A_{O_{br}-H-M_{cus}}^{H^*}$', \
            '$D_{O_{br}-C}^{{CH}_3^*}$']

    # ts-ss ax1 features selected by lasso 
    plot_selected_features(ax[0][0], features, feanames)
    
    # ts-ss ax2 feature selection 
    plot_feature_selection(ax[0][1], 'Ets', features)
    ax[0][1].text(-2, 1.2, '(a) Surface-stabilized Mechanism', \
            fontsize=20, fontweight='normal')
    
    # ts-ss ax3 best linear regression 
    plot_best_regression(ax[0][2], 'Ets', features, 7)

    # ts-ra part 
    ''' old
    features = {'E_Hab3': 0.92, \
            'd_O2-C_CH3ab': 0.04, 'd_O2-H1_Hab3': -0.02, 'd_O2-M4_suf': 0.01, \
            'h_O2-M4-H1-C_CH3ab': 0.01}

    feanames = ['$E_{H^*}$', \
            '$D_{O_{br}-C}^{CH_3^*}$', '$D_{O_{br}-H}^{H^*}$', \
            '$D_{O_{br}-M_{cus}}^{surface}$', '$H_{O_{br}-M_{cus}-H-C}^{CH_3^*}$']
    '''
    features = {'E_Hab3': 0.86, \
            'd_O2-H1_Hab3': -0.02, 'd_O2-M4_suf': 0.01}

    feanames = ['$E_{H^*}$', \
            '$D_{O_{br}-H}^{H^*}$', \
            '$D_{O_{br}-M_{cus}}^{surface}$']

    # ts-ra ax4 features selected by lasso 
    plot_selected_features(ax[1][0], features, feanames)

    # ts-ra ax5 feature selection 
    plot_feature_selection(ax[1][1], 'Etsra', features)
    ax[1][1].text(0.5, 1.2, '(b) Radical-like Mechanism', \
            fontsize=20, fontweight='normal')

    # ts-ra ax6 best linear regression 
    plot_best_regression(ax[1][2], 'Etsra', features, 1)

    #plt.show()
    plt.savefig('./figures/fig6.png')


if __name__ == '__main__':
    DS_CSV = '../CH4_10.csv'
    plot_main()
