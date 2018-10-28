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
sys.path.append('../..')
import decorates as deco
###
def load_GsLas():
    'Load Pickle'
    print('Loading Pickle...')
    with open('./Log/GsLas.pk', 'rb') as f:
        GsLas = pickle.load(f)

    'Prepare Results'
    Gs_results = GsLas.cv_results_
    Gs_results['scorers'] = GsLas.scorer_
    return Gs_results

def plt_GsLas():
    'Get Results'
    results = load_GsLas()
    'Plt Learning Curve'
    print('Plotting Learning Curve...')
    plt.figure(figsize=(4, 4)) # figsize in inch, 1inch=2.54cm
    plt.title("GridSearchCV for Lasso",fontsize=16)
    plt.xlabel("Alpha")
    plt.ylabel("Score")
    ''
    ax = plt.gca()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    # Get the regular numpy array from the MaskedArray
    X_axis = np.array(results['param_alpha'].data, dtype=float)
    ''
    for scorer, color in zip(sorted(results['scorers']), ['g', 'k']): # scorer
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
        ax.plot([X_axis[best_index], ] * 2, [0, best_score], \
                linestyle='-.', color=color, marker='x', markeredgewidth=3, ms=8)
    
        # Annotate the best score for that scorer
        ax.annotate("%0.2f" % best_score, \
                (X_axis[best_index], best_score + 0.005))
    '' 
    plt.legend(loc="best")
    plt.grid("off")
    plt.savefig('./Log/LearnCurve.png', tight='bbox')

if __name__ == '__main__':
    plt_GsLas()
