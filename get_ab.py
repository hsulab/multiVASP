#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: get_ab.py
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
def multi_ab(work_dir):
    ab_dir = []
    for root, dirs, files in os.walk(work_dir):
        root_dirs = os.listdir(root)
        if set(['suf']).issubset(set(root_dirs)):
            ab_dir.append(root)
    ###
    ab_content = ''
    ab_content = '{:<20}{:>20}{:>20}{:>20}'\
            .format('dir_name', 'Hab_sp2', 'Hab_sp3', 'CH3ab')
    H_TOTEN = '-1.11501367'
    CH3_TOTEN = '-18.21859244'
    for vasp_dir in ab_dir:
        suf = os.path.join(vasp_dir, 'suf')
        suf_printout = os.path.join(suf, 'print-out')
        Hab_sp2 = os.path.join(vasp_dir, 'Hab_sp2')
        Hab_sp3 = os.path.join(vasp_dir, 'Hab_sp3')
        CH3ab = os.path.join(vasp_dir, 'CH3ab')
        if os.path.exists(suf) and \
                set(['print-out','OUTCAR']).issubset(set(os.listdir(suf))) and \
                check_converg(suf_printout):
            ###
            suf_outcar = os.path.join(suf, 'OUTCAR')
            suf_TOTEN = get_TOTEN(suf_outcar)
            sufH_TOTEN = float(suf_TOTEN) + float(H_TOTEN)
            sufCH3_TOTEN = float(suf_TOTEN) + float(CH3_TOTEN)
            ###
            Hab_sp2_printout = os.path.join(Hab_sp2, 'print-out')
            Hab_sp3_printout = os.path.join(Hab_sp3, 'print-out')
            CH3ab_printout = os.path.join(CH3ab, 'print-out')
            if os.path.exists(Hab_sp2) and \
            set(['print-out','OUTCAR']).issubset(set(os.listdir(Hab_sp2))) and \
                    check_converg(Hab_sp2_printout):
                Hab_sp2_outcar = os.path.join(Hab_sp2, 'OUTCAR')
                Hab_sp2_TOTEN = get_TOTEN(Hab_sp2_outcar)
                E_Hab_sp2 = float(Hab_sp2_TOTEN)-float(sufH_TOTEN) 
            else:
                E_Hab_sp2 = ''
            if os.path.exists(Hab_sp3) and \
            set(['print-out','OUTCAR']).issubset(set(os.listdir(Hab_sp3))) and \
                    check_converg(Hab_sp3_printout):
                Hab_sp3_outcar = os.path.join(Hab_sp3, 'OUTCAR')
                Hab_sp3_TOTEN = get_TOTEN(Hab_sp3_outcar)
                E_Hab_sp3 = float(Hab_sp3_TOTEN)-float(sufH_TOTEN) 
            else:
                E_Hab_sp3 = ''
            if os.path.exists(CH3ab) and \
            set(['print-out','OUTCAR']).issubset(set(os.listdir(CH3ab))) and \
                    check_converg(CH3ab_printout):
                CH3ab_outcar = os.path.join(CH3ab, 'OUTCAR')
                CH3ab_TOTEN = get_TOTEN(CH3ab_outcar)
                E_CH3ab = float(CH3ab_TOTEN)-float(sufCH3_TOTEN) 
            else:
                E_CH3ab = ''
            if [E_Hab_sp2, E_Hab_sp3, E_CH3ab] != ['', '', '']:
                ab = '\n{:<20}{:>20}{:>20}{:>20}'\
                        .format(os.path.basename(vasp_dir), \
                        E_Hab_sp2, E_Hab_sp3, E_CH3ab)
                ab_content += ab
    print(ab_content)
###
def main():
    if len(sys.argv) == 1:
        print('get_ab.py . [DEFAULT]')
        print('Get ab in current dir.')
        multi_ab(r'.')
    elif len(sys.argv) == 2:
        if os.path.isdir(sys.argv[1]):
            multi_ab(sys.argv[1])
    else:
        print('Wrong argv.')

###
if __name__ == '__main__':
    main()
