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
    ### e1, e2, e22, e3 1x3
    e1 = (s2_abO + s3_abO) / np.linalg.norm(s2_abO + s3_abO)
    e1 = e1.sum(0)
    e2 = abO_s1 / np.linalg.norm(abO_s1)
    e2 = e2.sum(0)
    e1dote2 = np.dot(e1, e2.T)
    ##
    y_e2 = np.sqrt(1.0**2*(1-np.cos(np.pi/2)**2)/(1-e1dote2**2))
    x_e1 = 1.0*np.cos(np.pi/2) - y_e2*e1dote2
    e22 = x_e1*e1 + y_e2*e2
    e22 = e22/np.linalg.norm(e22)
    ##
    e3 = np.dot(np.linalg.inv(np.vstack((np.vstack((e1, e22)) ,[1, 0, 0]))), \
            [0, 0, 1])
    e3 = e3.T/np.linalg.norm(e3)
    ### set abO as O , e1 as x e22 as y 
    #    H1
    #   /  \  H3 H4
    #  /    \ / /
    # O      C
    #  \     /\
    #   \---M  H2
    ## get M
    rad_e1Oe2 = np.arccos(np.dot(e1, e2.T))
    M_e1x = np.linalg.norm(abO_s1)*np.cos(rad_e1Oe2) 
    M_e22y = np.linalg.norm(abO_s1)*np.sin(rad_e1Oe2)
    ## get H1
    H1_e1x = np.sqrt(OH_distance**2/(1+np.tan(theta/180*np.pi)**2))
    H1_e22y = H1_e1x*np.tan(theta/180*np.pi)
    H1_XYZ = (abc.T*abO).T.sum(0) + H1_e1x*e1 + H1_e22y*e22
    ## get C
    ## set x = ay + b
    #  set uy^2 + vy + w = 0
    a = -(H1_e22y-M_e22y)/(H1_e1x-M_e1x)
    b = (H1C_distance**2-CM_distance**2-(H1_e1x**2-M_e1x**2)-(H1_e22y**2-M_e22y**2))/\
            (-2*(H1_e1x-M_e1x))
    u = a**2+1
    v = 2*a*b-2*a*H1_e1x-2*H1_e22y
    w = b**2-2*b*H1_e1x+H1_e1x**2+H1_e22y**2-OH_distance**2
    C_e22y = (-v+np.sqrt(v**2-4*u*w))/(2*u) # choose the bigger one
    C_e1x = a*C_e22y + b
    C_XYZ = (abc.T*abO).T.sum(0) + C_e1x*e1 + C_e22y*e22
    ## get H2, H3, H4
    H34_degree = 15
    H_proj = np.cos(H34_degree/180*np.pi)*e1 - np.sin(H34_degree/180*np.pi)*e22
    H_proj = H_proj/np.linalg.norm(H_proj) # set 15 degree bt e1
    H3_XYZ = 1.0*np.tan(109.5/2/180*np.pi)*e3 + H_proj
    H3_XYZ = C_XYZ + H3_XYZ/np.linalg.norm(H3_XYZ)*1.096
    H4_XYZ = - 1.0*np.tan(109.5/2/180*np.pi)*e3 + H_proj
    H4_XYZ = C_XYZ + H4_XYZ/np.linalg.norm(H4_XYZ)*1.096 
    ##
    H2_XYZ = 1.096*np.cos(((360-109.5)/2-H34_degree)/180*np.pi)*e1 + 1.096*np.sin(95.25/180*np.pi)*e22
    H2_XYZ = C_XYZ + H2_XYZ/np.linalg.norm(H2_XYZ)*1.096
    ###
    H1_xyz = (np.dot(np.linalg.inv(abc.T), H1_XYZ)).T
    H2_xyz = (np.dot(np.linalg.inv(abc.T), H2_XYZ)).T
    H3_xyz = (np.dot(np.linalg.inv(abc.T), H3_XYZ)).T
    H4_xyz = (np.dot(np.linalg.inv(abc.T), H4_XYZ)).T
    C_xyz = (np.dot(np.linalg.inv(abc.T), C_XYZ)).T
    return H1_xyz, H2_xyz, H3_xyz, H4_xyz, C_xyz
###
def create_fort188(dir, suf_dir, ts_dir):
    with open(os.path.join(ts_dir, 'fort.188'), 'w') as f:
        f.write('1\n3\n6\n4\n0.04\n1   5     1.4\n0') # 1.4 H1C_distance

