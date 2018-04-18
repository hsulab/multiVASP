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
def cal_CH4_xyz(CONTCAR, theta= 109.5/2, \
        OH_distance = 1.4, H1C_distance = 1.4, CM_distance = 2.4):
    abc, xyz, s1, s2, s3, abO = cell_information(CONTCAR)
    ### calculate in D-coordinate 3x3
    s2_abO = (abc.T*abO).T - (abc.T*s2).T 
    s3_abO = (abc.T*abO).T - (abc.T*s3).T
    abO_s1 = (abc.T*s1).T - (abc.T*abO).T 
    ###
    e1 = (s2_abO + s3_abO) / np.linalg.norm(s2_abO + s3_abO)
    e2 = abO_s1 / np.linalg.norm(abO_s1)
    e1dote2 = np.dot(e1.sum(0), e2.sum(0).T)
    ##
    y_e2 = np.sqrt(1.0**2/(1-e1dote2**2))
    x_e1 = -y_e2*e1dote2
    e22 = x_e1*e1 + y_e2*e2
    ### set abO as O , e1 as x e22 as y 
    ## get M
    rad_e1Oe2 = np.arccos(np.dot(e1.sum(0), e2.sum(0).T))
    M_e1x = np.sqrt(np.linalg.norm(abO_s1)**2/(1+np.tan(rad_e1Oe2)**2))
    M_e22y = M_e1x*np.tan(rad_e1Oe2)
    ## get H1
    H1_e1x = np.sqrt(OH_distance**2/(1+np.tan(theta/180*np.pi)**2))
    H1_e22y = H1_e1x*np.tan(theta/180*np.pi)
    H1_XYZ = (abc.T*abO).T - H1_e1x*e1 + H1_e22y*e22
    ## get C
    ## set x = ay + b
    #  set uy^2 + vy + w = 0
    a = -(H1_e22y-M_e22y)/(H1_e1x-M_e1x)
    b = (OH_distance**2-np.linalg.norm(abO_s1)**2-(H1_e1x**2-M_e1x**2)-(H1_e22y**2-M_e22y**2))/\
            (-2*(H1_e1x-M_e1x))
    u = a**2+1
    v = 2*a*b-2*a*H1_e1x-2*H1_e22y
    w = b**2-2*b*H1_e1x+H1_e1x**2+H1_e22y**2-OH_distance**2
    M_e1x = (-v+np.sqrt(v**2-4*u*w))/(2*u)
    ##
    ###

###
def create_POSCAR(dir, suf_dir, Hab_dir):
    CONTCAR = os.path.join(suf_dir, 'CONTCAR')
    H_xyz = cal_CH4_xyz(CONTCAR)
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
    result_path = os.path.join(work_dir, 'prepare_Hab_sp2.xu')
    if not os.path.exists(result_path):
        print('Start!')
    else:
        print('%s exists!' %(result_path))
        os.system(r'rm %s' %(result_path))
        print('%s is removed!' %(result_path))
    ###
    for dir in finished_dirs:
        suf_dir = os.path.join(dir, 'suf')
        ab_dir = os.path.join(dir, 'Hab_sp2')
        if os.path.exists(ab_dir):
            if not os.path.exists(os.path.join(ab_dir, 'print-out')):
                shutil.rmtree(ab_dir)
                os.system(r'echo %s rming and making ab >> %s' %(ab_dir, result_path))
                os.mkdir(ab_dir)
                mC.create_VASPsp(dir, suf_dir, ab_dir)
                mC.create_INCAR(dir, suf_dir, ab_dir, '2')
                shutil.copyfile(os.path.join(suf_dir, 'KPOINTS'), os.path.join(ab_dir, 'KPOINTS'))
                create_POSCAR(dir, suf_dir, ab_dir)
                mC.create_POTCAR(ab_dir, './data/potpaw_PBE.54')
        else:
            os.system(r'echo %s making ab >> %s' %(ab_dir, result_path))
            os.mkdir(ab_dir)
            mC.create_VASPsp(dir, suf_dir, ab_dir)
            mC.create_INCAR(dir, suf_dir, ab_dir, '2')
            shutil.copyfile(os.path.join(suf_dir, 'KPOINTS'), os.path.join(ab_dir, 'KPOINTS'))
            create_POSCAR(dir, suf_dir, ab_dir)
            mC.create_POTCAR(ab_dir, './data/potpaw_PBE.54')

###
##
###
def main():
    work_dir = []
    if len(sys.argv) == 1:
        work_dir = r'./data/dopRutile'
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
