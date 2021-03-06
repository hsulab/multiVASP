#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: E2rE.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 二  5/ 8 09:19:05 2018
#########################################################################
import os
import sys
import time
import numpy as np
import pandas as pd
###
def E2rE(csv_file):
    df = pd.read_csv(csv_file, index_col=0)
    paras = []
    ###
    metal_color = {'Ti':'black','V':'grey','Ge':'green','Mo':'cyan',\
            'Ru':'lightseagreen','Rh':'skyblue','Os':'blue','Ir':'navy'}
    ###
    for i in range(1,len(df.columns)):
        paras.append(df.columns[i])
    ###
    cells = []
    dops = []
    for row_index in df.index:
        name = df.loc[row_index, 'name']
        for metal in metal_color.keys():
            if metal in name.split('_')[0]:
                cells.append(metal+'O2')
            if len(name.split('_')) >1 :
                if metal in name.split('_')[1]:
                    dops.append(metal)
            else:
                if metal in name.split('_')[0]:
                    dops.append('pure')
    ###
    names = np.array(df['name'])
    ###
    E_CH4 = -24.07015819;
    E_H = -1.11501367; E_CH3 = -18.21859244
    ###
    E_Hab2 = []; E_Hab3 = []
    E_CH3ab = []; E_CH3ab2 = []
    E_ts = []; E_tsra = []
    E_fs = []; E_fsra = []
    ##
    suf_E = np.array(df['suf_E']);
    Hab2_E = np.array(df['Hab2_E']); Hab3_E = np.array(df['Hab3_E'])
    CH3ab_E = np.array(df['CH3ab_E']); CH3ab2_E = np.array(df['CH3ab2_E'])
    ts_E = np.array(df['ts_E']); tsra_E = np.array(df['tsra_E'])
    fs_E = np.array(df['fs_E']); fsra_E = np.array(df['fsra_E'])
    for i in df.index:
        'Hab'
        if Hab2_E[i] != 'np.nan':
            E_Hab2.append(float(round(float(Hab2_E[i])-float(suf_E[i])-E_H, 8)))
        else:
            E_Hab2.append('np.nan')
        if Hab3_E[i] != 'np.nan':
            E_Hab3.append(float(round(float(Hab3_E[i])-float(suf_E[i])-E_H, 8)))
        else:
            E_Hab3.append('np.nan')
        'CH3ab'
        if CH3ab_E[i] != 'np.nan':
            E_CH3ab.append(float(round(float(CH3ab_E[i])-float(suf_E[i])-E_CH3, 8)))
        else:
            E_CH3ab.append('np.nan')
        if CH3ab2_E[i] != 'np.nan':
            E_CH3ab2.append(float(round(float(CH3ab2_E[i])-float(suf_E[i])-E_CH3, 8)))
        else:
            E_CH3ab2.append('np.nan')
        'ts'
        if ts_E[i] != 'np.nan':
            E_ts.append(float(round(float(ts_E[i])-float(suf_E[i])-E_CH4, 8)))
        else:
            E_ts.append('np.nan')
        if tsra_E[i] != 'np.nan':
            E_tsra.append(float(round(float(tsra_E[i])-float(suf_E[i])-E_CH4, 8)))
        else:
            E_tsra.append('np.nan')
        'fs'
        if fs_E[i] != 'np.nan':
            E_fs.append(float(round(float(fs_E[i])-float(suf_E[i])-E_CH4, 8)))
        else:
            E_fs.append('np.nan')
        if fsra_E[i] != 'np.nan':
            E_fsra.append(float(round(float(fsra_E[i])-float(suf_E[i])-E_CH4, 8)))
        else:
            E_fsra.append('np.nan') 
    ###
    new_df = pd.DataFrame({'name': names, 'cell': cells, 'dop': dops, \
            'E_Hab2': E_Hab2, 'E_Hab3': E_Hab3, 'E_CH3ab': E_CH3ab, 'E_CH3ab2': E_CH3ab2, \
            'E_ts': E_ts, 'E_tsra': E_tsra, 'E_fs': E_fs, 'E_fsra': E_fsra})
    new_df = new_df.sort_values(by=['name', 'cell', 'dop'], ascending=True)
    new_df = new_df.reset_index(drop=True)
    ###
    rE_csv_name = 'rE_data_' + time.strftime("%Y%m%d", time.localtime()) + '.csv'
    rE_csv = os.path.join(os.path.expanduser('~'), 'Desktop/CH4_DS/'+rE_csv_name)
    new_df.to_csv(rE_csv, columns=['name', 'cell', 'dop', 'E_Hab2', 'E_Hab3', 'E_CH3ab', 'E_CH3ab2', \
            'E_ts', 'E_tsra', 'E_fs', 'E_fsra'])
###
def main():
    if len(sys.argv) == 2:
        E_date = sys.argv[1]
        csv_file = os.path.join(os.path.expanduser('~'), 'Desktop/CH4_DS/E_data_2018'+E_date+'.csv')
        E2rE(csv_file)
    else:
        print('E2rE.py [Date of EnergyFile]')
###
if __name__ == '__main__':
    main()
