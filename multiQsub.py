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
from autoSet import set_VASPsp
##
import os
import sys
import re
###
def check_argv():
    reaction_types = ['bulk', 'suf', 'ts', 'fs', 'ab']
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
                qsub_dirs.append(root)
            else:
                if 'print-out' in os.listdir(root):
                    os.system(r'echo %s Already qsub vasp.script! >> %s' %(root, logfile))
                else:
                    lackfile = set(vaspfiles) - set(os.listdir(root))
                    lackfile = [str(i) for i in lackfile]
                    os.system(r'echo %s Lack %s! >> %s' %(root, lackfile, logfile))
    return qsub_dirs
###
def qsub_script(path, queue):
    os.chdir(path)
    os.system(r'echo -e "%s in %s    \c" >> %s' %(path, queue, logfile))
    os.system(r'qsub vasp.script >> %s' %(logfile))
    os.chdir(qsub_path)
###
def qsub_all(number):
    for qsub_dir in qsub_dirs:
        vasp_script = os.path.join(qsub_dir, 'vasp.script')
        ### set default
        set_VASPsp(vasp_script, '#PBS -q', 'bigmem', 1)
        ###
        with open(vasp_script, 'r') as f:
            queue = f.readlines()[6]
        if qsub_dirs.index(qsub_dir) < int(number/2):
            qsub_script(qsub_dir, 'bigmem')
        elif int(number/2) < qsub_dirs.index(qsub_dir) <= number:
            set_VASPsp(vasp_script, '#PBS -q', 'normal', 1)
            qsub_script(qsub_dir, 'normal')
###
def main():
    if not check_argv() == 0:
        qsub_path, reaction_type, logfile =  check_argv()
        get_qsub_dirs(qsub_path, reaction_type)
        qsub_all(16)
###
if __name__ == '__main__':
    main()
