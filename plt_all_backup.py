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
def collect_data():
    suf_file = os.path.join(os.path.expanduser('~'), 'Desktop/suf_data_20180508.csv')
    ts_file = os.path.join(os.path.expanduser('~'), 'Desktop/ts_data_20180510_E.csv')
    hab_file = os.path.join(os.path.expanduser('~'), 'Desktop/Hab2_data_20180510_E.csv')
    ch3ab_file = os.path.join(os.path.expanduser('~'), 'Desktop/CH3ab_data_20180514_E.csv')
    mix_file = os.path.join(os.path.expanduser('~'), 'Desktop/mix_data_20180514.csv')
    ###
    suf = pd.read_csv(suf_file, index_col=0)
    ts = pd.read_csv(ts_file, index_col=0)
    hab = pd.read_csv(hab_file, index_col=0)
    ch3ab = pd.read_csv(ch3ab_file, index_col=0)
    ###
    mix_df = ts[['cell', 'dop', 'name', 'Ea']]
    ###
    for row_index in mix_df.index:
        name = mix_df.loc[row_index, 'name'].strip('_ts')
        for suf_index in suf.index:
            if name in suf.loc[suf_index, 'name']:
                mix_df.loc[row_index, 'suf_dO2M4'] = round(suf.loc[suf_index, 'dO2_M4'] ,8)
                mix_df.loc[row_index, 'suf_dM4l2O2'] = round(suf.loc[suf_index, 'dM4_l2O2'] , 8)
        for hab_index in hab.index:
            if name in hab.loc[hab_index, 'name']:
                mix_df.loc[row_index, 'hab_dH1O2'] = round(hab.loc[hab_index, 'dH1_O2'], 8)
                mix_df.loc[row_index, 'hab_aH1O2M4'] = round(hab.loc[hab_index, 'aH1_O2_M4'], 8)
                mix_df.loc[row_index, 'E_H'] = round(hab.loc[hab_index, 'Eab_H'], 8)
        for ch3ab_index in ch3ab.index:
            if name in ch3ab.loc[ch3ab_index, 'name']:
                mix_df.loc[row_index, 'ch3_aH1O2M4'] = round(ch3ab.loc[ch3ab_index, 'aH1_O2_M4'], 8)
                mix_df.loc[row_index, 'ch3_aCM4O2'] = round(ch3ab.loc[ch3ab_index, 'aC_M4_O2'], 8)
                mix_df.loc[row_index, 'E_CH3'] = round(ch3ab.loc[ch3ab_index, 'Eab_CH3'], 8)
    ##
    for row_index in mix_df.index:
        name = mix_df.loc[row_index, 'name'].strip('_ts')
        mix_df.loc[row_index, 'E_CH3H'] = round(float(mix_df.loc[row_index, 'E_H']) + \
                float(mix_df.loc[row_index, 'E_CH3']), 8)
        mix_df.loc[row_index, 'Ea'] = round(mix_df.loc[row_index, 'Ea'], 8)
    ###
    mix_df.to_csv(mix_file, columns=['cell', 'dop', 'name', \
            'suf_dO2M4', 'suf_dM4l2O2', \
            'hab_dH1O2', 'hab_aH1O2M4', \
            'ch3_aH1O2M4', 'ch3_aCM4O2', \
            'E_H', 'E_CH3', 'E_CH3H', 'Ea'])
###
def main():
    data_path = os.path.join(os.path.expanduser('~'), 'Desktop/newdata')
    for csv_name in os.listdir(data_path):
        if 'rE' in csv_name:
            print(csv_name)
###
if __name__ == '__main__':
    main()
