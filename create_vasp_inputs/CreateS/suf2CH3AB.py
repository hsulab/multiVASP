#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: suf2CH3ab_M.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 四  3/29 16:41:51 2018
#########################################################################
import numpy as np
import os
import re
import shutil
import sys

import CreateCars
import CheckOut

def cal_CH3_xyz(CONTCAR, CH3_type, theta= 109.5/2,  CM_distance = 2.2):
    'Get lattice constant and atom coordinates.'
    abc, xyz, s1, s2, s3, abO = CreateCars.cell_info(CONTCAR)

    # calculate in D-coordinate 3x3
    s2_abO = (abc.T*abO).T - (abc.T*s2).T 
    s3_abO = (abc.T*abO).T - (abc.T*s3).T
    abO_s1 = (abc.T*s1).T - (abc.T*abO).T 

    'Set inner absicca'
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

    # get M
    rad_e1Oe2 = np.arccos(np.dot(e1, e2.T))
    M_e1x = np.linalg.norm(abO_s1)*np.cos(rad_e1Oe2) 
    M_e22y = np.linalg.norm(abO_s1)*np.sin(rad_e1Oe2)
    M_XYZ = (abc.T*s1).T.sum(0)

    # get C
    C_e1x = CM_distance 
    C_XYZ = M_XYZ + C_e1x*e1

    def calc_H_XYZs(CH3_type):
        if CH3_type == 'CH3ab':
            ### set abO as O , e1 as x e22 as y 
            #     H1  H3 H4
            #      \ / /
            # O     C
            #  \    |
            #   \---M  
            ###

            ## get H1
            H1_e1x = 1.096*np.cos((180-109.5)/180*np.pi)
            H1_e22y = -1.096*np.sin((180-109.5)/180*np.pi)
            H1_XYZ = C_XYZ + H1_e1x*e1 + H1_e22y*e22
            ## get H3, H4
            H_proj_rad = ((360-109.5)/2-(180-109.5))/180*np.pi 
            H_proj = np.cos(H_proj_rad)*e1 + np.sin(H_proj_rad)*e22
            H_proj = H_proj/np.linalg.norm(H_proj) # set 15 degree bt e1
            H3_XYZ = 1.0*np.tan(109.5/2/180*np.pi)*e3 + H_proj
            H3_XYZ = C_XYZ + H3_XYZ/np.linalg.norm(H3_XYZ)*1.096
            H4_XYZ = - 1.0*np.tan(109.5/2/180*np.pi)*e3 + H_proj
            H4_XYZ = C_XYZ + H4_XYZ/np.linalg.norm(H4_XYZ)*1.096 

        elif CH3_type == 'CH3ab2':
            ###
            #      H1
            #      |
            # O----C
            #    /   \
            #   H3   H4
            ###

            ## get H1
            H1_e1x = 1.096*np.cos((180-109.5)/180*np.pi)
            H1_e3z = 1.096*np.sin((180-109.5)/180*np.pi)
            H1_XYZ = C_XYZ + H1_e1x*e1 + 0*e22 + H1_e3z*e3
            ## get H3, H4
            H3_e1x = H1_e1x
            H3_e22y = -H1_e3z*np.cos((30.0/180.0)*np.pi)
            H3_e3z = -H1_e3z*np.sin((30.0/180.0)*np.pi)
            H3_XYZ = C_XYZ + H3_e1x*e1 + H3_e22y*e22 + H3_e3z*e3
            #
            H4_e1x = H1_e1x
            H4_e22y = H1_e3z*np.cos((30.0/180.0)*np.pi)
            H4_e3z = -H1_e3z*np.sin((30.0/180.0)*np.pi)
            H4_XYZ = C_XYZ + H4_e1x*e1 + H4_e22y*e22 + H4_e3z*e3
            ###
        else:
            print('Wrong CH3 type.')

        return H1_XYZ, H3_XYZ, H4_XYZ

    H1_XYZ, H3_XYZ, H4_XYZ = calc_H_XYZs(CH3_type)
    H1_xyz = (np.dot(np.linalg.inv(abc.T), H1_XYZ)).T
    H3_xyz = (np.dot(np.linalg.inv(abc.T), H3_XYZ)).T
    H4_xyz = (np.dot(np.linalg.inv(abc.T), H4_XYZ)).T
    C_xyz = (np.dot(np.linalg.inv(abc.T), C_XYZ)).T

    return H1_xyz, H3_xyz, H4_xyz, C_xyz

