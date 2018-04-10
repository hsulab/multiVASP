#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: suf2ts.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 日  3/18 18:36:16 2018
#########################################################################
import os
import shutil
import sys
###
import multiCAR as mC
import multiWalk as mW
###
def create_POSCAR(dir, suf_dir, ts_dir):
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
    new_content += '  0.573521486444      0.332890746494      0.542347538452       T   T   T\n\
  0.583968473201      0.643085208862      0.567518468967       T   T   T\n\
  0.723722447115      0.386856169075      0.609219236308       T   T   T\n\
  0.442815428287      0.383751349500      0.612745621226       T   T   T\n\
  0.578859020373      0.423707074865      0.584519962387       T   T   T\n'
    for line in content[9:58]:
        new_content += line
    with open(os.path.join(ts_dir, 'POSCAR'), 'w') as f:
        f.write(new_content)
###
def create_fort188(dir, suf_dir, ts_dir):
    with open(os.path.join(ts_dir, 'fort.188'), 'w') as f:
        f.write('1\n3\n6\n4\n0.04\n2   5     1.45016\n0')
###
###
def prepare_ts(work_dir, finished_dirs):
    result_path = os.path.join(work_dir, 'prepare_ts.xu')
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
            if not os.path.exists(os.path.join(ts_dir, 'print-out')):
                shutil.rmtree(ts_dir)
                os.system(r'echo %s rming and making ts >> %s' %(ts_dir, result_path))
                os.mkdir(ts_dir)
                mC.create_VASPsp(dir, suf_dir, ts_dir)
                mC.create_INCAR(dir, suf_dir, ts_dir, '1')
                shutil.copyfile(os.path.join(suf_dir, 'KPOINTS'), os.path.join(ts_dir, 'KPOINTS'))
                create_POSCAR(dir, suf_dir, ts_dir)
                mC.create_POTCAR(ts_dir, './potpaw_PBE.54')
                create_fort188(dir, suf_dir, ts_dir)
        else:
            os.system(r'echo %s making ts >> %s' %(ts_dir, result_path))
            os.mkdir(ts_dir)
            mC.create_VASPsp(dir, suf_dir, ts_dir)
            mC.create_INCAR(dir, suf_dir, ts_dir, '1')
            shutil.copyfile(os.path.join(suf_dir, 'KPOINTS'), os.path.join(ts_dir, 'KPOINTS'))
            create_POSCAR(dir, suf_dir, ts_dir)
            mC.create_POTCAR(ts_dir, './potpaw_PBE.54')
            create_fort188(dir, suf_dir, ts_dir)

###
##
work_dir = []
if len(sys.argv) == 1:
    work_dir = r'./data/dopIrO2_2'
elif len(sys.argv) == 2:
    work_dir = sys.argv[1]
    if not os.path.isdir(work_dir):
        sys.exit()
finished_dirs = mW.check_printout(work_dir, 'suf')
prepare_ts(work_dir, finished_dirs)
