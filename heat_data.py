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
from sklearn.decomposition import PCA
###
def heatmap_data(reaction):
    ###
    rE_file = os.path.join(os.path.expanduser('~'), 'Desktop/rE_data_20180521.csv')
    suf_file = os.path.join(os.path.expanduser('~'), 'Desktop/suf_data_20180508.csv')
    ts_file = os.path.join(os.path.expanduser('~'), 'Desktop/ts_data_20180521_E.csv')
    hab2_file = os.path.join(os.path.expanduser('~'), 'Desktop/Hab2_data_20180510_E.csv')
    hab3_file = os.path.join(os.path.expanduser('~'), 'Desktop/Hab3_data_20180518_E.csv')
    ch3ab_file = os.path.join(os.path.expanduser('~'), 'Desktop/CH3ab_data_20180514_E.csv')
    mix_file = os.path.join(os.path.expanduser('~'), 'Desktop/mix_data_20180514.csv')
    ###
    fig_file = os.path.join(os.path.expanduser('~'), 'Desktop/'+reaction+'_heat.png')
    ###
    files = locals()
    for key in files.keys():
        if reaction in key:
            df = pd.read_csv(files[key], index_col=0)
    ###
    paras = []
    for col in df.columns:
        if col not in ['cell', 'dop', 'name']:
            paras.append(col)
    X = df[paras]
    ##
    plt.subplots(figsize=(9, 9)) # 设置画面大小
    corr = X.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        ax = sns.heatmap(corr, annot=True, mask=mask, vmax=1, center=0, square=True)
    plt.title(reaction+'HeatMap')
    plt.savefig(fig_file, bbox='tight')
    plt.show()
    ###
###
def main():
    ###
    # paras
    # suf dO2_M4, dM4_l2O2
    # hab dH1_O2, dO2_M4, dM4_l2O2, aH1_O2_M4, aO8_O2_H1
    # ch3ab dH1_O2, dH1_C, dO2_M4, dC_M4, dM4_l2O2, aH1_O2_M4, aC_M4_O2, aO8_O2_H1, aC_M4_l2O2, aH1_C_M4
    # ts dH1_O2, dH1_C, dO2_M4, dC_M4, dM4_l2O2, aH1_O2_M4, aC_M4_O2, aO8_O2_H1, aC_M4_l2O2, aH1_C_H2
    ###
    heatmap_data('ts')
###
if __name__ == '__main__':
    main()
