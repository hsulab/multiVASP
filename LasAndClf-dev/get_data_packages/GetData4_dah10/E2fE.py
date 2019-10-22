#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import numpy as np
import pandas as pd

"""
Calculate and save reaction energy without ZPE.
"""


def rE2fE(E_file, F_file):
    # Read csv and Merge csv
    E_df = pd.read_csv(E_file, index_col=0)
    F_df = pd.read_csv(F_file, index_col=0)
    df = pd.merge(E_df, F_df, on='name')
    
    # Get Features Names
    metals= ['Ti', 'V', 'Cr', 'Mn', 'Ge', \
            'Mo', 'Ru', 'Rh', 'Os', 'Ir']

    fea_names = []
    for i in range(1,len(df.columns)):
        fea_names.append(df.columns[i])

    cells, dops = [], []
    for row_index in df.index:
        name = df.loc[row_index, 'name']
        for metal in metals:
            if metal in name.split('_')[0]:
                cells.append(metal+'O2')
            if len(name.split('_')) >1 :
                if metal in name.split('_')[1]:
                    dops.append(metal)
            else:
                if metal in name.split('_')[0]:
                    dops.append('pure')

    # Set first column
    names = np.array(df['name'])

    # Moleculer Energy Ignore FS
    E_CH4 = -24.07015819 + 1.18812
    E_H = -1.11501367 + 0.00172024
    E_CH3 = -18.21859244 + 0.792677

    E_Hab2 = []; E_Hab3 = []
    E_CH3ab = []; E_CH3ab2 = []
    E_ts = []; E_tsra = []

    # Set Energy
    suf_E = np.array(df['suf_E']);
    Hab2_E = np.array(df['Hab2_E']); Hab3_E = np.array(df['Hab3_E'])
    CH3ab_E = np.array(df['CH3ab_E']); CH3ab2_E = np.array(df['CH3ab2_E'])
    ts_E = np.array(df['ts_E']); tsra_E = np.array(df['tsra_E'])

    # Set Freguency
    Hab2_F = np.array(df['Hab2_F']); Hab3_F = np.array(df['Hab3_F'])
    CH3ab_F = np.array(df['CH3ab_F']); CH3ab2_F = np.array(df['CH3ab2_F'])
    ts_F = np.array(df['ts_F']); tsra_F = np.array(df['tsra_F'])

    def calc_energy(system, surface, molecule, zpe):
        return round(float(system)-float(surface)-float(molecule)+float(zpe), 8)

    banned_list = ['no_rdir', 'no_printout', 'not_converg', 'np.nan']
    for i in df.index:
        'Hab'
        if Hab2_E[i] not in banned_list and Hab2_F[i] not in banned_list:
            E_Hab2.append(calc_energy(Hab2_E[i], suf_E[i], E_H, Hab2_F[i]))
        else:
            E_Hab2.append('np.nan')
        if Hab3_E[i] not in banned_list and Hab3_F[i] not in banned_list:
            E_Hab3.append(calc_energy(Hab3_E[i], suf_E[i], E_H, Hab3_F[i]))
        else:
            E_Hab3.append('np.nan')
        'CH3ab'
        if CH3ab_E[i] not in banned_list and CH3ab_F[i] not in banned_list:
            E_CH3ab.append(calc_energy(CH3ab_E[i], suf_E[i], E_CH3, CH3ab_F[i]))
        else:
            E_CH3ab.append('np.nan')
        if CH3ab2_E[i] not in banned_list and CH3ab2_F[i] not in banned_list:
            E_CH3ab2.append(calc_energy(CH3ab2_E[i], suf_E[i], E_CH3, CH3ab2_F[i]))
        else:
            E_CH3ab2.append('np.nan')
        'ts'
        if ts_E[i] not in banned_list and ts_F[i] not in banned_list:
            E_ts.append(calc_energy(ts_E[i], suf_E[i], E_CH4, ts_F[i]))
        else:
            E_ts.append('np.nan')
        if tsra_E[i] not in banned_list and tsra_F[i] not in banned_list:
            E_tsra.append(calc_energy(tsra_E[i], suf_E[i], E_CH4, tsra_F[i]))
        else:
            E_tsra.append('np.nan')

    # set column index
    new_df = pd.DataFrame({'name': names, 'cell': cells, 'dop': dops, \
            'E_Hab2': E_Hab2, 'E_Hab3': E_Hab3, \
            'E_CH3ab': E_CH3ab, 'E_CH3ab2': E_CH3ab2, \
            'E_ts': E_ts, 'E_tsra': E_tsra})

    # set data by name, cell and dop
    new_df = new_df.sort_values(by=['name', 'cell', 'dop'], ascending=True)
    new_df = new_df.reset_index(drop=True)

    # get name and path, then save
    fE_csv_name = 'fE_data_' + time.strftime("%Y%m%d", time.localtime()) + '.csv'
    fE_csv = os.path.join(os.path.expanduser('~'), 'Desktop/CH4_DS/'+fE_csv_name)

    new_df.to_csv(fE_csv, columns=['name', 'cell', 'dop', \
            'E_Hab2', 'E_Hab3', 'E_CH3ab', 'E_CH3ab2', \
            'E_ts', 'E_tsra'])


if __name__ == '__main__':
    if len(sys.argv) == 3:
        # get file from arguments
        E_date = sys.argv[1]
        F_date = sys.argv[2]

        # get
        E_file = os.path.join(os.path.expanduser('~'), \
                'Desktop/CH4_DS/E_data_' + E_date + '.csv')
        F_file = os.path.join(os.path.expanduser('~'), \
                'Desktop/CH4_DS/Freq_data_' + F_date + '.csv')
        rE2fE(E_file, F_file)

        print('Successfully transfer absolute energy to reaction energy + ZPE.')
    else:
        print('rE2fE.py [Date of EnergyFile]')
