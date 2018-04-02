#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: multiWalk.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 五  3/30 15:08:51 2018
#########################################################################
import os
import re
###
def check_printout(check_dir, reaction_type):
    check_list = []
    for root,dirs,files in os.walk(check_dir):
        if re.match(r'.*' + reaction_type, root):
            if os.path.exists(os.path.join(root, 'print-out')):
                check_list.append(root)
   ###
    result_path = os.path.join(check_dir, 'check_printout.xu')
    if not os.path.exists(result_path):
        print('Start!')
    else:
        print('%s exists!' %(result_path))
        os.system(r'rm %s' %(result_path))
        print('%s is removed!' %(result_path))
    ###
    finish_flag = ' reached required accuracy - stopping structural energy minimisation\n'
    finished_dirs = []
    for check in check_list:
        printout = os.path.abspath(os.path.join(check, 'print-out'))
        with open(printout, 'r') as f:
            content = f.readlines()
            if content[-1] == finish_flag:
                os.system(r'echo Calculation finished in %s! >> %s' %(check, result_path))
                finished_dirs.append(os.path.dirname(check))
            else:
                os.system(r'echo Calculation undone or unconverged in %s! >> %s' %(check, result_path))
    return finished_dirs
###
def main():
    print()
###
if __name__ == '__main__':
    main()
