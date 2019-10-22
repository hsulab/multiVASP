#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: plt_data.py
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
def norm_data(geo_file, rE_file):
    ### read data
    geo_df = pd.read_csv(geo_file, index_col=0)
    rE_df = pd.read_csv(rE_file, index_col=0) 
    geo_file_name = os.path.basename(geo_file).split('.')[0]
    ###
    if 'suf' in geo_file_name:
        E_dict = {}
    else:
        if 'Hab' in geo_file_name:
            reaction = 'Eab_H'
        elif 'CH3ab' in geo_file_name:
            reaction = 'Eab_CH3'
        elif 'ts' in geo_file_name:
            reaction = 'Ea'
        ### get E
        E_dict = {}
        for row_index in rE_df.index:
            if rE_df.loc[row_index, reaction] != 'np.nan':
                E_dict[rE_df.loc[row_index, 'name']] = rE_df.loc[row_index, reaction]
        ### insert E in geo_df
        E_list = []
        for row_index in geo_df.index:
            for name in E_dict.keys():
                if name in geo_df.loc[row_index, 'name']:
                    E_list.append(E_dict[name])
        ##
        geo_df.insert(len(geo_df.columns), reaction, E_list)
        geo_df.to_csv(os.path.join(os.path.expanduser('~'), 'Desktop/'+geo_file_name+'_E.csv'))
        ##
        for j in range(4, len(geo_df.columns)):
            geo_df[geo_df.columns[j]] = preprocessing.scale(geo_df[geo_df.columns[j]])
    ### save data
    norm_geo_df = geo_df
    return norm_geo_df
###
def visual_data_pairplot(geoE_file, norm_geo_df):
    geoE_file_name = os.path.basename(geoE_file).split('.')[0].split('_')[0]
    ### get number paras
    num_paras = []
    number = len(norm_geo_df.columns)
    for i in range(4, number):
        num_paras.append(norm_geo_df.columns[i])
    ###
    def plt_norm_geo(norm_geo_df, num_paras):
        sns.set_style("whitegrid")
         ###
        grid = sns.PairGrid(data=norm_geo_df, vars=num_paras)
        ###
        grid.map_upper(sns.regplot, x_ci='sd')
        grid.map_diag(plt.hist, bins = 10, edgecolor = 'k');
        grid.map_lower(plt.scatter)
    ###
    ###
        fig_file = os.path.join(os.path.expanduser('~'), \
                'Desktop/methane_pics/'+geoE_file_name+'_reg.png')
        plt.savefig(fig_file, bbox_inches='tight')
    ###
    plt_norm_geo(norm_geo_df, num_paras)
###
def main():
    rE_file = os.path.join(os.path.expanduser('~'), 'Desktop/rE_data_20180514.csv')
    ###
    ts_file = os.path.join(os.path.expanduser('~'), 'Desktop/ts_data_20180510.csv')
    hab_file = os.path.join(os.path.expanduser('~'), 'Desktop/Hab2_data_20180510.csv')
    ch3ab_file = os.path.join(os.path.expanduser('~'), 'Desktop/CH3ab_data_20180514.csv')
    ###
    tsE_file = os.path.join(os.path.expanduser('~'), 'Desktop/ts_data_20180510_E.csv')
    habE_file = os.path.join(os.path.expanduser('~'), 'Desktop/Hab2_data_20180510_E.csv')
    ch3abE_file = os.path.join(os.path.expanduser('~'), 'Desktop/CH3ab_data_20180514_E.csv')
    ###
    if not os.path.exists(tsE_file):
        norm_ts_df = norm_data(ts_file, rE_file)
        visual_data_pairplot(tsE_file, norm_ts_df)
    ###
    if not os.path.exists(habE_file):
        norm_ts_df = norm_data(hab_file, rE_file)
        visual_data_pairplot(habE_file, norm_ts_df)
    ###
    if not os.path.exists(ch3abE_file):
        norm_ts_df = norm_data(ch3ab_file, rE_file)
        visual_data_pairplot(ch3abE_file, norm_ts_df)
###
def hot():

    # Draw a heatmap with the numeric values in each cell
    f, ax = plt.subplots(figsize=(9, 6))
    sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)

###
if __name__ == '__main__':
    main()
