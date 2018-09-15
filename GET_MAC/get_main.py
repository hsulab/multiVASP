#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: get_CH3ab_paras.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 9/10-2018
#########################################################################
import time
import os
import shutil
import string
import numpy as np
import pandas as pd
np.set_printoptions(suppress=True)
##
import pos2cif as p2c
import std_contcars as sc
import get_paras as gp
###
def main():
    ###
    group = 'CH3ab'
    para_type = 'da'
    ### local file
    cons_dir = '../data/'+group+'_data/CH3ab_cons'
    cifs_dir = '../data/'+group+'_data/CH3ab_cifs'
    ###
    MS_dir = os.path.join(os.path.expanduser('~'), 'Documents/USRP/DopRutile_Files/Documents')
    MS_cifs_dir = os.path.join(MS_dir, group+'_cifs')
    ###
    csv_name = group + '_data_' + time.strftime("%Y%m%d", time.localtime()) + '.csv'
    csv_path = os.path.join(os.path.expanduser('~'), 'Desktop/' + csv_name)
    ###
    ### pd.DataFrame
    row_index = 1
    group_df = pd.DataFrame()
    ###
    for con_name in os.listdir(cons_dir):
        print(con_name)
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
    print(group_df.shape[1])
    group_df.to_csv(csv_path)
###
if __name__ == '__main__':
    main()
