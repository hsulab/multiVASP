#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: test.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 三  3/14 22:00:05 2018
#########################################################################
import os 
f = os.popen('grep sadasdasdadas OUTCAR')
print(f.readlines())
