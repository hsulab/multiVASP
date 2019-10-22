#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: CreateCars.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 一  4/ 2 21:38:15 2018
#########################################################################
import os
import shutil
import SetParams as mS

'''
from old_dir to new_dir, vasp.script, INCAR, POSCAR, POTCAR, KPOINTS, fort.188
'''

def create_VASPsp(root_dir, old_dir, new_dir):
    'copy file'
    old_VASPsp = os.path.join(old_dir, 'vasp.script')
    new_VASPsp = os.path.join(new_dir, 'vasp.script')
    shutil.copyfile(old_VASPsp, new_VASPsp)

    'change $PBS -N'
    job_name =  os.path.basename(root_dir) + '_' + os.path.basename(new_dir)
    mS.set_param(new_VASPsp, '#PBS -N', '#PBS -N %s\n'%job_name)

def create_INCAR(root_dir, old_dir, new_dir, ibrion_num):
    'copy file'
    old_INCAR = os.path.join(old_dir, 'INCAR')
    new_INCAR = os.path.join(new_dir, 'INCAR')
    shutil.copyfile(old_INCAR, new_INCAR)

    'Set Parameters'
    mS.set_param(new_INCAR, 'SYSTEM', 'SYSTEM=' + os.path.basename(root_dir) + \
            '_' + os.path.basename(new_dir))
    mS.set_param(new_INCAR, 'IBRION', 'IBRION='+str(ibrion_num))

def create_POTCAR(new_dir, potdir= '/data/pot/vasp/potpaw_PBE.54'):
    ''
    POTCAR = ''
    element_pot_list = []

    'elements'
    with open(os.path.join(new_dir, 'POSCAR'), 'r') as f:
        elements = f.readlines()[5]
    elements = elements.strip('\n').split(' ')
    elements = [i for i in elements if not i == '']

    'Find POT'
    for element in elements:
        element_pot_new = '%s/%s_new/POTCAR' %(potdir, element)
        element_pot = '%s/%s/POTCAR' %(potdir, element)
        if os.path.exists(element_pot_new):
            element_pot_list.append(element_pot_new)
        elif os.path.exists(element_pot):
            element_pot_list.append(element_pot)
        else:
            print('Something wrong in %s: POTCAR.' %(new_dir))
            print('%s\n%s' %(element_pot_new, element_pot))

    'Write POT'
    for pot in element_pot_list:
        with open(pot, 'r') as f:
            pot_content = f.readlines()
        for line in pot_content:
            POTCAR += line

    with open(os.path.join(new_dir, 'POTCAR'), 'w') as f:
        f.write(POTCAR)

'Get lattice constant and atom coors of surface.'
def cell_info(CONTCAR):
    'Get lattice constant and atom coordinate.'
    abc, xyz = [], []
    with open(CONTCAR, 'r') as f:
        content = f.readlines()
        for i in range(2,5): # lattice constant
            a_abc = []
            for cor in content[i].strip('\n').split(' '):
                if cor not in ['']: 
                    a_abc.append(float(cor))
            abc.append(a_abc)
        for i in range(9,57): # four layers of 2x1 rutile surface
            a_xyz = [] 
            for cor in content[i].strip('\n').split(' '):
                if cor not in ['','T','F']: 
                    a_xyz.append(float(cor)) ###
            xyz.append(a_xyz)
    abc, xyz = np.array(abc), np.array(xyz)

    'Get atoms.'
    M_xyz = xyz[32:48]
    M_xyz_sortbyz = M_xyz[M_xyz[:,2].argsort()] # argsort, small to big

    dop_M_xyz = M_xyz_sortbyz[-4:]
    dop_M_xyz_sortbyx = dop_M_xyz[dop_M_xyz[:,0].argsort()]
    dop_s1_xyz = dop_M_xyz_sortbyx[2]
    dop_s2_xyz = dop_M_xyz_sortbyx[1] # different for V
    dop_s3_xyz = dop_M_xyz_sortbyx[3]

    O_xyz = xyz[0:32]
    O_xyz_sortbyz = O_xyz[O_xyz[:,2].argsort()]
    ab_O_xyz = O_xyz_sortbyz[-2:]
    ab_O_xyz_sortbyx = ab_O_xyz[ab_O_xyz[:,0].argsort()]
    ab_O_b_xyz = ab_O_xyz_sortbyx[1]

    return abc, xyz, dop_s1_xyz, dop_s2_xyz, dop_s3_xyz, ab_O_b_xyz

if __name__ == '__main__':
    print()
