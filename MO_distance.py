#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: MO_distance.py
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
        for i in range(9,57):
            a_xyz = [] 
            for cor in content[i].strip('\n').split(' '):
                if cor not in ['','T','F']: 
                    a_xyz.append(float(cor)) ###
            xyz.append(a_xyz)
    xyz = np.array(xyz)
    abc = np.array(abc)
    ###
    M_xyz = xyz[32:48]
    M_xyz_sortbyz = M_xyz[M_xyz[:,2].argsort()]
    dop_M_xyz = M_xyz_sortbyz[-4:]
    #
    dop_M_xyz_sortbyx = dop_M_xyz[dop_M_xyz[:,0].argsort()]
    dop_s1_xyz = dop_M_xyz_sortbyx[2]
    dop_s2_xyz = dop_M_xyz_sortbyx[1]
    dop_s3_xyz = dop_M_xyz_sortbyx[3]
    ###
    O_xyz = xyz[0:32]
    O_xyz_sortbyz = O_xyz[O_xyz[:,2].argsort()]
    ab_O_xyz = O_xyz_sortbyz[-2:]
    ab_O_xyz_sortbyx = ab_O_xyz[ab_O_xyz[:,0].argsort()]
    #
    ab_O_b_xyz = ab_O_xyz_sortbyx[1]
    ####
    return abc, xyz, dop_s1_xyz, dop_s2_xyz, dop_s3_xyz, ab_O_b_xyz
###
def cal_MO_distance(CONTCAR):
    abc, xyz, s1, s2, s3, O = cell_information(CONTCAR)
    MO = O - s1
    MO_distance = np.linalg.norm((abc.T * MO).T)
    return MO_distance
###
def prepare_MO(finished_dirs):
    for finished_dir in finished_dirs:
        dir_name = finished_dir.split('/')[-1]
        suf_dir = os.path.join(finished_dir, 'suf')
        contcar = os.path.join(suf_dir, 'CONTCAR')
        MO_distance = cal_MO_distance(contcar)
        print(dir_name, MO_distance)
    
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
    finished_dirs = mW.check_printout(work_dir, 'suf')
    prepare_MO(finished_dirs)
###
if __name__ == '__main__':
    main()
