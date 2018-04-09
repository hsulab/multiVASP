#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: multiQsub.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 日  3/18 21:28:59 2018
#d########################################################################
#qsub: Maximum number of jobs already in queue for user MSG=total number of current user's jobs exceeds the queue limit: user jyxu@master.cluster, queue bigmem
###
import multiSet as mS
##
import os
import sys
import re
###
def check_argv():
    reaction_types = ['bulk', 'suf', 'ts', 'fs', 'Hab', 'CH3ab']
    if len(sys.argv) == 3 and os.path.isdir(sys.argv[1]) and \
            sys.argv[2] in reaction_types:
        qsub_path = sys.argv[1]
        reaction_type = sys.argv[2]
        logfile = os.path.abspath(os.path.join(qsub_path, 'qsub_results.xu'))
        if os.path.exists(logfile):
            print('qsub_results.xu exists!')
            print('A new qsub_results.xu is created!')
            os.remove(logfile)
        else:
            print('Start!')
        return qsub_path, reaction_type, logfile
    else:
        print('multiQsub.py [qsub_path] [reaction_type]')
        print('Please check the argvs.')
        return 0
    ###
### qsub_dirs must be abspath.
def get_qsub_dirs(qsub_path, reaction_type):
    qsub_dirs = []
    qsub_path = os.path.abspath(qsub_path)
    vaspfiles = ['INCAR','POSCAR','POTCAR','KPOINTS','vasp.script']
    ###
    for root, dirs, files in os.walk(qsub_path):
        if os.path.basename(root) == reaction_type:
            if set(vaspfiles) & set(os.listdir(root)) == set(vaspfiles):
                if 'print-out' not in os.listdir(root):
                    print(os.listdir(root))
                    qsub_dirs.append(root)
                else:
                    lackfile = set(vaspfiles) - set(os.listdir(root))
                    lackfile = [str(i) for i in lackfile]
                    if lackfile != []:
                        print(r'%s Lack %s!' %(root, lackfile))
    return qsub_dirs
###
def qsub_script(path, queue= 'bigmem'):
    os.chdir(path)
    mS.set_VASPsp('vasp.script', '#PBS -q', queue, 1)
    qsub_file = os.popen(r'qsub vasp.script')
    qsub_result = qsub_file.readlines()
    qsub_result = queue + ': ' + path + ' ' + ''.join(qsub_result)
    return qsub_result
    
###
def qsub_all(qsub_dirs, number, logfile):
    with open(logfile, 'w+') as f:
        for qsub_dir in qsub_dirs:
            if qsub_dirs.index(qsub_dir) < int(number/2):
                f.write(qsub_script(qsub_dir, 'bigmem'))
            elif int(number/2) < qsub_dirs.index(qsub_dir) <= number:
                f.write(qsub_script(qsub_dir, 'normal'))
###
def main():
    if not check_argv() == 0:
        qsub_path, reaction_type, logfile =  check_argv()
        qsub_dirs = get_qsub_dirs(qsub_path, reaction_type)
        qsub_all(qsub_dirs, 16, logfile)
###
if __name__ == '__main__':
    main()
