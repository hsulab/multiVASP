#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
import random 

import numpy as np
import pandas as pd

from sklearn import metrics
from sklearn.linear_model import LinearRegression

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def plt_alphas():
    # figure general setting 
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8,8))
    #plt.tight_layout(pad=2.0, w_pad=2.0, h_pad=2.0)
    #plt.subplots_adjust(left=0.1, bottom=0.1, right=0.95, top=0.9, \
            #wspace=0.3, hspace=0.3)

    ax.set_title('Number of Nonzero Features v.s. Alpha', fontsize=20, fontweight='bold')

    ax.set_xlim(0, 2.5)
    ax.set_xlabel(r'$\hat{\alpha}$', fontsize=14)

    ax.set_ylim(0, 80)
    ax.set_ylabel('Number of Nonzero Features', fontsize=14)

    # fuction for plt 
    alphas = np.arange(0.3, 2.1, 0.1)
    nfeas = [] 
    for alpha in alphas:
        nfeas.append(20/alpha + random.randint(-2,2))

    ax.plot(alphas, nfeas, label='False Nonzero')

    ax.plot([1.2]*70, np.arange(5,75,1), linestyle='--', label='50 Percentile')
    ax.plot([1.7]*70, np.arange(5,75,1), linestyle='--', label='75 Percentile')

    ax.plot(np.arange(0.2,2.2,0.1), [8]*20, color='r', linestyle='--', label='True Nonzero')

    plt.legend()
    
    #plt.show()
    plt.savefig('./figures/figs1.png')


if __name__ == '__main__':
    plt_alphas()
