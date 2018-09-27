#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: get_Ea.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 一  4/ 9 20:06:27 2018
#########################################################################
import os
import re
import sys
###
def get_TOTEN(OUTCAR):
    TOTEN_list = []
    with open(OUTCAR, 'r') as f:
        for line in f.readlines():
            if re.match(r'.*TOTEN.*', line):
                line = line.strip('\n').split(' ')[-2]
                TOTEN_list.append(line)
    TOTEN = TOTEN_list[-1]
    return TOTEN
###
def check_converg(print_out):
    converg_flag = ' reached required accuracy - stopping structural energy minimisation\n'
    with open(print_out, 'r') as f:
        content = f.readlines()
    if content[-1] == converg_flag:
        return True
    else:
        return False
###
def multi_Ea(work_dir):
    Ea_dir = []
    for root, dirs, files in os.walk(work_dir):
        root_dirs = os.listdir(root)
        if set(['suf', 'ts']).issubset(set(root_dirs)):
            Ea_dir.append(root)
    ###
    Ea_content = ''
    Ea_content = '{:<20}{:>20}{:>20}{:>20}'\
            .format('dir_name', 'ts', 'suf+CH4', 'Ea')
    CH4_TOTEN = '-24.07015819'
    for vasp_dir in Ea_dir:
        suf = os.path.join(vasp_dir, 'suf')
        ts = os.path.join(vasp_dir, 'ts')
        if set(['print-out','OUTCAR']).issubset(set(os.listdir(suf))) and \
                set(['print-out','OUTCAR']).issubset(set(os.listdir(ts))):
                    suf_outcar = os.path.join(suf, 'OUTCAR')
                    suf_printout = os.path.join(suf, 'print-out')
                    ts_outcar = os.path.join(ts, 'OUTCAR')
                    ts_printout = os.path.join(ts, 'print-out')
                    if check_converg(suf_printout) and check_converg(ts_printout):
                        suf_TOTEN = get_TOTEN(suf_outcar)
                        sufCH4_TOTEN = float(suf_TOTEN) + float(CH4_TOTEN)
                        ts_TOTEN = get_TOTEN(ts_outcar)
                        Ea = '\n{:<20}{:>20}{:>20}{:>20}'\
                                .format(os.path.basename(vasp_dir), \
                                ts_TOTEN, sufCH4_TOTEN, \
                                float(ts_TOTEN)-float(sufCH4_TOTEN))
                        Ea_content += Ea
    print(Ea_content)


###
def main():
    if len(sys.argv) == 1:
        print('get_Ea.py . [DEFAULT]')
        print('Get Ea in current dir.')
        multi_Ea(r'.')
    elif len(sys.argv) == 2:
        if os.path.isdir(sys.argv[1]):
            multi_Ea(sys.argv[1])
    else:
        print('Wrong argv.')

###
if __name__ == '__main__':
    main()
