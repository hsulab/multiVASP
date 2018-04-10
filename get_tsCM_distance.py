#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: get_tsCM_distance.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 四  3/29 16:41:51 2018
#########################################################################
import numpy as np
import os
import re
import shutil
import sys
###
import multiCAR as mC
import multiWalk as mW
###
def cell_information(CONTCAR):
    abc = []
    xyz = []
    with open(CONTCAR, 'r') as f:
        content = f.readlines()
        for i in range(2,5):
            a_abc = []
            for cor in content[i].strip('\n').split(' '):
                if cor not in ['']: 
                    a_abc.append(float(cor))
            abc.append(a_abc)
        for i in range(9,62):
            a_xyz = [] 
            for cor in content[i].strip('\n').split(' '):
                if cor not in ['','T','F']: 
                    a_xyz.append(float(cor)) ###
            xyz.append(a_xyz)
    xyz = np.array(xyz)
    abc = np.array(abc)
    ### make xyz between 0 and 1
    for i in range(len(xyz)):
        for j in range(len(xyz[i])):
            if xyz[i][j] >= float(0.9):
                xyz[i][j] -= 1
            elif xyz[i][j] < float(0):
                xyz[i][j] += 1
    ###
    M_xyz = xyz[37:53]
    M_xyz_sortbyz = M_xyz[M_xyz[:,2].argsort()]
    dop_M_xyz = M_xyz_sortbyz[-4:]
    #
    dop_M_xyz_sortbyx = dop_M_xyz[dop_M_xyz[:,0].argsort()]
    dop_s1_xyz = dop_M_xyz_sortbyx[2]
    dop_s2_xyz = dop_M_xyz_sortbyx[1]
    dop_s3_xyz = dop_M_xyz_sortbyx[3]
    ###
    O_xyz = xyz[5:37]
    O_xyz_sortbyz = O_xyz[O_xyz[:,2].argsort()]
    ab_O_xyz = O_xyz_sortbyz[-2:]
    ab_O_xyz_sortbyx = ab_O_xyz[ab_O_xyz[:,0].argsort()]
    #
    ab_O_b_xyz = ab_O_xyz_sortbyx[1]
    ####
    return abc, xyz, dop_s1_xyz, dop_s2_xyz, dop_s3_xyz, ab_O_b_xyz
###
def cal_CM_distance(CONTCAR):
    abc, xyz, s1, s2, s3, O = cell_information(CONTCAR)
    C_xyz = xyz[4]
    CM = s1 - C_xyz
    CM_distance = np.linalg.norm((abc.T*CM).T)
    return CM_distance
###
def multi_CM(converg_dirs):
    CM_content = ''
    CM_content += '{:<20}{:<20}'.format('dir_name', 'CM_distance WHEN ts')
    for converg_dir in converg_dirs:
        dir_name = os.path.basename(converg_dir)
        ts_dir = os.path.join(converg_dir, 'ts')
        ts_contcar = os.path.join(ts_dir, 'CONTCAR')
        CM_distance = cal_CM_distance(ts_contcar)
        CM_content += '\n{:<20}{:<20}'.format(dir_name, CM_distance)
    print(CM_content)
###
def main():
    work_dir = []
    if len(sys.argv) == 1:
        work_dir = r'./data/dopIrO2_2'
    elif len(sys.argv) == 2:
        work_dir = sys.argv[1]
        if not os.path.isdir(work_dir):
            sys.exit()
    ###
    finished_dirs = mW.check_printout(work_dir, 'ts')
    multi_CM(finished_dirs)
###
if __name__ == '__main__':
    main()
