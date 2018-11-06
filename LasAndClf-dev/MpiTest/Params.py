#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: Params.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 二 11/ 6 10:53:14 2018
#########################################################################
import numpy as np

Etype = 'Etsra'
'''
total feastures 6662
Important Parameters:
--> splits, repeats, test_alphas
cv_splits = 5; cv_repeats = 5
test_alphas = np.linspace(0.01, 0.1, 10)
'''
cv_splits = 2; cv_repeats = 5
test_alphas = np.linspace(0.01, 0.05, 5)

'''
Important Params
--> test_thetas
Etype = 'Etsra'
test_thetas = np.linspace(0.50, 1, 11)
cv_splits = 5; cv_repeats = 1
'''
tcv_splits = 5; tcv_repeats = 1
test_thetas = np.linspace(0.50, 1, 11)
