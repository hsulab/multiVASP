#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import os
import time
import numpy as np
import pandas as pd

from sklearn import metrics
from sklearn.linear_model import Lasso, LinearRegression

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold, RepeatedKFold

from mpi4py import MPI


"""
Description:
    Percentile LASSO version MPI, an algorithm extracts 
    features from a sheer volume of data.
    This is the integrated version, including massive CV lasso 
    training, hyperparameter theta and alpha, and final features 
    with positive coefficients extraction.
Author:
    Jiayan XU, CCC, ECUST, 2018-2019.
Reference:
    S. Roberts, G. Nowak, 
    Computational Statistics and Data Analysis, 70, 2014, 198–211.
Scheme:
    step 0. prepare data.
    step 1. train LASSO with different alphas.
    step 2. choose hyperparameter theta to determine alpha.
    step 3. extract features with positive coefficients.
"""


# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 
# How time flies ... 
# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 
def timer(func):
    """Count Time."""
    def inner(*args, **kwargs): #1
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(str(func.__name__)+' TakeTime: ', round(end-start, 4), 's')
        return ret #2
    return inner


# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 
# Data Preparation and Useful Functions
# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 
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


# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 
# Percentile-LASSO 
# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 
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


def randomize_repeated_folds(y, splits, repeats):
    """
    Description:
        Get randomized k-folds from sklearn function, 
        and arrange them in dict.
    """
    # get randomized k-folds
    rkf = RepeatedKFold(n_splits=splits, n_repeats=repeats, random_state=0)

    # rearrange folds
    folds = {}
    for i in range(1, repeats+1):
        folds[i] = []

    i, j = 0, 0
    for train_index, test_index in rkf.split(y):
        if j % splits == 0:
            i += 1
        folds[i].append([train_index, test_index])
        j += 1

    return folds


def train_test(y_train, X_train, y_test, X_test, a=0.01): 
    """
    Description:
        Train LASSO with training data and test MeanSquareError on test data. 
        Note the scale of test data should use the parametres of the scale of 
        training data which has done for training.
    """
    # Scaler Use the Train Scaler. That is why i dont use cross_validate. 
    y_train_s, X_train_s, sy, sX = stardard_scaling(y_train, X_train) 
    
    # Lasso for TrainSet 
    las = Lasso(alpha=a, fit_intercept=True, normalize=False, \
            max_iter=10000, random_state=None, selection='random')
    las.fit(X_train_s, y_train_s)

    # Predict on TestSet
    y_test_s = sy.transform(y_test) 
    X_test_s = sX.transform(X_test)
    y_test_p = las.predict(X_test_s)

    # get mean square error
    MSE = metrics.mean_squared_error(y_test_s, y_test_p)

    return MSE


def lasso_using_alphas(y, X, kfold, alphas):
    """
    Description:
        Train LASSO with a series of alphas at given k-folds.
    IN:
        y, X, kfold, alphas
    OUT:
        best_alpha, r2_score, n_poscoef
    """
    # mean mean square errors 
    MeanMSEs = [] 

    # alphas = np.linspace(0.01, 1, 100)
    for a in alphas:
        a_MSEs = []
        for i in range(len(kfold)):
            # Get train and test set 
            train_index = kfold[i][0]
            y_train, X_train = y[train_index], X[train_index]

            test_index = kfold[i][1]
            y_test, X_test = y[test_index], X[test_index]
            
            # Train and Test
            a_MSE = train_test(y_train, X_train, y_test, X_test, a)
            a_MSEs.append(a_MSE)

        # append average MSE on a fold
        MeanMSEs.append(np.mean(a_MSEs))

    # get Best, having same aloha is fine
    best_index = MeanMSEs.index(min(MeanMSEs)) 
    best_alpha = alphas[best_index]

    # Here y and X are original data, which should be std.
    y_s, X_s, s4y, s4X= stardard_scaling(y, X)

    # train lassp with best hyper-parameters
    best_las = Lasso(alpha=best_alpha, fit_intercept=True, normalize=False, \
            max_iter=10000, random_state=None, selection='random')
    best_las.fit(X_s, y_s)

    # get r2score and coefs
    r2_score = round(best_las.score(X_s, y_s), 2)

    return best_alpha, r2_score, best_las.coef_ 


def extract_nonzero_coefs(feanames, coefs):
    """Get Positive Coef"""
    name_coef = {}
    for name, coef in zip(feanames, coefs):
        if abs(coef) > 1e-6:
            name_coef[name] = coef
    
    # sort fea by abs value
    nc_sorted = sorted(name_coef.items(), key=lambda d:abs(d[1]), reverse=True)
    nc_dict = {}
    for t in nc_sorted:
        nc_dict[t[0]] =t[1]

    return nc_dict


