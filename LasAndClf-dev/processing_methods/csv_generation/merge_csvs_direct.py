#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
import re
import time

import numpy as np
import pandas as pd

"""
"""


# ===== ===== ===== ===== ===== ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== ===== ===== ===== ===== =====
def get_dataframe_from_csv(name):
    # get csvname in dir
    dirpath = os.path.join(os.path.expanduser('~'), 'Desktop/CH4_DS')
    for file_name in os.listdir(dirpath):
        if re.match(name, file_name):
            csv_name = file_name

    # turn csvfile into dataframe
    csv = os.path.join(dirpath, csv_name)
    df = pd.read_csv(csv, index_col=0)

    fea_numbers = len(df.columns) - 3
    #print(self.name+' has '+str(fea_numbers)+' features.')

    feas = []
    for i in range(3, fea_numbers+3):
        feas.append(df.columns[i])

    return df.loc[:,tuple(['name']+feas)]


def add_preferred_energy_and_type(df):
    mtype = [] # mechanism type
    mE = []
    for i in range(df.shape[0]):
        if df.loc[i, 'E_ts'] == 'np.nan' and df.loc[i, 'E_tsra'] == 'np.nan':
            mtype.append('np.nan')
            mE.append('np.nan')
        elif df.loc[i, 'E_ts'] == 'np.nan' and df.loc[i, 'E_tsra'] != 'np.nan':
            mtype.append('tsra')
            mE.append(df.loc[i, 'E_tsra'])
        elif df.loc[i, 'E_ts'] != 'np.nan' and df.loc[i, 'E_tsra'] == 'np.nan':
            mtype.append('ts')
            mE.append(df.loc[i, 'E_ts'])
        elif df.loc[i, 'E_ts'] > df.loc[i, 'E_tsra']:
            mtype.append('tsra')
            mE.append(df.loc[i, 'E_tsra'])
        else:
            mtype.append('ts')
            mE.append(df.loc[i, 'E_ts'])
    df.loc[:, 'mtype'] = mtype
    df.loc[:, 'mE'] = mE
    return df


# ===== ===== ===== ===== ===== ===== ===== ===== ===== =====
# merge geometric features csv and energy csv into one 
# ===== ===== ===== ===== ===== ===== ===== ===== ===== =====
def merge_csv():
    """
    Description:
        Merge geometric features of different adsorption structure 
        into one csv file. descriptors: distance 45, angles 360, dihedrals 630.
    """
    # calculate number of descriptors
    natoms = 4
    ndistances = natoms * (natoms-1) / 2
    nangles = natoms * (natoms-1) * (natoms-2) / 2
    ndihedrals = natoms * (natoms-1) / 2 * (natoms-2) * (natoms-3) / 8
    ngfeatures = ndistances + nangles + ndihedrals # number of geometric features 

    print('%d atoms generate %d distances, %d angles, %d dihedrals, %d total' \
            %(natoms, ndistances, nangles, ndihedrals, ngfeatures))

    # load csv files
    print('Load suf, hab3, ch3ab data from csv files...')
    suf = get_dataframe_from_csv('suf')
    hab3 = get_dataframe_from_csv('Hab3')
    ch3ab = get_dataframe_from_csv('CH3ab')

    # calculate the difference between suf and adsorbed state
    name_df = pd.DataFrame()
    name_df.loc[:, 'name'] = suf.loc[:, 'name']

    name_suf = pd.merge(name_df, suf, on='name') # if included suf 
    name_hab3 = pd.merge(name_suf, hab3, on='name')
    name_hab3_ch3ab = pd.merge(name_hab3, ch3ab, on='name')
    #print(name_hab3_ch3ab)

    # Merge geofeas
    print('This set has ', name_hab3_ch3ab.shape[0], 'samples.')
    print('This set has ', name_hab3_ch3ab.shape[1]-1, 'features.')

    # Get numbers of geofeas
    print('Merge geometric features CSV with energy CSV ...')
    E_feas = ['name', 'mtype', 'E_ts', 'E_tsra', 'mE', 'E_Hab3', 'E_CH3ab']
    fE = add_preferred_energy_and_type(get_dataframe_from_csv('fE')).loc[:, E_feas] # reaction Energy
    
    di = pd.merge(fE, name_hab3_ch3ab, on='name')
    new_di = di.loc[di.loc[:, 'mtype'] != 'np.nan', :]

    # ===== ===== ===== ===== ===== ===== ===== ===== ===== =====
    # remove data with some problems
    # new_di = new_di.loc[di.loc[:,'name']!='pureMoO2', :] # CH3ab freq wrong
    # new_di = new_di.loc[di.loc[:,'name']!='pureMnO2', :] # tsra freq wrong
    new_di = new_di.loc[di.loc[:,'name']!='dopCrO2_Ru', :] # CH3ab freq wrong
    # ===== ===== ===== ===== ===== ===== ===== ===== ===== =====

    print('Energy and Geometry set has ', new_di.shape[0], 'samples.')
    print('Energy and Geometry set has ', new_di.shape[1]-5, 'features.')
    
    # Save data -> ./CH4_DataSet.csv
    merged_data_csv = './CH4_neo.csv'
    print('Save data -> %s' %merged_data_csv)
    new_di.to_csv(merged_data_csv)
    return new_di # [name, mtype, mE, geo ... feas]


if __name__ == '__main__':
    merge_csv()