###
def create_POSCAR(dir, suf_dir, ts_dir):
    CONTCAR = os.path.join(suf_dir, 'CONTCAR')
    H1_xyz, H2_xyz, H3_xyz, H4_xyz, C_xyz = cal_CH4_xyz(CONTCAR)
    content = []
    shutil.copyfile(os.path.join(suf_dir, 'CONTCAR'), os.path.join(ts_dir, 'POSCAR'))
    with open(os.path.join(ts_dir, 'POSCAR'), 'r') as f:
        content = f.readlines()
    new_content = ''
    for i in range(5):
        new_content += content[i]
    new_content += '{:>5}{:>5}'.format('H', 'C') + str(content[5])
    new_content += '{:>5}{:>5}'.format('4', '1') + str(content[6])
    for line in content[7:9]:
        new_content += line
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(H1_xyz[0], H1_xyz[1], H1_xyz[2])
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(H2_xyz[0], H2_xyz[1], H2_xyz[2])
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(H3_xyz[0], H3_xyz[1], H3_xyz[2])
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(H4_xyz[0], H4_xyz[1], H4_xyz[2])
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(C_xyz[0], C_xyz[1], C_xyz[2])
    for line in content[9:58]:
        new_content += line
    with open(os.path.join(ts_dir, 'POSCAR'), 'w') as f:
        f.write(new_content)
###
def prepare_ts(work_dir, finished_dirs):
    result_path = os.path.join(work_dir, 'prepare_ts_M.xu')
    if not os.path.exists(result_path):
        print('Start!')
    else:
        print('%s exists!' %(result_path))
        os.system(r'rm %s' %(result_path))
        print('%s is removed!' %(result_path))
    ###
    for dir in finished_dirs:
        suf_dir = os.path.join(dir, 'suf')
        ts_dir = os.path.join(dir, 'ts')
        if os.path.exists(ts_dir):
            print(ts_dir)
            if not os.path.exists(os.path.join(ts_dir, 'print-out')):
                shutil.rmtree(ts_dir)
                os.system(r'echo %s rming and making ts >> %s' %(ts_dir, result_path))
                os.mkdir(ts_dir)
                mC.create_VASPsp(dir, suf_dir, ts_dir)
                mC.create_INCAR(dir, suf_dir, ts_dir, '1')
                shutil.copyfile(os.path.join(suf_dir, 'KPOINTS'), os.path.join(ts_dir, 'KPOINTS'))
                create_POSCAR(dir, suf_dir, ts_dir)
                create_fort188(dir, suf_dir, ts_dir)
                mC.create_POTCAR(ts_dir, './data/potpaw_PBE.54')
        else:
            print(ts_dir)
            os.system(r'echo %s making ts >> %s' %(ts_dir, result_path))
            os.mkdir(ts_dir)
            mC.create_VASPsp(dir, suf_dir, ts_dir)
            mC.create_INCAR(dir, suf_dir, ts_dir, '1')
            shutil.copyfile(os.path.join(suf_dir, 'KPOINTS'), os.path.join(ts_dir, 'KPOINTS'))
            create_POSCAR(dir, suf_dir, ts_dir)
            create_fort188(dir, suf_dir, ts_dir)
            mC.create_POTCAR(ts_dir, './data/potpaw_PBE.54')

###
##
###
def main():
    if len(sys.argv) == 1:
        work_dir = r'./data/dopRutile'
        finished_dirs = mW.check_printout(work_dir, 'suf')
        print(finished_dirs)
        prepare_ts(work_dir, finished_dirs)       
    elif len(sys.argv) == 2:
        work_dir = sys.argv[1] 
        finished_dirs = mW.check_printout(work_dir, 'suf')
        prepare_ts(work_dir, finished_dirs)       
    elif len(sys.argv) == 3:
        work_dir = sys.argv[1]
        element = sys.argv[2]
        finished_dirs = []
        converg_dirs = mW.check_printout(work_dir, 'suf')
        for vasp_dir in converg_dirs:
            if re.match(r'.*' + element + r'O2_.*', vasp_dir):
                finished_dirs.append(vasp_dir)
        prepare_ts(work_dir, finished_dirs)       
    else:
        print('Wrong argvs!')
        sys.exit()
    ###
###
if __name__ == '__main__':
    main()
