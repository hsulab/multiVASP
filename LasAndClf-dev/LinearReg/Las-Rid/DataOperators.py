#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: DataOperators.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六 10/27 21:07:14 2018
#########################################################################
import pandas as pd
import pickle

def GetDS():
    'Get Data and Index'
    df = pd.read_csv('../../CH4_DataSet.csv', index_col=0)
    # 'name', 'mtype', 'E_ts', 'E_tsra'
    indexs_cols = df.iloc[:,range(4)]
    # Ea: min(E_ts, E_tsra), E_Hab2, E_Hab3, E_CH3ab, E_CH3ab2(wait), Geos
    vals_cols = df.iloc[:,range(4,len(df.columns))]

    'Get DataSet'
    DS = {}
    DS['target'] = vals_cols.iloc[:,range(1)].values
    DS['features'] = vals_cols.iloc[:,range(1,len(vals_cols.columns))].values
    DS['fea_names'] = vals_cols.columns[1:].values
    return DS


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
