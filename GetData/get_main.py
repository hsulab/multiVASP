#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: get_CH3ab_paras.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 9/10-2018
#########################################################################
### python system
import time
import os
import re
import sys
import shutil
import string
### python scilibs
import numpy as np
import pandas as pd
np.set_printoptions(suppress=True)
### cigars' lib
import pos2cif as p2c
import std_contcars as sc
import get_paras as gp
###
def get_csv(group, para_type):
    ### group = 'CH3ab' para_type = 'da'
    ### local file
    cons_dir = '../data/'+group+'_data/' + group + '_cons'
    cifs_dir = '../data/'+group+'_data/' + group + '_cifs'
    ### MS file
    MS_dir = os.path.join(os.path.expanduser('~'), 'Documents/USRP/DopRutile_Files/Documents')
    MS_cifs_dir = os.path.join(MS_dir, group+'_cifs')
    ### csv file
    csv_name = group + '_data_' + time.strftime("%Y%m%d", time.localtime()) + '.csv'
    csv_path = os.path.join(os.path.expanduser('~'), 'Desktop/' + csv_name)
    ### pd.DataFrame
    row_index = 1
    group_df = pd.DataFrame()
    ###
    for file_name in os.listdir(cons_dir):
        f = os.path.join(cons_dir, file_name)
        if re.match(r'.*.cif', file_name):
            os.remove(f)
    for con_name in os.listdir(cons_dir):
        if row_index % 4 == 0:
            print('{:<5}{:^5}{:<30}{:^3}'.format(row_index, ' --> ', con_name, ' | '))
        else:
            print('{:<5}{:^5}{:<30}{:^3}'.format(row_index, ' --> ', con_name, ' | '), end='')
        ###
        con = os.path.join(cons_dir, con_name)
        abc, elements, numbers, xyzs, l1, l2, group_dict = sc.std_contcars(con, group)
        ##
        cif_name = os.path.basename(con) + '.cif'
        p2c.write_cif(con+'.cif', abc, elements, numbers, xyzs)
        ##
        total_paras = gp.get_paras(abc, l1, l2, group, group_dict, cif_name, para_type)
        ###
        if row_index == 1:
            group_df = pd.DataFrame(columns=tuple(total_paras.keys()))
        group_df.loc[row_index] = list(total_paras.values())
        row_index += 1
        ###
        cif = os.path.join(cifs_dir, cif_name)
        ###
        ms_xsd = os.path.join(MS_cifs_dir, os.path.basename(con)+'.xsd')
        if not os.path.exists(ms_xsd):
            ms_cif = os.path.join(MS_cifs_dir, cif_name)
            shutil.copy(con+'.cif', cif)
            shutil.move(con+'.cif', ms_cif)
        else:
            os.remove(con+'.cif')
    ###
    group_df = group_df.sort_values(by=['cell', 'name', 'dop'], ascending=True)
    group_df = group_df.reset_index(drop=True)
    print('\n', group_df.shape[1], '\n')
    group_df.to_csv(csv_path)
###
def main():
    if len(sys.argv) == 1:
        print('get geometry features\nget_main.py [group] [paras]')
    elif len(sys.argv) == 2:
        group = str(sys.argv[1]) 
        get_csv(group, 'dah')
    elif len(sys.argv) == 3:
        group = str(sys.argv[1])
        paras = str(sys.argv[2])
        get_csv(group, paras)
    else:
        print('Wrong argvs!')
        sys.exit()

###
if __name__ == '__main__':
    main()