@timer
def mpiLasso(comm):
    """
    Description:
        Percentile LASSO with MPI which is the main function of 
        Percentile-LASSO.
    """
    # MPI setting 
    comm_rank = comm.Get_rank()
    comm_size = comm.Get_size()

    # Get DS
    DS = generate_dataset_from_csv(Etype)
    y, X = DS['target'], DS['features']
    feanames = DS['fea_names']

    # Print Initial Setting and Scatter Folds
    if comm_rank == 0:
        # log
        content = '<- Percentile-LASSO Setting ->\n'
        content += 'Processing Data --> %s\n' %Etype
        content += 'K-Folds Setting --> splits: %d repeats: %d\n' \
                %(cv_splits, cv_repeats)
        content += 'TestAlphs --> From %f to %f Total %d\n' \
                %(test_alphas[0], test_alphas[-1], len(test_alphas))
        content += ' Generating %d [%d-Fold]s \n' %(cv_repeats, cv_splits)
        content += '\n'
        print(content, flush=True)

        # folds is a dict, {1:fold}
        folds = randomize_repeated_folds(y, splits=cv_splits, repeats=cv_repeats)

        folds_list = [] # [num,[[],[],[],...]]
        for number, fold in folds.items():
            folds_list.append([number, fold])

        folds_scatter = []
        folds_num = len(folds.keys())
        n = int(folds_num/comm_size)
        for i in range(comm_size):
            if i*n+n < n*comm_size:
                start, end = i*n, i*n+n
                folds_scatter.append(folds_list[start:end])
            else:
                start = i*n
                folds_scatter.append(folds_list[start:])
    else:
        folds_scatter = None

    # Process Folds
    local_folds = comm.scatter(folds_scatter, root=0)

    content = '<- Slot' + str(comm_rank) + ' Percentile-LASSO Begin->\n'
    best_alphas = []
    for num_fold in local_folds: 
        # get fold and its number
        num, fold = num_fold[0], num_fold[1]

        # lasso
        best_alpha, r2_score, coefs = lasso_using_alphas(y, X, fold, test_alphas)
        best_alphas.append(best_alpha)
        
        # get nonzero coefficients
        positive_coefs = extract_nonzero_coefs(feanames, coefs)

        # print
        content += '-'*20 + '\n'
        content += 'Fold <%d-%d> \n' %(comm_rank, num)
        content += 'LasCV --> BestAlpha: %s \n' %str(best_alpha) 
        content += 'OneShot --> BestR2Score: %s \n' %str(r2_score) 
        content += 'OneShot --> N_PosCoefs: %s \n' %str(len(positive_coefs))
        for feaname, coef in positive_coefs.items():
            content += '%s -> %.4f\n' %(feaname, coef)

    content += '-'*20 + '\n'
    content += '<- Slot %d Percentile-LASSO Done->\n' %comm_rank
    content += '\n'

    print(content, flush=True)
    gathered_alphas = comm.gather(best_alphas, root=0)
    if comm_rank == 0:
        return np.array(gathered_alphas).ravel()
    else:
        return None


# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 
# Theta Selection
# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 
def extract_lasso_coefficients(Etype, a):
    """
    Description:
        Train LASSO with best alpha.
        Extract features' names and coefficients(>0).
    IN:
        Etype - energy type, a - alpha
    OUT:
        name_coef - dict, {name: coef}
    """
    # get complete dataframe
    DS = generate_dataset_from_csv(Etype)
    y, X = DS['target'], DS['features']
    feanames = DS['fea_names']

    # train Lasso with best alpha
    las = Lasso(alpha=a, fit_intercept=True, \
            normalize=False, max_iter=10000, \
            random_state=None, selection='random')

    y_s, X_s, sy, sX = stardard_scaling(y, X)
    las.fit(X_s, y_s) 

    # get coefficients 
    coefs = las.coef_
    
    # get nonzero coefficients
    if len(coefs) != 0:
        name_coef = extract_nonzero_coefs(feanames, coefs)
    else:
        name_coef = {}

    # calc scores 
    y_p = las.predict(X_s)
    mse = metrics.mean_squared_error(y_s, y_p)
    r2 = metrics.r2_score(y_s, y_p)

    return name_coef, mse, r2 


