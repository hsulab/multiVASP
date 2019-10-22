#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: CheckOut.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 五  3/30 15:08:51 2018
#########################################################################
import os
import re

def check_printout(check_dir, reaction_type):
    check_list = []
    for root,dirs,files in os.walk(check_dir):
        print(root)
        if re.match(r'.*(' + reaction_type + r')$', root):
            if os.path.exists(os.path.join(root, 'print-out')):
                check_list.append(root)

    finish_flag = ' reached required accuracy - stopping structural energy minimisation\n'
    finished_dirs = []
    for check in check_list:
        printout = os.path.abspath(os.path.join(check, 'print-out'))
        with open(printout, 'r') as f:
            content = f.readlines()
            if content[-1] == finish_flag:
                finished_dirs.append(os.path.dirname(check))
    return finished_dirs

if __name__ == '__main__':
    print()
