#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: suf2ab.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 四  3/29 16:41:51 2018
#########################################################################
import numpy as np
import os
import re
import shutil
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
    dop_M_xyz = M_xyz_sortbyz[-3:]
    #
    dop_M_xyz_sortbyx = dop_M_xyz[dop_M_xyz[:,0].argsort()]
    dop_s1_xyz = dop_M_xyz_sortbyx[1]
    dop_s2_xyz = dop_M_xyz_sortbyx[0]
    dop_s3_xyz = dop_M_xyz_sortbyx[2]
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
def create_VASPsp(dir, suf_dir, Hab_dir):
    suf_VASPsp = os.path.join(suf_dir, 'vasp.script')
    Hab_VASPsp = os.path.join(Hab_dir, 'vasp.script')
    shutil.copyfile(suf_VASPsp, Hab_VASPsp)
    set_VASPsp(Hab_VASPsp, '#PBS -N', os.path.basename(dir) + '_Hab', 1)
###
def create_INCAR(dir, suf_dir, Hab_dir):
    suf_INCAR = os.path.join(suf_dir, 'INCAR')
    Hab_INCAR = os.path.join(Hab_dir, 'INCAR')
    shutil.copyfile(suf_INCAR, Hab_INCAR)
    set_INCAR(Hab_INCAR, 'SYSTEM', os.path.basename(dir) + '_Hab', 1)
    set_INCAR(Hab_INCAR, 'IBRION', '2', 1)
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
    H_xyz = np.dot(H_XYZ.T, np.linalg.inv(abc.T)).T
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
def create_POTCAR(Hab_dir, potdir= '/data/pot/vasp/potpaw_PBE.54'):
    POTCAR = ''
    element_pot_list = []
    with open(os.path.join(Hab_dir, 'POSCAR'), 'r') as f:
        elements = f.readlines()[5]
    elements = elements.strip('\n').split(' ')
    elements = [i for i in elements if not i == '']
    for element in elements:
        element_pot_new = '%s/%s_new/POTCAR' %(potdir, element)
        element_pot = '%s/%s/POTCAR' %(potdir, element)
        if os.path.exists(element_pot_new):
            element_pot_list.append(element_pot_new)
        elif os.path.exists(element_pot):
            element_pot_list.append(element_pot)
        else:
            print('Something wrong in %s: POTCAR.' %(Hab_dir))
            print('%s\n%s' %(element_pot_new, element_pot))
    for pot in element_pot_list:
        with open(pot, 'r') as f:
            pot_content = f.readlines()
        for line in pot_content:
            POTCAR += line
    with open(os.path.join(Hab_dir, 'POTCAR'), 'w') as f:
        f.write(POTCAR)
###
def main():
    ###
    dop_dir = './dopIrO2_2/dopIrO2_1_IrIrRu'
    suf_dir = os.path.join(dop_dir, 'suf')
    Hab_dir = os.path.join(dop_dir, 'Hab')
    os.mkdir(Hab_dir)
    ###
    create_POSCAR(dir, suf_dir, Hab_dir)
    ###
    element_order = dop_dir.split('_')[-1]
    element_order = re.findall(r'.{2}', element_order)
    print(element_order)
    ###
###
if __name__ == '__main__':
    main()
