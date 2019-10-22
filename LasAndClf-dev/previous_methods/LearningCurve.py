#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: LearningCurve.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 四 10/11 14:09:19 2018
#########################################################################
import sys
import time
### plot
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  
'sklearn'
import numpy as np
import pandas as pd
''
import pickle
### mylibs
sys.path.append('..')
import decorates as deco
from DataOperators import pkload
from DataOperators import pltsave

def plt_cv():
    'Load Pickle'
    print('Loading Pickle...')
    gslas = pkload('las_Ea.pk')

    'Get Results'
    results = gslas.cv_results_
    scoring = gslas.scorer_

#def additional():
    'Plt Learning Curve'
    print('Plotting Learning Curve...')
    plt.figure(figsize=(12, 8)) # figsize in inch, 1inch=2.54cm
    plt.title("GridSearchCV for LASSO",fontsize=16)
    plt.xlabel("Alpha")

    # Get the regular numpy array from the MaskedArray
    X_axis = np.array(results['param_alpha'].data, dtype=float)
    ax = plt.gca()

    'R2'
    scorer='R2'; color='g'
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_ylabel('R2')
    for sample, style in (('train', '--'), ('test', '-')): # sample
        sample_score_mean = results['mean_%s_%s' % (sample, scorer)] # score mean
        sample_score_std = results['std_%s_%s' % (sample, scorer)] # score std
        
        ax.fill_between(X_axis, sample_score_mean - sample_score_std, \
                sample_score_mean + sample_score_std, \
                alpha=0.1 if sample == 'test' else 0, color=color)
        ax.plot(X_axis, sample_score_mean, style, color=color, \
                alpha=1 if sample == 'test' else 0.7, \
                label="%s (%s)" % (scorer, sample))
    
    best_index = np.nonzero(results['rank_test_%s' % scorer] == 1)[0][0]
    best_score = results['mean_test_%s' % scorer][best_index]
    
    # Plot a dotted vertical line at the best score for that scorer marked by x
    ax.plot([X_axis[best_index], ] * 2, [0, best_score],
            linestyle='-.', color=color, marker='x', markeredgewidth=3, ms=8)

    # Annotate the best score for that scorer
    ax.annotate("%0.2f" % best_score, \
            (X_axis[best_index], best_score + 0.005))

    ax.legend(loc=2)

    'MSE'
    scorer='MSE'; color='k'
    ax2 = ax.twinx()
    ax2.set_xlim(0,1)
    ax2.set_ylim(-1,2)
    ax2.set_ylabel('MSE')
    for sample, style in (('train', '--'), ('test', '-')): # sample
        sample_score_mean = results['mean_%s_%s' % (sample, scorer)] # score mean
        sample_score_std = results['std_%s_%s' % (sample, scorer)] # score std
        
        ax2.fill_between(X_axis, sample_score_mean - sample_score_std, \
                sample_score_mean + sample_score_std, \
                alpha=0.1 if sample == 'test' else 0, color=color)
        ax2.plot(X_axis, sample_score_mean, style, color=color, \
                alpha=1 if sample == 'test' else 0.7, \
                label="%s (%s)" % (scorer, sample))
    
    best_index = np.nonzero(results['rank_test_%s' % scorer] == 1)[0][0]
    best_score = results['mean_test_%s' % scorer][best_index]

    # Plot a dotted vertical line at the best score for that scorer marked by x
    ax2.plot([X_axis[best_index], ] * 2, [0, best_score],
            linestyle='-.', color=color, marker='x', markeredgewidth=3, ms=8)
    
    # Annotate the best score for that scorer
    ax2.annotate("%0.2f" % best_score, \
            (X_axis[best_index], best_score + 0.005))

    ax2.legend(loc=1)

    '' 
    plt.grid("off")
    pltsave('LearnCurve.png')

if __name__ == '__main__':
    plt_cv()
