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
with open('./CONTCAR', 'r') as f:
    contcar = f.readlines()
#
new_content = ''
for line in contcar[9:62]:
    new_line = []
    line = line.strip('\n').split(' ')
    for i in line:
        if i != '':
            new_line.append(i)
    new_content += '{:>20}{:>20}{:>20}  T  T  T\n'.format(new_line[0], new_line[1], new_line[2])
print(new_content)
