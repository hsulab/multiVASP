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
def cal_H_xyz(CONTCAR, theta= 109.5/2, distance = 1.0):
    abc, xyz, s1, s2, s3, abO = cell_information(CONTCAR)
    ###
    s2_abO = (abc.T*abO).T - (abc.T*s2).T 
    s3_abO = (abc.T*abO).T - (abc.T*s3).T
    abO_s1 = (abc.T*s1).T - (abc.T*abO).T 
    e1 = (s2_abO + s3_abO) / np.linalg.norm(s2_abO + s3_abO)
    e2 = abO_s1 / np.linalg.norm(abO_s1)
    e1dote2 = np.dot(e1.sum(0), e2.sum(0).T)
    ##
    cos_theta = np.cos(theta/180*np.pi)
    y_e2 = np.sqrt(distance**2*(1-cos_theta**2)/(1-e1dote2**2))
    x_e1 = distance*cos_theta - y_e2*e1dote2
    abO_H = x_e1*e1 + y_e2*e2
    H_XYZ = ((abc.T*abO).T + abO_H).sum(0)
    H_xyz = np.dot(np.linalg.inv(abc.T), H_XYZ.T).T
    return H_xyz

###
def create_POSCAR(dir, suf_dir, Hab_dir):
    CONTCAR = os.path.join(suf_dir, 'CONTCAR')
    H_xyz = cal_H_xyz(CONTCAR)
    content = []
    shutil.copyfile(os.path.join(suf_dir, 'CONTCAR'), os.path.join(Hab_dir, 'POSCAR'))
    with open(os.path.join(Hab_dir, 'POSCAR'), 'r') as f:
        content = f.readlines()
    new_content = ''
    for i in range(5):
        new_content += content[i]
    new_content += '{:>5}'.format('H') + str(content[5])
    new_content += '{:>5}'.format('1') + str(content[6])
    for line in content[7:9]:
        new_content += line
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(H_xyz[0], H_xyz[1], H_xyz[2])
    for line in content[9:58]:
        new_content += line
    with open(os.path.join(Hab_dir, 'POSCAR'), 'w') as f:
        f.write(new_content)
###
def prepare_ab(work_dir, finished_dirs):
    result_path = os.path.join(work_dir, 'prepare_Hab_sp3.xu')
    if not os.path.exists(result_path):
        print('Start!')
    else:
        print('%s exists!' %(result_path))
        os.system(r'rm %s' %(result_path))
        print('%s is removed!' %(result_path))
    ###
    for dir in finished_dirs:
        suf_dir = os.path.join(dir, 'suf')
        ab_dir = os.path.join(dir, 'Hab_sp3')
        if os.path.exists(ab_dir):
            if not os.path.exists(os.path.join(ab_dir, 'print-out')):
                shutil.rmtree(ab_dir)
                os.system(r'echo %s rming and making ab >> %s' %(ab_dir, result_path))
                os.mkdir(ab_dir)
                mC.create_VASPsp(dir, suf_dir, ab_dir)
                mC.create_INCAR(dir, suf_dir, ab_dir, '1')
                shutil.copyfile(os.path.join(suf_dir, 'KPOINTS'), os.path.join(ab_dir, 'KPOINTS'))
                create_POSCAR(dir, suf_dir, ab_dir)
                mC.create_POTCAR(ab_dir, './data/potpaw_PBE.54')
        else:
            os.system(r'echo %s making ab >> %s' %(ab_dir, result_path))
            os.mkdir(ab_dir)
            mC.create_VASPsp(dir, suf_dir, ab_dir)
            mC.create_INCAR(dir, suf_dir, ab_dir, '1')
            shutil.copyfile(os.path.join(suf_dir, 'KPOINTS'), os.path.join(ab_dir, 'KPOINTS'))
            create_POSCAR(dir, suf_dir, ab_dir)
            mC.create_POTCAR(ab_dir, './data/potpaw_PBE.54')

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
    prepare_ab(work_dir, finished_dirs)       
###
if __name__ == '__main__':
    main()
