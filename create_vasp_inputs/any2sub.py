#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: multiQsub_M.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 日  3/18 21:28:59 2018
#d########################################################################
'''
*Usage*
any2sub.py [qsub_path] [reaction_type] [element]

*Example*

*Bug*
In the check process of <get_qsub_dirs>, check <qstat> first.

'''

import os
import sys
import re

def set_param(inputfile, para, value):
    new_inputfile = ''
    with open(inputfile, 'r') as f:
        for line in f:
            if re.match(r'^%s.*' %(para), line):
                line = '%s' %(value)
            new_inputfile += line
    with open(inputfile, 'w') as f:
        f.write(new_inputfile)

def get_qsub_dirs(qsub_path, reaction_type, element):
    qsub_dirs = [] # qsub_dirs must be abspath.
    qsub_path = os.path.abspath(qsub_path)
    vaspfiles = ['INCAR','POSCAR','POTCAR','KPOINTS','vasp.script']

    for root, dirs, files in os.walk(qsub_path):
        if re.match(r'.*dop'+element+r'O2_.*', os.path.dirname(root)) or \
                re.match(r'pure' + element + r'O2', os.path.basename(vasp_dir)):
            if os.path.basename(root) == reaction_type:
                if set(vaspfiles) & set(os.listdir(root)) == set(vaspfiles):
                    if 'print-out' not in os.listdir(root):
                        qsub_dirs.append(root)
                else:
                    lackfile = set(vaspfiles) - set(os.listdir(root))
                    lackfile = [str(i) for i in lackfile]
                    if lackfile != []:
                        print(r'%s Lack %s!' %(root, lackfile))
    return qsub_dirs

def qsub_all(qsub_dirs, number):
    def qsub_script(path, queue= 'normal'):
        os.chdir(path)
        set_param('vasp.script', '#PBS -q', '#PBS -q %s\n' %queue)
        qsub_file = os.popen(r'qsub vasp.script')
        qsub_result = qsub_file.readlines()
        qsub_result = queue + ': ' + path + ' ' + ''.join(qsub_result)
        return qsub_result

    for qsub_dir in qsub_dirs:
        if qsub_dirs.index(qsub_dir)<number:
            print(qsub_dir)
            qsub_script(qsub_dir, 'normal')

def main():
    'Supported reaction types and elements'
    reaction_types = ['bulk', 'suf', \
            'ts', 'ts_ra','fs', 'fs_ra', \
            'Hab_sp2', 'Hab_sp3', 'CH3ab', 'CH3ab2',\
            'ts_f', 'ts_ra_f', 'Hab_sp2_f', 'Hab_sp3_f', 'CH3ab_f', 'CH3ab2_f']
    elements = ['Ti', 'V', 'Cr', 'Mn', 'Ge', 'Mo', 'Ru', 'Rh', 'Os', 'Ir', 'Pb']

    'Check arguments'
    if len(sys.argv) == 4 and os.path.isdir(sys.argv[1]) and \
            sys.argv[2] in reaction_types and sys.argv[3] in elements:
        # get arguments
        qsub_path = sys.argv[1]
        reaction_type = sys.argv[2]
        element = sys.argv[3]

        # sub tasks
        qsub_dirs = get_qsub_dirs(qsub_path, reaction_type, element)
        qsub_all(qsub_dirs, 8)
    else:
        print('any2sub.py [qsub_path] [reaction_type] [element]')

if __name__ == '__main__':
    main()