def create_POSCAR(dir, suf_dir, CH3ab_dir, CH3_type):
    CONTCAR = os.path.join(suf_dir, 'CONTCAR')
    H1_xyz, H3_xyz, H4_xyz, C_xyz = cal_CH3_xyz(CONTCAR, CH3_type)
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
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(H1_xyz[0], H1_xyz[1], H1_xyz[2])
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(H3_xyz[0], H3_xyz[1], H3_xyz[2])
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(H4_xyz[0], H4_xyz[1], H4_xyz[2])
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(C_xyz[0], C_xyz[1], C_xyz[2])
    for line in content[9:58]:
        new_content += line
    with open(os.path.join(CH3ab_dir, 'POSCAR'), 'w') as f:
        f.write(new_content)

def prepare_CH3ab2(finished_dirs, CH3_type):
    ###
    for root_dir in finished_dirs:
        ''
        suf_dir = os.path.join(root_dir, 'suf')
        CH3ab2_dir = os.path.join(root_dir, CH3_type)

        ''
        if os.path.exists(CH3ab2_dir):
            if not os.path.exists(os.path.join(CH3ab2_dir, 'print-out')):
                print(CH3ab2_dir + '--> Remove and Create...')
                shutil.rmtree(CH3ab2_dir)
                os.mkdir(CH3ab2_dir)
                CreateCars.create_VASPsp(root_dir, suf_dir, CH3ab2_dir)
                CreateCars.create_INCAR(root_dir, suf_dir, CH3ab2_dir, 2)
                shutil.copyfile(os.path.join(suf_dir, 'KPOINTS'), os.path.join(CH3ab2_dir, 'KPOINTS'))
                create_POSCAR(root_dir, suf_dir, CH3ab2_dir, CH3_type)
                CreateCars.create_POTCAR(CH3ab2_dir)
            else:
                print(CH3ab2_dir + '--> already done.')
        else:
            print(CH3ab2_dir + '--> Create...')
            os.mkdir(CH3ab2_dir)
            CreateCars.create_VASPsp(root_dir, suf_dir, CH3ab2_dir)
            CreateCars.create_INCAR(root_dir, suf_dir, CH3ab2_dir, 2)
            shutil.copyfile(os.path.join(suf_dir, 'KPOINTS'), os.path.join(CH3ab2_dir, 'KPOINTS'))
            create_POSCAR(root_dir, suf_dir, CH3ab2_dir, CH3_type)
            CreateCars.create_POTCAR(CH3ab2_dir)

def main():
    if len(sys.argv) == 1:
        work_dir = r'./TestDir/'
        if os.path.exists(work_dir):
            finished_dirs = CheckOut.check_printout(work_dir, 'suf')
            print('Finished Dirs: ', finished_dirs)
            prepare_CH3ab2(finished_dirs)       
        else:
            print('Test Only.')
    elif len(sys.argv) == 4:
        'Get argvs'
        work_dir = sys.argv[1]
        CH3_type = sys.argv[2]
        element = sys.argv[3]

        ''
        finished_dirs = []
        converg_dirs = CheckOut.check_printout(work_dir, 'suf')
        for vasp_dir in converg_dirs:
            if re.match(r'.*' + element + r'O2_.*', os.path.basename(vasp_dir)) or \
                re.match(r'pure'+ element + r'O2', os.path.basename(vasp_dir)):
                    finished_dirs.append(vasp_dir)

        prepare_CH3AB(finished_dirs, CH3_type)
    else:
        print('suf2CH3AB.py [Dir] [CH3-type] [Metal]')
        sys.exit()

if __name__ == '__main__':
    main()
