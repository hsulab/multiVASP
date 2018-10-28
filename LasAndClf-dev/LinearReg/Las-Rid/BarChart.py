#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: BarChart.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六 10/27 22:15:02 2018
#########################################################################
'Plot'
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import pickle
from DataOperators import pkload

def plt_bar():
    ''
    feas, best_feas, best_coefs, meanMSEs, stdMSEs = pkload('BestReg-test.pk')

    'Plot the best feas'
    x = range(len(best_feas))
    fig, ax = plt.subplots()
    plt.bar(x, best_coefs)
    plt.xticks(x, best_feas)
    plt.show()

if __name__ == '__main__':
    plt_bar()
