#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os

import numpy as np
from scipy import interpolate

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


"""
Paper figure 4.
"""


def get_training_info(out):
    # get the number of positive coefficients 
    Ns = []
    f = os.popen('grep \'N_\' ' + out)
    for line in f.readlines():
        line = line.strip('\n')
        Ns.append(int(line.split(' ')[3]))

    # get alphas 
    alphas = []
    f = os.popen('grep \'BestAlpha:\' ' + out)
    for line in f.readlines():
        line = line.strip('\n')
        alphas.append(float(line.split(' ')[3]))

    # get the best alpha 
    BestAlpha = 0
    f = os.popen('grep \'Selected A\' ' + out)
    for line in f.readlines():
        line = line.strip('\n')
        BestAlpha = float(line.split(' ')[3])

    # get the best theta 
    BestTheta = 0
    f = os.popen('grep \'Best Theta\' ' + out)
    for line in f.readlines():
        line = line.strip('\n')
        BestTheta = float(line.split(' ')[3])

    # !!
    a_n = {}
    for a, N in zip(alphas, Ns):
        a_n[a] = N

    a_n_tuple = sorted(a_n.items(), key= lambda d:d[0])

    x, y = [], [] 
    for t in a_n_tuple:
        x.append(t[0])
        y.append(t[1])

    x, y = np.array(x), np.array(y)

    x_new = np.linspace(x.min(), x.max(), 200)
    smooth = interpolate.interp1d(x, y, kind = 3)
    y_smooth = smooth(x_new)

    BestN = int(smooth(BestAlpha))

    return BestAlpha, BestTheta, BestN, alphas, Ns, x, y, x_new, y_smooth


def PltCurve():
    """"""
    # figure general setting 
    plt.figure(figsize=(16,9))
    #plt.tight_layout(pad=1.0, w_pad=1.0, h_pad=1.0)
    plt.tight_layout()
    plt.subplots_adjust(left=0.1, bottom=0.08, right=0.9, top=0.88, \
            wspace=None, hspace=10)

    plt.suptitle('Percentile-LASSO Training Process', \
            fontsize=24, fontweight='bold')

    # subfigures grid 
    gs = GridSpec(22, 2)

    # get related training information 
    ts = '../percentile_lasso_versions/Ets_100_500_11_new'
    a, c, n, alphas, Ns, x, y, x_s, y_s = get_training_info(ts)

    # Learning Curve 
    ax1 = plt.subplot(gs[0:10, 0])
    ax1.text(0.03, 18, '(a) Surface-stabilized Mechanism', \
            fontsize=20, fontweight='normal')

    ax1.set_title(r'Number of Nonzero Coefficients v.s. $\alpha$', fontsize=16)
    ax1.set_xlabel(r'$\alpha$', fontsize=16)
    ax1.set_ylabel('Number of Nonzero Coefficients (n)', fontsize=16)
    #ax1.set_xlim(0, max(alphas)+0.01)
    #ax1.set_ylim(0, max(Ns)+1)
    ax1.set_xlim(0, 0.05)
    ax1.set_ylim(0, 16)
    ax1.scatter(x, y, edgecolor=(0,0,0))
    ax1.plot(x, y) ###

    ax1.plot([a,]*2, [0, n], linestyle='-.', color='b', marker='x')
    ax1.text(a,n+1.5, r'$\alpha$=%0.3f' %a+'\n'+r'$\theta$=%d' %(c*100)+'\nn=%d' %n)

    # alpha histogram 
    ax2 = plt.subplot(gs[0:4, 1])
    ax2.set_title(r'Histogram for $\alpha$ with 100 Times Training', fontsize=16)
    ax2.set_xlabel(r'$\alpha$', fontsize=16)
    ax2.set_xlim(0, 0.05)
    ax2.set_ylabel('Frequency', fontsize=16)
    ax2.set_ylim(0, 60)
    ax2.hist(alphas)

    # number of coefficients histogram 
    ax3 = plt.subplot(gs[6:10, 1])
    ax3.set_title('Histogram for Numbers with 100 Times Training', fontsize=16)
    ax3.set_xlabel('Number of Nonzero Coefficients (n)', fontsize=16)
    ax3.set_xlim(0, 20)
    ax3.set_ylabel('Frequency', fontsize=16)
    ax3.set_ylim(0, 60)
    ax3.hist(Ns)
    
    # tsra
    tsra = '../percentile_lasso_versions/Etsra_100_500_11_new'
    a, c, n, alphas, Ns, x, y, x_s, y_s = get_training_info(tsra)

    # Learning Curve 
    ax1 = plt.subplot(gs[12:22, 0])
    #ax1.suptitle('(a) ', fontsize=20)
    ax1.text(0.10, 18, '(b) Radical-like Mechanism', \
            fontsize=20, fontweight='normal')

    ax1.set_title(r'Number of Nonzero Coefficients v.s. $\alpha$', fontsize=16)
    ax1.set_xlabel(r'$\alpha$', fontsize=16)
    ax1.set_ylabel('Number of Nonzero Coefficients (n)', fontsize=16)
    #ax1.set_xlim(0, max(alphas)+0.01)
    #ax1.set_ylim(0, max(Ns)+1)
    ax1.set_xlim(0, 0.15)
    ax1.set_ylim(0, 16)
    ax1.scatter(x, y, edgecolor=(0,0,0))
    ax1.plot(x, y) ###

    #n = 5
    ax1.plot([a,]*2, [0, n], linestyle='-.', color='b', marker='x')
    ax1.text(a,n+2, r'$\alpha$=%0.3f' %a+'\n'+r'$\theta$=%d' %(c*100)+'\nn=%d' %n)

    # alpha histogram 
    ax2 = plt.subplot(gs[12:16, 1])
    ax2.set_title(r'Histogram for $\alpha$ with 100 Times Training', fontsize=16)
    ax2.set_xlabel(r'$\alpha$', fontsize=16)
    ax2.set_xlim(0, 0.15)
    ax2.set_ylabel('Frequency', fontsize=16)
    ax2.set_ylim(0, 60)
    ax2.hist(alphas)

    # number of coefficients histogram 
    ax3 = plt.subplot(gs[18:22, 1])
    ax3.set_title('Histogram for Numbers with 100 Times Training', fontsize=16)
    ax3.set_xlabel('Number of Nonzero Coefficients (n)', fontsize=16)
    ax3.set_xlim(0, 20)
    ax3.set_ylabel('Frequency', fontsize=16)
    ax3.set_ylim(0, 60)
    ax3.hist(Ns)

    #plt.show()
    plt.savefig('./figures/fig5.png')


if __name__ == '__main__':
    PltCurve()
