#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: multiResult.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 日  4/ 1 00:00:41 2018
#########################################################################
import os 
import datetime
import re
###
def find_multiVASP():
    user_home = os.path.expanduser('~')
    multiVASP_pattern = re.compile('.*multiVASP')
    for root, dirs, files in os.walk(user_home):
        if multiVASP_pattern.match(root):
            if os.path.isdir(root):
                return root
                break
            else:
                print(r'No multiVASP in HOME.')
                break
###
def init_logdir(multiVASP_dir):
    logdir = os.path.join(multiVASP_dir, '.multiResult')
    if not os.path.exists(logdir):
        os.mkdir(logdir)

###
def main():
    workTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    multiVASP_dir = find_multiVASP()
    init_logdir(multiVASP_dir)


###
if __name__ == "__main__":
    main()
