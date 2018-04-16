#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: dopRutile.py
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
import multiSet as mS
import multiCAR as mC
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
    top_M_xyz = M_xyz_sortbyz[-4:]
    #
    top_M_xyz_sortbyx = top_M_xyz[top_M_xyz[:,0].argsort()]
    top_s1_xyz = top_M_xyz_sortbyx[2]
    for i in range(len(xyz)):
        if list(top_s1_xyz) == list(xyz[i]):
            top_s1_index = i
            break
    #
    #### xyz is the frac_xyz under abc
    return abc, xyz, top_s1_xyz, top_s1_index
###
def change_POSCAR(POSCAR, base_element, dop_element):
    abc, xyz, s1_xyz, s1_index = cell_information(POSCAR)
    with open(POSCAR, 'r') as f:
        content = f.readlines()
    new_content = ''
    for i in range(5):
        new_content += content[i]
    new_content += '{:>5}{:>5}{:>5}\n'.format('O', base_element, dop_element)
    new_content += '{:>5}{:>5}{:>5}\n'.format('32', '15', '1')
    for i in range(7,9):
        new_content += content[i]
    for i in range(9, 57):
        if i != s1_index+9:
            new_content += content[i]
    new_content += '    {:<18}{:<18}{:<18} T   T   T\n'.format(s1_xyz[0], s1_xyz[1], s1_xyz[2])
    with open(POSCAR, 'w') as f:
        f.write(new_content)
###
def make_dopdirs(work_dir):
    numbers=['22', '23', '32', '42', '44', '45', '76', '77', '82']
    elements=['Ti','V', 'Ge', 'Mo', 'Ru', 'Rh', 'Os', 'Ir', 'Pb']
    for base_element in elements:
        suf_dir = os.path.join(work_dir, base_element+'O2')
        contcar = os.path.join(suf_dir, 'CONTCAR')
        for dop_element in elements:
            dop_dirname = 'dop' + base_element + 'O2' + '_' + dop_element
            dop_dir = os.path.join(work_dir, dop_dirname)
            dopsuf_dir = os.path.join(dop_dir, 'suf')
            if not os.path.exists(dopsuf_dir):
                os.mkdir(dop_dir)
                os.mkdir(dopsuf_dir)
            shutil.copyfile(os.path.join(suf_dir, 'INCAR'), os.path.join(dopsuf_dir, 'INCAR'))
            mS.set_INCAR(os.path.join(dopsuf_dir, 'INCAR'), 'SYSTEM', dop_dirname+'_suf', 1)
            shutil.copyfile(os.path.join(suf_dir, 'POSCAR'), os.path.join(dopsuf_dir, 'POSCAR'))
            change_POSCAR(os.path.join(dopsuf_dir, 'POSCAR'), base_element, dop_element)
            shutil.copyfile(os.path.join(suf_dir, 'KPOINTS'), os.path.join(dopsuf_dir, 'KPOINTS'))
            shutil.copyfile(os.path.join(suf_dir, 'vasp.script'), os.path.join(dopsuf_dir, 'vasp.script'))
            mC.create_POTCAR(dopsuf_dir, './data/potpaw_PBE.54')
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
    make_dopdirs(work_dir)
###
if __name__ == '__main__':
    main()