def linear_regression_with_cv(y, X, cv_splits, cv_repeats):
    """y=reduced_y, X=reduced_X"""
    ols = LinearRegression(fit_intercept=True, normalize=False)

    ols_MeanMSEs = []
    folds = randomize_repeated_folds(y, splits=cv_splits, repeats=cv_repeats)
    for kfold in folds.values():
        ols_MSE = 0
        for i in range(len(kfold)):
            train_index, test_index = kfold[i][0], kfold[i][1]
            y_train, X_train = y[train_index], X[train_index]
            y_test, X_test = y[test_index], X[test_index]

            ry_s, rX_s, r_sy, r_sX = stardard_scaling(y_train, X_train)
            ols.fit(rX_s, ry_s)
            ry_p = ols.predict(r_sX.transform(X_test))
            
            ols_MSE += metrics.mean_squared_error(r_sy.transform(y_test), ry_p)

        ols_MeanMSEs.append(ols_MSE/len(kfold))

    return ols_MeanMSEs


@timer
def ThetaSelection(Etype='Ets', cv_splits=5, cv_repeats=1, \
        best_alphas=[0.1], test_thetas=np.linspace(0.50, 1, 11)):
    """
    Description:
        Theta Selection
    IN:
        ...
    OUT:
        information
    """
    # out current best alphas 
    content = 'Gathered BestAlphas: %s\n' %str(best_alphas)
    content += 'Use %d best alphas. Max: %.4f Min: %.4f\n' \
            %(len(best_alphas), np.max(best_alphas), np.min(best_alphas))
    content += '\n'

    # out theta selection setting 
    content += '<- Theta-Selection Setting ->\n'
    content += 'K-Folds Setting --> splits: %d repeats: %d\n' \
            %(tcv_splits, tcv_repeats)
    content += 'TestThetas --> From %f to %f Total %d\n' \
            %(test_thetas[0], test_thetas[-1], len(test_thetas))
    content += '\n'

    # out theta selection part 
    content += '<- Theta Selection START ->\n'

    # choose theta by linear regression with cross-validation
    theta_MeanMSEs = []
    for theta in test_thetas:
        # get alpha with given theta
        alpha_by_theta = round(np.percentile(best_alphas, theta*100), 3)
        name_coef, mse, r2 = extract_lasso_coefficients(Etype, alpha_by_theta)

        if len(name_coef.keys()) != 0:
            # get data selected by lasso
            reduced_DS = generate_dataset_from_csv(Etype, name_coef.keys())
            reduced_y = reduced_DS['target']
            reduced_X = reduced_DS['features']

            # ordinary linear regression
            ols_MeanMSEs = linear_regression_with_cv(reduced_y, reduced_X, cv_splits, cv_repeats)
            mean_MSEs = np.mean(ols_MeanMSEs)
        else:
            mean_MSEs = 1e6
        
        theta_MeanMSEs.append(mean_MSEs)

        # log
        content += 'Theta <%0.2f> Alpha: %.4f MSE: %.4f\n' \
                %(theta, alpha_by_theta, mean_MSEs)

    # get best theta
    if len(theta_MeanMSEs) != len(set(theta_MeanMSEs)):
        print('Warning -- There may be the same mean MSE for different theta value!!!')

    best_index = theta_MeanMSEs.index(min(theta_MeanMSEs))
    best_theta = test_thetas[best_index]

    # get best alpha according to best theta
    alpha_by_theta = round(np.percentile(best_alphas, best_theta*100), 3)

    # log
    content += '<- Theta Selection DONE ->\n'
    content += '\n'

    content += '<- Selected HyerParameter ->\n'
    content += 'Best Theta --> ' + str(best_theta) + '\n'
    content += 'Selected Alpha --> ' + str(alpha_by_theta) + '\n'
    
    # log
    print(content, flush=True)

    return best_theta, alpha_by_theta 


# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 
# main routine 
# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 
if __name__ == '__main__':
    # dataset path 
    DS_CSV = '../CH4_10.csv'

    # set parameters
    Etype = 'Etsra'
    
    '''
    cv_splits = 5; cv_repeats = 100
    test_alphas = np.linspace(0.001, 0.5, 500)
    '''
    cv_splits = 5; cv_repeats = 100
    test_alphas = np.linspace(0.001, 0.5, 500)
    
    '''
    tcv_splits = 5; tcv_repeats = 1
    test_thetas = np.linspace(0.50, 1, 11)
    '''
    tcv_splits = 5; tcv_repeats = 1
    test_thetas = np.linspace(0.50, 1, 11)

    # Init MPI
    comm = MPI.COMM_WORLD

    # step 1.
    best_alphas = mpiLasso(comm) # cuz a list in a list
    
    if comm.Get_rank() == 0: 
        best_theta, alpha_by_theta = ThetaSelection(Etype, \
                tcv_splits, tcv_repeats, \
                best_alphas, test_thetas)

        positive_coefs, mse, r2 = extract_lasso_coefficients(Etype, alpha_by_theta)
        for name, coef in positive_coefs.items():
            print('\'%s\': %.2f,' %(name, coef))
        print('Model Score: mse --> %.2f r2 --> %.2f' %(mse, r2))
