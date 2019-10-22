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
def check_ts(INCAR, OUTCAR, printout):
    ### get name
    file_name = OUTCAR.split('/')
    name = file_name[-3] + '/' + file_name[-2]
    ###
    ### get NSW
    with open(INCAR, 'r') as f:
        content = f.readlines()
        for line in content:
            if re.match(r'NSW.*', line):
                NSW = line.split(' ')[2]
    ### get converg status
    end_string = ' reached required accuracy - stopping structural energy minimisation\n'
    with open(printout, 'r') as f:
        content = f.readlines()
        if content[-1] == end_string:
            finish_flag = 1
        else:
            finish_flag = 0
    ###
    if finish_flag == 1:
        return '=Finished=', '{:<25}{:^15}\n'.format(name, '=Finished=')
    else:   
        ### get forces
        forces = []
        distance_inputs = []
        distance_opts = []
        ## get outcat information
        forces_file = os.popen(r'grep %s %s' %('RMS', OUTCAR))
        inputs_file = os.popen(r'grep %s %s' %('\'distance input to fix\'', OUTCAR))
        opts_file = os.popen(r'grep %s %s' %('\'distance after opt\'', OUTCAR))
        ##
        forces_content = forces_file.readlines()
        inputs_content = inputs_file.readlines()
        opts_content = opts_file.readlines()
        if len(forces_content) == len(inputs_content) and len(forces_content) == len(opts_content) \
                and len(forces_content) >0:
            for line in forces_content:
                line = line.strip('\n').split(' ')[-5]
                forces.append(line) 
            for line in inputs_content:
                line = line.strip('\n').split(' ')[-1]
                distance_inputs.append(line)
            for line in opts_content:
                line = line.strip('\n').split(' ')[-1]
                distance_opts.append(line)
            ###
            steps = []
            distance_step = [-1,-1]
            ## insert a list
            distance_step[1:1] = distance_inputs
            for i in range(1,len(distance_step)):
                if not distance_step[i] == distance_step[i-1]:
                    steps.append(i-1)
            steps = steps[1:]
            #
            if int(steps[-1]) < int(NSW):
                    converg_flag = '=Calculating='
            elif abs(float(forces[-1])) > 0.05:
                    converg_flag = '=Unconverged='
            #
            step = steps[-1]
            content = '{:<25}{:^15}Step:{:<10}Input:{:<15}Force:{:<15}Opt:{:<15}\n'\
                    .format(name, converg_flag, step, \
                    distance_inputs[step-1], forces[step-1], distance_opts[step-1])
        else:
            converg_flag = '=Waiting='
            content = '{:<25}{:^15}\n'.format(name, converg_flag)
            #
        ###
        return converg_flag, content 
###
def multi_check(check_dir = r'./'):
    check_list = []
    finish_content = ''
    sum_content = ''
    for root,dirs,files in os.walk(check_dir):
        if re.match(r'.*ts$', root):
            incar_path = os.path.abspath(os.path.join(root, 'INCAR'))
            outcar_path = os.path.abspath(os.path.join(root, 'OUTCAR'))
            printout_path = os.path.abspath(os.path.join(root, 'print-out'))
            if os.path.exists(outcar_path) and os.path.exists(incar_path):
                check_result, check_content = check_ts(incar_path, outcar_path, printout_path)
                check_list.append(check_result)
                sum_content += check_content
    ###
    sum_content += '{:^5}{:<15}   '.format(len(check_list), '=Total=')
    for item in set(check_list):
        sum_content += '{:^5}{:<15}   '.format(check_list.count(item), item)
    print(sum_content)
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
