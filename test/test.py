#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: test.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 三  3/14 22:00:05 2018
#########################################################################
import os 
import re
###
with open('./haha', 'r') as f:
    finish = f.readlines()
#
finish_dirs = []
#
for i in range(len(finish)):
    finish_dir = finish[i].split(' ')[0]
    if re.match(r'^dop.*', finish_dir):
        finish_dirs.append(finish_dir)
print(finish_dirs)
