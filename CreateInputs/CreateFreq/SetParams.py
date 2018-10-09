#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: SetParams.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 日  3/18 19:45:53 2018
#########################################################################
import re
import sys
### IBRION= 2
def set_param(inputfile, para, value):
    new_inputfile = ''
    with open(inputfile, 'r') as f:
        for line in f:
            if re.match(r'^%s.*' %(para), line):
                line = '%s' %(value)
            new_inputfile += line
    with open(inputfile, 'w') as f:
        f.write(new_inputfile)
###
if __name__ == '__main__':
    if len(sys.argv) == 1:
        INCAR = r'./TestFile/INCAR'
        set_param(INCAR, 'IBRION', 'IBRION=0.015\nNFREE=2\n')
    elif len(sys.argv) == 2:
        INCARfile = sys.argv[1]
    else:
        print('INCAR file is wrong!')

