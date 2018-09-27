#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: plt_bivars.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 二  5/ 8 09:19:05 2018
#########################################################################
import os
###
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  
import numpy as np
import pandas as pd
import seaborn as sns  
from sklearn import preprocessing
###
def get_bivars(df1_name, para1, df2_name, para2):
    ###
    rE_file = os.path.join(os.path.expanduser('~'), 'Desktop/rE_data_20180514.csv')
    suf_file = os.path.join(os.path.expanduser('~'), 'Desktop/suf_data_20180508.csv')
    ts_file = os.path.join(os.path.expanduser('~'), 'Desktop/ts_data_20180510_E.csv')
    hab2_file = os.path.join(os.path.expanduser('~'), 'Desktop/Hab2_data_20180510_E.csv')
    hab3_file = os.path.join(os.path.expanduser('~'), 'Desktop/Hab3_data_20180510_E.csv')
    ch3ab_file = os.path.join(os.path.expanduser('~'), 'Desktop/CH3ab_data_20180514_E.csv')
    ###
    files = locals()
    ###
    for key in files.keys():
        if df1_name in key:
            df1 = pd.read_csv(files[key], index_col=0)
        if df2_name in key:
            df2 = pd.read_csv(files[key], index_col=0)
    ##
    cdn = pd.read_csv(ts_file, index_col=0)[['cell', 'dop', 'name']]
    ###
    for row_index in cdn.index:
        name = cdn.loc[row_index, 'name'].strip('_ts')
        for df1_index in df1.index:
            if name in df1.loc[df1_index, 'name']:
                cdn.loc[row_index, df1_name+'_'+para1] = round(float(df1.loc[df1_index, para1]), 8)
        for df2_index in df2.index:
            if name in df2.loc[df2_index, 'name']:
                cdn.loc[row_index, df2_name+'_'+para2] = round(float(df2.loc[df2_index, para2]), 8)
    ##
    return cdn[df1_name+'_'+para1], cdn[df2_name+'_'+para2]
###
def main():
    ###
    # paras
    # suf dO2_M4, dM4_l2O2
    # hab dH1_O2, dO2_M4, dM4_l2O2, aH1_O2_M4, aO8_O2_H1
    # ch3ab dH1_O2, dH1_C, dO2_M4, dC_M4, dM4_l2O2, aH1_O2_M4, aC_M4_O2, aO8_O2_H1, aC_M4_l2O2, aH1_C_M4
    # ts dH1_O2, dH1_C, dO2_M4, dC_M4, dM4_l2O2, aH1_O2_M4, aC_M4_O2, aO8_O2_H1, aC_M4_l2O2, aH1_C_H2
    ###
    hab2_file = os.path.join(os.path.expanduser('~'), 'Desktop/Hab2_data_20180510_E.csv')
    hab2 = pd.read_csv(hab2_file, index_col=0)
    print(hab2.columns)
    ###
    d_col = []
    a_col = []
    for col in hab2.columns:
        if col not in ['cell', 'dop', 'name']:
            if col[0] == 'd':
                d_col.append(col)
            if col[0] == 'a':
                a_col.append(col)
    ###
    sns.jointplot(hab2[d_col[0]]+hab2[d_col[1]], hab2['Eab_H']).set_axis_labels("x")
    plt.show()

###
if __name__ == '__main__':
    main()
