#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: multiCAR.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 一  4/ 2 21:38:15 2018
#########################################################################
import os
import shutil
import multiSet as mS
'''
from old_dir to new_dir, vasp.script, INCAR, POSCAR, POTCAR, KPOINTS, fort.188
'''
####
def create_VASPsp(root_dir, old_dir, new_dir):
    old_VASPsp = os.path.join(old_dir, 'vasp.script')
    new_VASPsp = os.path.join(new_dir, 'vasp.script')
    shutil.copyfile(old_VASPsp, new_VASPsp)
    mS.set_VASPsp(new_VASPsp, '#PBS -N', os.path.basename(root_dir) + \
            '_' + os.path.basename(new_dir), 1)
###
def create_INCAR(root_dir, old_dir, new_dir, ibrion_num):
    old_INCAR = os.path.join(old_dir, 'INCAR')
    new_INCAR = os.path.join(new_dir, 'INCAR')
    shutil.copyfile(old_INCAR, new_INCAR)
    mS.set_INCAR(new_INCAR, 'SYSTEM', os.path.basename(root_dir) + '_' + \
            os.path.basename(new_dir), 1)
    mS.set_INCAR(new_INCAR, 'IBRION', ibrion_num, 1)
###
def create_POSCAR(root_dir, old_dir, new_dir):
    content = []
    shutil.copyfile(os.path.join(old_dir, 'CONTCAR'), os.path.join(new_dir, 'POSCAR'))
    with open(os.path.join(new_dir, 'POSCAR'), 'r') as f:
        content = f.readlines()
    new_content = ''
    for i in range(5):
        new_content += content[i]
    new_content += '{:>5}{:>5}'.format('H', 'C') + str(content[5])
    new_content += '{:>5}{:>5}'.format('4', '1') + str(content[6])
    for line in content[7:9]:
        new_content += line
    new_content += '  0.573521486444      0.332890746494      0.542347538452       T   T   T\n\
  0.583968473201      0.643085208862      0.567518468967       T   T   T\n\
  0.723722447115      0.386856169075      0.609219236308       T   T   T\n\
  0.442815428287      0.383751349500      0.612745621226       T   T   T\n\
  0.578859020373      0.423707074865      0.584519962387       T   T   T\n'
    for line in content[9:58]:
        new_content += line
    with open(os.path.join(new_dir, 'POSCAR'), 'w') as f:
        f.write(new_content)
###
###
def create_POTCAR(new_dir, potdir= '/data/pot/vasp/potpaw_PBE.54'):
    POTCAR = ''
    element_pot_list = []
    with open(os.path.join(new_dir, 'POSCAR'), 'r') as f:
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
            print('Something wrong in %s: POTCAR.' %(new_dir))
            print('%s\n%s' %(element_pot_new, element_pot))
    for pot in element_pot_list:
        with open(pot, 'r') as f:
            pot_content = f.readlines()
        for line in pot_content:
            POTCAR += line
    with open(os.path.join(new_dir, 'POTCAR'), 'w') as f:
        f.write(POTCAR)
###
def create_fort188(root_dir, old_dir, new_dir):
    with open(os.path.join(new_dir, 'fort.188'), 'w') as f:
        f.write('1\n3\n6\n4\n0.04\n2   5     1.45016\n0')
##

###
def main():
    print()
###
if __name__ == '__main__':
    main()
