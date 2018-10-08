#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: reg_main.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
import time
### plot
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  
### scilibs
import numpy as np
import pandas as pd
'sklearn'
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import KFold
### mylibs
import decorates as deco
###
def pre_yx():
    'Get Total DataSet'
    df = pd.read_csv('./CH4_DataSet.csv', index_col = 0)
    feas_E = ['E_ts', 'E_tsra', 'E_Hab2','E_Hab3','E_CH3ab']
    'Get index and values'
    yx_indexs = df.iloc[:,range(2)] # 'name' and 'mtype'
    'Get DataSet'
    DS = {}
    DS['name'] = yx_indexs.iloc[:,range(1)].values
    DS['mtype'] = yx_indexs.iloc[:,range(1,2)].values
    DS['E_ts'] = df.loc[:,'E_ts'].values # mE
    DS['E_tsra'] = df.loc[:,'E_tsra'].values # mE
    DS['E_Hab2'] = df.loc[:,'E_Hab2'].values
    DS['E_Hab3'] = df.loc[:,'E_Hab3'].values
    DS['E_CH3ab'] = df.loc[:,'E_CH3ab'].values
    'Check Hab2 Hab3'
    def check_Had_energy(names=DS['name'], E_H_2=DS['E_Hab2'], \
            E_H_3=DS['E_Hab3']):
        count = 0
        for H2, H3 in zip(E_H_2, E_H_3):
            name = names[count]
            if H2 < H3:
                print(H2, H3, name)
            count += 1
    'ts Ea-Hab2+CH3ab Ea-Hab3+CH3ab tsra Ea-Hab2 Ea-Hab3'
    def get_ds(mtype, adtype):
        ds = {}; ds['Ea'] = []; ds['ad'] = [];
        for m, E_ts, E_tsra, H_2, H_3, CH3 in zip(DS['mtype'], \
                DS['E_ts'], DS['E_tsra'], DS['E_Hab2'], DS['E_Hab3'], DS['E_CH3ab']):
            if mtype == 'ts':
                if E_ts != 'np.nan':
                    ds['Ea'].append(float(E_ts))
                    if adtype == 2:
                        ds['ad'].append(H_2+CH3)
                    elif adtype == 3:
                        ds['ad'].append(H_3+CH3)
            elif mtype == 'tsra':
                if E_tsra != 'np.nan':
                    ds['Ea'].append(float(E_tsra))
                    if adtype == 2:
                        ds['ad'].append(H_2+CH3)
                    elif adtype == 3:
                        ds['ad'].append(H_3+CH3)
        return ds
    ts1 = get_ds('ts', 2)
    ts2 = get_ds('ts', 3)
    tsra1 = get_ds('tsra', 2)
    tsra2 = get_ds('tsra', 3)
    return ts1, ts2, tsra1, tsra2
###
def cv_yx(y, n):
    kf = KFold(n_splits=n)
    groups_index = []
    for train_index, test_index in kf.split(y):
        groups_index.append([train_index, test_index])
    return groups_index
###
logtime = time.strftime("%Y%m%d")
def reg_yx():
    'Pre and Scaler Data'
    ts1, ts2, tsra1, tsra2 = pre_yx()
    ds = {}
    ds['ts1'] = ts1; ds['ts2'] = ts2;
    ds['tsra1'] = tsra1; ds['tsra2'] = tsra2;
    'ts Ea-Hab2+CH3ab Ea-Hab3+CH3ab tsra Ea-Hab2 Ea-Hab3'
    notes = {}
    notes['ts1'] = 'CH3+H_2'; notes['ts2'] = 'CH3+H_3'
    notes['tsra1'] = 'H_2'; notes['tsra2'] = 'H_3'
    def regs(ds, note):
        content = 'Reg Type: ' + note
        'Get DataSet'
        y = np.array(ds[note]['Ea'])
        X = np.array(ds[note]['ad']).reshape(-1,1)
        content += 'Sample Points: ' + str(len(y)) + '\n'
        'Linear Regression'
        model = LinearRegression()
        model.fit(X, y)
        'Coef and Feas'
        coefs = round(model.coef_[0], 4)
        inter = round(model.intercept_)
        content += 'mE = ' + str(coefs) + ' x ' +str(notes[note]) + ' + ' + str(inter) + '\n'
        y_p = model.predict(X)
        content += "_R2:" + str(metrics.explained_variance_score(y, y_p)) + ' '*5
        content += "MSE:" + str(metrics.mean_squared_error(y, y_p)) + '\n'
        return content, y, y_p
    reg_log = ''
    for note in notes.keys():
        'Reg and Log'
        content, y, y_p = regs(ds, note)
        reg_log += content
        'Plt'
        plt_yx(notes[note], y, y_p)
    with open('./Logs/reg/reg_'+logtime+'.txt', 'w') as f:
        f.write(reg_log)
###
def plt_yx(note, y, y_p):
    'plt'
    fig, ax = plt.subplots()
    ax.scatter(y, y_p, edgecolors=(0, 0, 0))
    ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    ax.set_title('Ea v.s. E_('+note+')')
    plt.savefig('./Logs/reg/'+note+'.png', bbox='tight')
###
if __name__ == '__main__':
    'total feastures 8454'
    reg_yx()
