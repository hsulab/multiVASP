#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: sufH2ab.py
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
def cal_CH3_xyz(CONTCAR, distance = 2.0):
    abc, xyz, s1, s2, s3, abO = cell_information(CONTCAR)
    ###
    C_xyz = np.array([0.5757753123041196, 0.3546416050953361, 0.5898707284108468])
    H_set_xyz = np.array([[0.5846828762668761, 0.1925734122114778, 0.6062930829869076],\
            [0.4275524324132437, 0.4273708074288867, 0.6043764087475084],\
            [0.7065416984266363, 0.4485714748568330, 0.6075371582613880]])
    ###
    O_xyz = xyz[0:32]
    O_xyz_sortbyz = O_xyz[O_xyz[:,2].argsort()]
    OuM_xyz_set = O_xyz_sortbyz[-10:-8] # O under M
    OuM_xyz_set_sortbyx = OuM_xyz_set[OuM_xyz_set[:,0].argsort()]
    #
    OuM_xyz = OuM_xyz_set_sortbyx[1]
    ###
    OuM_M = (abc.T*s1).T - (abc.T*OuM_xyz).T 
    OuM_M = OuM_M.sum(0)
    OuM_M = distance*OuM_M/ np.linalg.norm(OuM_M)
    ###
    s1_XYZ = (abc.T*s1).T.sum(0)
    new_C_XYZ = s1_XYZ + OuM_M
    ###
    new_H_set_xyz = []
    for H_xyz in H_set_xyz:
        CH = H_xyz - C_xyz
        H_XYZ = (abc.T*CH).T.sum(0) + new_C_XYZ
        H_xyz = np.dot(np.linalg.inv(abc.T), H_XYZ.T).T
        new_H_set_xyz.append(H_xyz)
    new_C_xyz = np.dot(np.linalg.inv(abc.T), new_C_XYZ.T).T
    return new_C_xyz, new_H_set_xyz


###
def create_POSCAR(dir, suf_dir, CH3ab_dir):
    CONTCAR = os.path.join(suf_dir, 'CONTCAR')
    C_xyz, H_set_xyz = cal_CH3_xyz(CONTCAR)
    content = []
    shutil.copyfile(os.path.join(suf_dir, 'CONTCAR'), os.path.join(CH3ab_dir, 'POSCAR'))
    with open(os.path.join(CH3ab_dir, 'POSCAR'), 'r') as f:
        content = f.readlines()
    new_content = ''
    for i in range(5):
        new_content += content[i]
    new_content += '{:>5}{:>5}'.format('H', 'C') + str(content[5])
    new_content += '{:>5}{:>5}'.format('3', '1') + str(content[6])
    for line in content[7:9]:
        new_content += line
    ###
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(H_set_xyz[0][0], H_set_xyz[0][1], H_set_xyz[0][2])
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(H_set_xyz[1][0], H_set_xyz[1][1], H_set_xyz[1][2])
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(H_set_xyz[2][0], H_set_xyz[2][1], H_set_xyz[2][2])
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(C_xyz[0], C_xyz[1], C_xyz[2])
    for line in content[9:58]:
        new_content += line
    with open(os.path.join(CH3ab_dir, 'POSCAR'), 'w') as f:
        f.write(new_content)
###
def prepare_CH3ab(work_dir, finished_dirs):
    result_path = os.path.join(work_dir, 'prepare_CH3ab.xu')
    if not os.path.exists(result_path):
        print('Start!')
    else:
        print('%s exists!' %(result_path))
        os.system(r'rm %s' %(result_path))
        print('%s is removed!' %(result_path))
    ###
    for dir in finished_dirs:
        suf_dir = os.path.join(dir, 'suf')
        CH3ab_dir = os.path.join(dir, 'CH3ab')
        if os.path.exists(CH3ab_dir):
            if not os.path.exists(os.path.join(CH3ab_dir, 'print-out')):
                shutil.rmtree(CH3ab_dir)
                os.system(r'echo %s rming and making ab >> %s' %(CH3ab_dir, result_path))
                os.mkdir(CH3ab_dir)
                mC.create_VASPsp(dir, suf_dir, CH3ab_dir)
                mC.create_INCAR(dir, suf_dir, CH3ab_dir, '2')
                shutil.copyfile(os.path.join(suf_dir, 'KPOINTS'), os.path.join(CH3ab_dir, 'KPOINTS'))
                create_POSCAR(dir, suf_dir, CH3ab_dir)
                mC.create_POTCAR(CH3ab_dir, './data/potpaw_PBE.54')
        else:
            os.system(r'echo %s making ab >> %s' %(CH3ab_dir, result_path))
            os.mkdir(CH3ab_dir)
            mC.create_VASPsp(dir, suf_dir, CH3ab_dir)
            mC.create_INCAR(dir, suf_dir, CH3ab_dir, '2')
            shutil.copyfile(os.path.join(suf_dir, 'KPOINTS'), os.path.join(CH3ab_dir, 'KPOINTS'))
            create_POSCAR(dir, suf_dir, CH3ab_dir)
            mC.create_POTCAR(CH3ab_dir, './data/potpaw_PBE.54')

###
##
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
    prepare_CH3ab(work_dir, finished_dirs)
###
if __name__ == '__main__':
    main()
