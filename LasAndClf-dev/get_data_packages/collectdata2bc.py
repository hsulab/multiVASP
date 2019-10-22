#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
import re
import time

import numpy as np
import pandas as pd

"""
"""


class GeoData():
    # Geometry Features Data
    def __init__(self, name):
        self.name = name

    # Path Settings
    __dirpath = os.path.join(os.path.expanduser('~'), 'Desktop/CH4_DS')
    def set_path(self, path):
        """Set data path."""
        self.__dirpath = path

    def get_path(self):
        """Get data path."""
        self.__dirpath

    # Get Csv Name
    def __csvname(self):
        """Get data csvfile."""
        for file_name in os.listdir(self.__dirpath):
            if re.match(self.name, file_name):
                csv_name = file_name
        return csv_name
    
    # Get df col=[name, feas]
    def df(self, numbers=-1):
        """Get dataframe."""
        csv = os.path.join(self.__dirpath, self.__csvname())
        df = pd.read_csv(csv, index_col=0)

        fea_numbers = len(df.columns) - 3
        #print(self.name+' has '+str(fea_numbers)+' features.')

        if numbers == -1:
            numbers = fea_numbers
        feas = []
        for i in range(3, numbers+3):
            feas.append(df.columns[i])

        return df.loc[:,tuple(['name']+feas)]


class EneData(GeoData):
    'Energy Data'
    def allE(self):
        df = self.df()
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

def get_data():
    """
    Description:
        Get Geo DataFrame.
        descriptors: distance 45, angles 360, dihedrals 630.
    """
    print('Load Data...')
    suf = GeoData('suf').df()
    hab3 = GeoData('Hab3').df()
    ch3ab = GeoData('CH3ab').df() 

    #
    delta_df = pd.DataFrame()
    delta_df.loc[:, 'name'] = suf.loc[:, 'name']
    cols = suf.columns[1:]

    for col in cols:
        t = col.strip('suf')
        delta_df.loc[:, t+'hab3'] = hab3.loc[:, t+'Hab3'] - suf.loc[:, t+'suf']

    for col in cols:
        t = col.strip('suf')
        delta_df.loc[:, t+'ch3ab'] = ch3ab.loc[:, t+'CH3ab'] - suf.loc[:, t+'suf']

    'Merge geofeas'
    print('This set has ', delta_df.shape[0], 'samples.')
    print('This set has ', delta_df.shape[1]-1, 'features.')

    'Get numbers of geofeas'
    print('Merge Data...')
    E_feas = ['name', 'mtype', 'E_ts', 'E_tsra', 'mE', 'E_Hab3', 'E_CH3ab']
    fE = EneData('fE').allE().loc[:, E_feas] # reaction Energy
    e_numbers = fE.shape[1]
    
    di = pd.merge(fE, delta_df, on='name')
    new_di = di.loc[di.loc[:,'mtype']!='np.nan', :]
    # !!!
    new_di = new_di.loc[di.loc[:,'name']!='pureMoO2', :] # CH3ab wrong
    new_di = new_di.loc[di.loc[:,'name']!='pureMnO2', :] # CH3ab wrong
    new_di = new_di.loc[di.loc[:,'name']!='dopCrO2_Ru', :] # CH3ab wrong

    print('Energy and Geometry set has ', new_di.shape[0], 'samples.')
    print('Energy and Geometry set has ', new_di.shape[1]-5, 'features.')
    
    # Save data -> ./CH4_DataSet.csv
    merged_data_csv = './CH4_neo.csv'
    print('Save data -> %s' %merged_data_csv)
    new_di.to_csv(merged_data_csv)
    return new_di # [name, mtype, mE, geo ... feas]


if __name__ == '__main__':
    'geoFeatures Total 1035'
    get_data()
