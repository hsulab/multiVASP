#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: check_ts.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 一  3/26 22:36:31 2018
#########################################################################
import os 
import re
import sys
###
def check_ts(OUTCAR, echo_option = 1):
    forces = []
    distance_inputs = []
    distance_opts = []
    ###
    file_name = OUTCAR.split('/')
    name = file_name[-3] + '/' + file_name[-2]
    ###
    forces_file = os.popen(r'grep %s %s' %('RMS', OUTCAR))
    inputs_file = os.popen(r'grep %s %s' %('\'distance input to fix\'', OUTCAR))
    opts_file = os.popen(r'grep %s %s' %('\'distance after opt\'', OUTCAR))
    if not ( (forces_file == []) or (inputs_file == []) or (opts_file == []) ):
        for line in forces_file.readlines():
            line = line.strip('\n').split(' ')[-5]
            forces.append(line) 
        for line in inputs_file.readlines():
            line = line.strip('\n').split(' ')[-1]
            distance_inputs.append(line)
        for line in opts_file.readlines():
            line = line.strip('\n').split(' ')[-1]
            distance_opts.append(line)
        ###
        steps = []
        distance_step = [-1,-1]
        distance_step[1:1] = distance_inputs
        for i in range(1,len(distance_step)):
            if not distance_step[i] == distance_step[i-1]:
                steps.append(i-1)
        steps = steps[1:]
        #
        if abs(float(forces[-1])) <= 0.05:
            finish_flag = '=Finished='
        else:
            if int(steps[-1]) < 1000:
                finish_flag = '=Calculating='
            else:
                finish_flag = '=Unconverged='
        #
        content = ''
        for step in steps:
            content += '{:<25}{:^15}Step:{:<10}Input:{:<15}Force:{:<15}Opt:{:<15}\n'\
                    .format(name, finish_flag, step, \
                    distance_inputs[step-1], forces[step-1], distance_opts[step-1])
    else:
        content = '{:<25}{:^15}\n'.format(name, '=Waiting=')
        #
    if echo_option == 1:
        print(content.split('\n')[-2])
    else:
        print(content)
    ###
    return finish_flag 
###
def multi_check(check_dir = r'./'):
    finish_list = []
    for root,dirs,files in os.walk(check_dir):
        if re.match(r'.*ts', root):
            outcar_path = os.path.abspath(os.path.join(root, 'OUTCAR'))
            if os.path.exists(outcar_path):
                finish_list.append(check_ts(outcar_path))
    ###
    content = ''
    for item in set(finish_list):
        content += '{:^5}{:<15}   '.format(finish_list.count(item), item)
    print(content)
###
def main():
    if len(sys.argv) == 1:
        print(r'check_ts.py . [DEFAULT]')
        multi_check()
    elif len(sys.argv) == 2:
        check_dir = sys.argv[1]
        multi_check(check_dir)
    else:
        print(r'check_ts.py [directory]')
###
if __name__ == '__main__':
   main()
