#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: collectdata.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 二  15/09/2018
#########################################################################
import os
import re
import time
###
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  
import numpy as np
import pandas as pd
### import sklearn
from sklearn import preprocessing
from sklearn.decomposition import PCA
###
class GeoData():
    'Geometry Features Data'
    def __init__(self, name):
        self.name = name

    'Path Settings'
    __dirpath = os.path.join(os.path.expanduser('~'), 'Desktop/CH4_DS')
    def get_path(self):
        self.__dirpath
    def set_path(self, path):
        self.__dirpath = path

    'Get Csv Name'
    def __csvname(self):
        ###
        for file_name in os.listdir(self.__dirpath):
            if re.match(self.name, file_name):
                csv_name = file_name
        return csv_name
    'Get df col=[name, feas]'
    def df(self, numbers=-1):
        csv = os.path.join(self.__dirpath, self.__csvname())
        df = pd.read_csv(csv, index_col=0)
        ###
        fea_numbers = len(df.columns) - 3
        #print(self.name+' has '+str(fea_numbers)+' features.')
        ###
        if numbers == -1:
            numbers = fea_numbers
        feas = []
        for i in range(3, numbers+3):
            feas.append(df.columns[i])
        return df.loc[:,tuple(['name']+feas)]
###
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

def get_data(geocomps):
    'Get Geo DataFrame'
    print('Load Data...')
    suf = GeoData('suf').df() # d 66 a 660
    hab3 = GeoData('Hab3').df() # d 78 a 858 all
    ch3ab = GeoData('CH3ab').df() # d 120 a 1680 all 1800

    'Merge geofeas'
    allgeo = pd.merge(suf, ch3ab, on='name')
    allgeo = pd.merge(allgeo, hab3, on='name')
    print('This set has ', allgeo.shape[0], 'samples.')
    print('This set has ', allgeo.shape[1]-1, 'features.')

    'Get numbers of geofeas'
    if geocomps <= allgeo.shape[1]-1:
        'Merge Data.'
        print('Merge Data...')
        geo = allgeo.iloc[:,range(1+geocomps)]
        ###
        E_feas = ['name', 'mtype', 'E_ts', 'E_tsra', 'mE', 'E_Hab3', 'E_CH3ab']
        fE = EneData('fE').allE().loc[:, E_feas] # reaction Energy
        e_numbers = fE.shape[1]
        ###
        di = pd.merge(fE, geo, on='name')
        new_di = di.loc[di.loc[:,'mtype']!='np.nan', :]
        new_di = new_di.loc[di.loc[:,'name']!='pureMoO2', :] # CH3ab wrong
        print('Mix set has ', new_di.shape[0], 'samples.')
        print('Mix set has ', new_di.shape[1]-5, 'features.')

        'Save data -> ./CH4_DataSet.csv'
        print('Save data -> ./CH4_DataSet.csv')
        new_di.to_csv('./CH4_DataSet.csv')
        return di # [name, mtype, mE, geo ... feas]
    else:
        print('Too many features!')

if __name__ == '__main__':
    'geoFeatures Total 6660'
    get_data(21642)
