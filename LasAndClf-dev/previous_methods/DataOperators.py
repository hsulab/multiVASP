#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import math
import pickle


def PosSelection(feanames, coefs):
    # get positive coefficients 
    name_coef = {}
    for name, coef in zip(feanames, coefs):
        if abs(coef) > 0:
            name_coef[name] = coef

    # sort fea by abs value
    nc_sorted = sorted(name_coef.items(), key=lambda d:abs(d[1]), reverse=True)
    nc_dict = {}
    for t in nc_sorted:
        nc_dict[t[0]] =t[1]

    return nc_dict


def GetDS(dstype, n_feas='all'):
    # get data and index 
    df = pd.read_csv('../Data/CH4_neo.csv', index_col=0)
    if dstype == 'Ea':
        df = df
        df = df.loc[df.loc[:,'E_CH3ab']!='np.nan', :]
        df = df.loc[df.loc[:,'E_CH3ab2']!='np.nan', :]
        En = 'mE'
    elif dstype == 'Ets':
        df = df.loc[df.loc[:,'E_ts']!='np.nan', :]
        df = df.loc[df.loc[:,'E_CH3ab']!='np.nan', :]
        En = 'E_ts'
    elif dstype == 'Etsra':
        df = df.loc[df.loc[:,'E_tsra']!='np.nan', :]
        En = 'E_tsra'

    ''
    # 'name', 'mtype', 'E_ts', 'E_tsra', Ea: min(E_ts, E_tsra)
    indexs_cols = df.iloc[:,range(5)]
    # E_Hab3, E_CH3ab, Geos
    if n_feas == 'all':
        vals_cols = df.iloc[:,range(5,len(df.columns))]
    else:
        vals_cols = df.loc[:, n_feas]

    # get dataSet 
    DS = {}
    DS['Etype'] = indexs_cols.loc[:, 'mtype'].values
    DS['target'] = indexs_cols.loc[:,En].values.reshape(-1,1).astype(np.float64)
    DS['features'] = vals_cols.values.astype(np.float64)
    DS['fea_names'] = vals_cols.columns.values

    return DS

def pltsave(figname):
    plt.savefig('./Pics/'+figname, tight='bbox')

def pkload(pk):
    'Load Pickle'
    with open('./PKs/'+pk, 'rb') as f:
        ret = pickle.load(f)
    return ret

def pkdump(pk, ret):
    'Dump Pickle'
    with open('./PKs/'+pk, 'wb') as f:
        pickle.dump(ret, f)

if __name__ == '__main__':
    GetDS('Ea')
