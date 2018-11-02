#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: VisPerLas.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 四 11/ 1 23:01:45 2018
#########################################################################
'System'
import os

import numpy as np
from scipy import interpolate

'Plot'
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from DataOperators import pltsave

def GetAN(out):
    'Get Positive Numbers'
    Ns = []
    f = os.popen('grep \'N_\' ' + out)
    for line in f.readlines():
        line = line.strip('\n')
        Ns.append(int(line.split(' ')[4]))

    'Get Alphas'
    alphas = []
    f = os.popen('grep \'BestAlpha\' ' + out)
    for line in f.readlines():
        line = line.strip('\n')
        alphas.append(float(line.split(' ')[4]))

    'Get BestAlpha'
    BestAlpha = 0
    f = os.popen('grep \'Selected\' ' + out)
    for line in f.readlines():
        line = line.strip('\n')
        BestAlpha = float(line.split(' ')[4])

    a_n = {}
    for a, N in zip(alphas, Ns):
        a_n[a] = N
    
    BestN = a_n[BestAlpha]

    a_n_tuple = sorted(a_n.items(), key= lambda d:d[0])

    x = []
    y = []
    for t in a_n_tuple:
        x.append(t[0])
        y.append(t[1])

    x = np.array(x)
    y = np.array(y)

    x_new = np.linspace(x.min(), x.max(), 200)
    smooth = interpolate.interp1d(x, y, kind = 3)
    y_smooth = smooth(x_new)

    return BestAlpha, BestN, alphas, Ns, x, y, x_new, y_smooth

def PltCurve(outs):
    a, n, alphas, Ns, x, y, x_s, y_s = GetAN(outs)

    plt.figure(figsize=(16,6))
    plt.tight_layout(pad=2.0, w_pad=2.0, h_pad=2.0)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, \
            wspace=None, hspace=0.4)

    plt.suptitle('LASSO for Surface Pathway', fontsize=16)

    'Learning Curve'
    ax1 = plt.subplot(121)
    ax1.set_title('Number of Nonzero Coefficient v.s. Alpha')
    ax1.set_xlabel('${alpha}$')
    ax1.set_ylabel('Number')
    ax1.set_xlim(0, max(alphas)+0.01)
    ax1.set_ylim(0, max(Ns)+1)
    ax1.scatter(x, y, edgecolor=(0,0,0))
    ax1.plot(x_s, y_s)

    ax1.plot([a,]*2, [0, n], linestyle='-.', color='b', marker='x')
    ax1.text(0.10,70, 'alpha=%0.3f, n=%d' %(a, n))

    'alphas'
    ax2 = plt.subplot(222)
    ax2.set_title('Hist for Alphas', fontsize=10)
    ax2.set_xlabel('${alpha}$', fontsize=10)
    ax2.set_ylabel('Frequency', fontsize=10)
    ax2.hist(alphas)

    'Ns'
    ax3 = plt.subplot(224)
    ax3.set_title('Hist for Numbers', fontsize=10)
    ax3.set_xlabel('Number of Nonzero Coefficient', fontsize=10)
    ax3.set_ylabel('Frequency', fontsize=10)
    ax3.hist(Ns)

    pltsave('PerLas_'+outs+'.png')

if __name__ == '__main__':
    PltCurve('Ets1pppp')
