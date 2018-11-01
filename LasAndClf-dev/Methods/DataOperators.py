#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: DataOperators.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六 10/27 21:07:14 2018
#########################################################################
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import pickle

def GetDS(dstype, n_feas='all'):
    'Get Data and Index'
    df = pd.read_csv('../Data/CH4_DataSet.csv', index_col=0)
    if dstype == 'Ea':
        df = df
        En = 4
    elif dstype == 'Ets':
        df = df.loc[df.loc[:,'E_ts']!='np.nan', :]
        En = 2
    elif dstype == 'Etsra':
        df = df.loc[df.loc[:,'E_tsra']!='np.nan', :]
        En = 3

    ''
    # 'name', 'mtype', 'E_ts', 'E_tsra', Ea: min(E_ts, E_tsra)
    indexs_cols = df.iloc[:,range(5)]
    # E_Hab3, E_CH3ab, Geos
    if n_feas == 'all':
        vals_cols = df.iloc[:,range(5,len(df.columns))]
    else:
        vals_cols = df.loc[:, n_feas]

    'Get DataSet'
    DS = {}
    DS['Etype'] = indexs_cols.loc[:, 'mtype'].values
    DS['target'] = indexs_cols.iloc[:, En].values.reshape(-1,1).astype(np.float64)
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
    GetDS()
