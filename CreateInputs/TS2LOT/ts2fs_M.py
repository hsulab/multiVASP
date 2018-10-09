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
def prepare_fs(work_dir, finished_dirs):
    result_path = os.path.join(work_dir, 'prepare_fs_M.xu')
    if not os.path.exists(result_path):
        print('Start!')
    else:
        print('%s exists!' %(result_path))
        os.system(r'rm %s' %(result_path))
        print('%s is removed!' %(result_path))
    ###
    for dir in finished_dirs:
        ts_dir = os.path.join(dir, 'ts')
        fs_dir = os.path.join(dir, 'fs')
        if os.path.exists(fs_dir):
            if not os.path.exists(os.path.join(fs_dir, 'print-out')):
                print(fs_dir)
                shutil.rmtree(fs_dir)
                os.system(r'echo %s rming and making fs >> %s' %(fs_dir, result_path))
                os.mkdir(fs_dir)
                mC.create_VASPsp(dir, ts_dir, fs_dir)
                mC.create_INCAR(dir, ts_dir, fs_dir, '2')
                shutil.copyfile(os.path.join(ts_dir, 'CONTCAR'), os.path.join(fs_dir, 'POSCAR'))
                shutil.copyfile(os.path.join(ts_dir, 'KPOINTS'), os.path.join(fs_dir, 'KPOINTS'))
                mC.create_POTCAR(fs_dir, './data/potpaw_PBE.54')
        else:
            print(fs_dir)
            os.system(r'echo %s making fs >> %s' %(fs_dir, result_path))
            os.mkdir(fs_dir)
            mC.create_VASPsp(dir, ts_dir, fs_dir)
            mC.create_INCAR(dir, ts_dir, fs_dir, '2')
            shutil.copyfile(os.path.join(ts_dir, 'KPOINTS'), os.path.join(fs_dir, 'KPOINTS'))
            shutil.copyfile(os.path.join(ts_dir, 'CONTCAR'), os.path.join(fs_dir, 'POSCAR'))
            mC.create_POTCAR(fs_dir, './data/potpaw_PBE.54')
###
def main():
    if len(sys.argv) == 1:
        work_dir = r'./data/dopRutile'
        finished_dirs = mW.check_printout(work_dir, 'ts')
        print(finished_dirs)
        prepare_fs(work_dir, finished_dirs)       
    elif len(sys.argv) == 2:
        work_dir = sys.argv[1] 
        finished_dirs = mW.check_printout(work_dir, 'ts')
        prepare_fs(work_dir, finished_dirs)       
    elif len(sys.argv) == 3:
        work_dir = sys.argv[1]
        element = sys.argv[2]
        finished_dirs = []
        converg_dirs = mW.check_printout(work_dir, 'ts')
        for vasp_dir in converg_dirs:
            if re.match(r'.*' + element + r'O2_.*', vasp_dir):
                finished_dirs.append(vasp_dir)
        prepare_fs(work_dir, finished_dirs)       
    else:
        print('Wrong argvs!')
        sys.exit()
    ###
###
if __name__ == '__main__':
    main()
