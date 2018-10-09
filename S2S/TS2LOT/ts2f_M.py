#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: ts2freq.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 日  3/18 18:36:16 2018
#########################################################################
import os
import re
import shutil
import sys
###
import multiCAR as mC
import multiWalk as mW
import multiSet as mS
###
def create_INCAR(root_dir, old_dir, new_dir):
    old_INCAR = os.path.join(old_dir, 'INCAR')
    new_INCAR = os.path.join(new_dir, 'INCAR')
    shutil.copyfile(old_INCAR, new_INCAR)
    mS.set_INCAR(new_INCAR, 'SYSTEM', os.path.basename(root_dir) + '_' + \
            os.path.basename(new_dir), 1)
    mS.set_INCAR(new_INCAR, 'IBRION', '5', 1)
    mS.set_INCAR(new_INCAR, 'POTIM', '0.015', 1)

###
def create_POSCAR(root_dir, old_dir, new_dir):
    shutil.copyfile(os.path.join(old_dir, 'CONTCAR'), os.path.join(new_dir, 'POSCAR'))
    with open(os.path.join(new_dir, 'POSCAR'), 'r') as f:
        content = f.readlines()
    new_content = ''
    for i in range(7):
        new_content += content[i]
    for line in content[7:9]:
        new_content += line
    for line in content[9:14]:
        new_line = []
        line = line.strip('\n').split(' ')
        for i in line:
            if i != '':
                new_line.append(i)
        new_content += '{:>20}{:>20}{:>20}  T  T  T\n'\
                .format(new_line[0], new_line[1], new_line[2])
    for line in content[14:62]:
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
def prepare_freq(work_dir, finished_dirs):
    result_path = os.path.join(work_dir, 'prepare_tsf.xu')
    if not os.path.exists(result_path):
        print('Start!')
    else:
        print('%s exists!' %(result_path))
        os.system(r'rm %s' %(result_path))
        print('%s is removed!' %(result_path))
    ###
    for dir in finished_dirs:
        ts_dir = os.path.join(dir, 'ts')
        freq_dir = os.path.join(dir, 'ts_f')
        if os.path.exists(freq_dir):
            if not os.path.exists(os.path.join(freq_dir, 'print-out')):
                print(freq_dir)
                shutil.rmtree(freq_dir)
                os.system(r'echo %s rming and making tsfreq >> %s' %(freq_dir, result_path))
                os.mkdir(freq_dir)
                mC.create_VASPsp(dir, ts_dir, freq_dir)
                create_INCAR(dir, ts_dir, freq_dir)
                shutil.copyfile(os.path.join(ts_dir, 'KPOINTS'), os.path.join(freq_dir, 'KPOINTS'))
                create_POSCAR(dir, ts_dir, freq_dir)
                mC.create_POTCAR(freq_dir, './data/potpaw_PBE.54')
        else:
            print(freq_dir)
            os.system(r'echo %s making freq >> %s' %(freq_dir, result_path))
            os.mkdir(freq_dir)
            mC.create_VASPsp(dir, ts_dir, freq_dir)
            create_INCAR(dir, ts_dir, freq_dir)
            shutil.copyfile(os.path.join(ts_dir, 'KPOINTS'), os.path.join(freq_dir, 'KPOINTS'))
            create_POSCAR(dir, ts_dir, freq_dir)
            mC.create_POTCAR(freq_dir, './data/potpaw_PBE.54')

###
def main():
    if len(sys.argv) == 1:
        work_dir = r'./data/dopRutile'
        finished_dirs = mW.check_printout(work_dir, 'ts')
        print(finished_dirs)
        prepare_freq(work_dir, finished_dirs)       
    elif len(sys.argv) == 2:
        work_dir = sys.argv[1] 
        finished_dirs = mW.check_printout(work_dir, 'ts')
        prepare_freq(work_dir, finished_dirs)       
    elif len(sys.argv) == 3:
        work_dir = sys.argv[1]
        element = sys.argv[2]
        finished_dirs = []
        converg_dirs = mW.check_printout(work_dir, 'ts')
        for vasp_dir in converg_dirs:
            if re.match(r'.*' + element + r'O2_.*', vasp_dir):
                finished_dirs.append(vasp_dir)
        prepare_freq(work_dir, finished_dirs)       
    else:
        print('Wrong argvs!')
        sys.exit()
###
if __name__ == '__main__':
    main()
