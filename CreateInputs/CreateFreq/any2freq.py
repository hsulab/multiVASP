#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: ts2freq.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 日  3/18 18:36:16 2018
#########################################################################
import os; import re
import sys; import shutil 
###
import CreateCars
from SetParams import set_param
import CheckOut
###
def create_INCAR(root_dir, old_dir, new_dir):
    'Get Path'
    old_INCAR = os.path.join(old_dir, 'INCAR')
    new_INCAR = os.path.join(new_dir, 'INCAR')
    shutil.copyfile(old_INCAR, new_INCAR)
    job_name = os.path.basename(root_dir) + '_' + os.path.basename(new_dir)
    set_param(new_INCAR, 'SYSTEM', 'SYSTEM=%s\n'%job_name)
    set_param(new_INCAR, 'IBRION', 'IBRION=5\n')
    set_param(new_INCAR, 'POTIM', 'POTIM=0.015\nNFREE=2\n')
    set_param(new_INCAR, 'NSW', 'NSW=1\n')
###
def create_POSCAR(root_dir, old_dir, new_dir, f_atoms):
    'Copy CONTCAR to POSCAR'
    shutil.copyfile(os.path.join(old_dir, 'CONTCAR'), os.path.join(new_dir, 'POSCAR'))
    'Read POSCAR'
    with open(os.path.join(new_dir, 'POSCAR'), 'r') as f:
        content = f.readlines()
    'Make new POSCAR' 
    new_content = ''
    # abc 1~7 Selective Dy... 8~9
    for i in range(9):
        new_content += content[i]
    # atoms xyz
    for line in content[9:9+f_atoms]:
        new_line = []
        line = line.strip('\n').split(' ')
        for i in line:
            if i != '':
                new_line.append(i)
        new_content += '{:>20}{:>20}{:>20}  T  T  T\n'\
                .format(new_line[0], new_line[1], new_line[2])
    for line in content[9+f_atoms:57+f_atoms]:
        new_line = []
        line = line.strip('\n').split(' ')
        for i in line:
            if i != '':
                new_line.append(i)
        new_content += '{:>20}{:>20}{:>20}  F  F  F\n'\
                .format(new_line[0], new_line[1], new_line[2])
    with open(os.path.join(new_dir, 'POSCAR'), 'w') as f:
        f.write(new_content)
###
def prepare_freq(finished_dirs, reaction):
    'rtype' 
    rtype={};
    rtype['Hab_sp2']=1;rtype['Hab_sp3']=1;
    rtype['CH3ab']=4;
    rtype['ts']=5;rtype['ts_ra']=5;
    rtype['fs']=5
    'Find Dirs'
    for root_dir in finished_dirs:
        'print log'
        content = ''
        'Origin and Target'
        origin = os.path.join(root_dir, reaction)
        target = os.path.join(root_dir, reaction+'_f')
        'Create Inputs'
        content += '{:<30}'.format(target)
        printout = os.path.join(target, 'print-out')
        if os.path.exists(target):
            if os.path.exists(printout):
                content += '--> print-out exists.\n'
            else:
                'Remove existed and uncalculated dir'
                content += '--> remove old files and create new.\n'
                shutil.rmtree(target)
                os.mkdir(target)
        else:
            os.mkdir(target)
        'Create'
        'vasp.script'
        CreateCars.create_VASPsp(root_dir, origin, target)
        'INCAR'
        create_INCAR(root_dir, origin, target)
        'POSCAR'
        create_POSCAR(root_dir, origin, target, rtype[reaction])
        'POTCAR'
        CreateCars.create_POTCAR(target)
        'KPOINTS'
        shutil.copyfile(os.path.join(origin, 'KPOINTS'), os.path.join(target, 'KPOINTS'))
        content += '--> Create Success.\n'
        print(content)
###
def main():
    if len(sys.argv) == 1:
        work_dir = r'./TestDir/'
        if os.path.exists(work_dir):
            finished_dirs = CheckOut.check_printout(work_dir, 'ts')
            print('Finished Dirs: ', finished_dirs)
            prepare_freq(finished_dirs, 'ts')       
        else:
            print('Test Only.')
    elif len(sys.argv) == 4:
        'Get argvs'
        work_dir = sys.argv[1]
        reaction = sys.argv[2]
        element = sys.argv[3]
        ''
        finished_dirs = []
        converg_dirs = CheckOut.check_printout(work_dir, reaction)
        for vasp_dir in converg_dirs:
            if re.match(r'.*' + element + r'O2_.*', vasp_dir):
                finished_dirs.append(vasp_dir)
        print('Finished Dirs: ', finished_dirs)
        prepare_freq(finished_dirs, reaction)
    else:
        print('any2freq.py [Dir] [Reaction] [Metal]')
        sys.exit()
###
if __name__ == '__main__':
    main()
