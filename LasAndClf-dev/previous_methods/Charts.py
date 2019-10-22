#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

''
import math
import numpy as np

'Plot'
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

'MyLibs'
import pickle
from DataOperators import pkload
from DataOperators import pltsave

def plt_bep():
    print('Plotting...')
    fig, ((ax1, ax2, ax5), (ax3, ax4, ax6)) = plt.subplots(nrows=2, ncols=3, figsize=(12,8))
    plt.suptitle('BEP for Methane Activation')
    plt.tight_layout(pad=2.0, w_pad=2.0, h_pad=2.0)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=0.9, \
            wspace=None, hspace=0.2)

    y, y_p, r2, mse = pkload('ts_Hab2_CH3ab.pk')
    ax1.set_title('(a) $E_{H^{{sp}^2}} + E_{{{CH}_3}^v}$')
    ax1.scatter(y, y_p, edgecolors=(0, 0, 0))
    ax1.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    ax1.text(-0.5,1, '${R^2}$=%0.2f, MSE=%0.2f' %(r2, mse))
    
    y, y_p, r2, mse = pkload('ts_Hab2_CH3ab2.pk')
    ax2.set_title('(b) $E_{H^{{sp}^2}} + E_{{{CH}_3}^p}$')
    ax2.scatter(y, y_p, edgecolors=(0, 0, 0))
    ax2.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    ax2.text(-0.5,1, '${R^2}$=%0.2f, MSE=%0.2f' %(r2, mse))
    
    y, y_p, r2, mse = pkload('ts_Hab3_CH3ab.pk')
    ax3.set_title('(c) $E_{H^{{sp}^3}} + E_{{{CH}_3}^v}$')
    ax3.scatter(y, y_p, edgecolors=(0, 0, 0))
    ax3.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    ax3.text(-0.5,1, '${R^2}$=%0.2f, MSE=%0.2f' %(r2, mse))
    
    y, y_p, r2, mse = pkload('ts_Hab3_CH3ab2.pk')
    ax4.set_title('(d) $E_{H^{{sp}^3}} + E_{{{CH}_3}^p}$')
    ax4.scatter(y, y_p, edgecolors=(0, 0, 0))
    ax4.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    ax4.text(-0.5,1, '${R^2}$=%0.2f, MSE=%0.2f' %(r2, mse))
    
    y, y_p, r2, mse = pkload('tsra_Hab2.pk')
    ax5.set_title('(e) $E_{H^{{sp}^2}}$')
    ax5.scatter(y, y_p, edgecolors=(0, 0, 0))
    ax5.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    ax5.text(0.4,1.4, '${R^2}$=%0.2f, MSE=%0.2f' %(r2, mse))

    y, y_p, r2, mse = pkload('tsra_Hab3.pk')
    ax6.set_title('(f) $E_{H^{{sp}^3}}$')
    ax6.scatter(y, y_p, edgecolors=(0, 0, 0))
    ax6.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    ax6.text(0.4,1.4, '${R^2}$=%0.2f, MSE=%0.2f' %(r2, mse))

    #plt.show()
    pltsave('bep.png')

    print('Success...')

def plt_bar():
    ''
    feas, best_feas, best_coefs, meanMSEs, stdMSEs = pkload('BestReg-test.pk')

    'Plot the best feas'
    x = range(len(best_feas))
    fig, ax = plt.subplots()
    plt.bar(x, best_coefs)
    plt.xticks(x, best_feas)
    plt.show()

def plt_hist(pkfile):
    ''
    params, nc = pkload(pkfile) # nc - name_coef

    'Hist'
    coef_max, coef_min = max(nc.values()), min(nc.values())
    up = math.ceil(coef_max*100)/100.0
    if coef_min <= 0:
        down = math.ceil(coef_min*-100)/-100.0
    else:
        down = math.ceil(coef_min*-100)/-100.0

    print('Preparing Hist...')
    fig, ax = plt.subplots()
    plt.title('Coefficient Count '+str(len(nc.keys()))+' in total')
    plt.xlabel('Coefficient')
    plt.ylabel('Number')

    ''
    ax.hist(nc.values(), bins=np.arange(down, up+0.1*up, (up-down)/5))
    counts, edges = np.histogram(list(nc.values()), bins=5)
    ax.set_xticks(np.arange(down, up+0.1*up, (up-down)/5))
    ax.set_xlim(down, up)
    ax.set_yticks(np.arange(0,max(counts)+2,2))

    print('Save fig...')
    pltsave(pkfile.split('.')[0]+'.png')

    print('Success...')

def plt_curve(pkfile):
    'Load pk'
    feas, best_feas, mean_MSEs, std_MSEs = pkload(pkfile)
    print(best_feas)

    'Plt Learning Curve'
    print('Plotting Learning Curve...')
    plt.title('Feature Selection from LASSO '+\
            pkfile.split('.')[0].split('_')[2],fontsize=16)
    plt.xlabel('Number of Feature Used')
    plt.ylabel('Mean MSE')

    ''
    ax = plt.gca()
    x = range(1,len(feas.keys())+1)
    ax.set_xlim(0, len(x)+1)
    ax.set_xticks(np.arange(0, len(x)+1, 2))
    ax.set_ylim(0, max(mean_MSEs)*1.1)
    ax.set_yticks(np.arange(0, max(mean_MSEs)*1.1, 0.5))
    ax.plot(x, mean_MSEs)

    'Plot best_index'
    best_score = min(mean_MSEs)
    best_index = mean_MSEs.index(best_score)
    
    # Plot a dotted vertical line at the best score for that scorer marked by x
    ax.plot([x[best_index], ] * 2, [0, best_score], \
            linestyle='-.', color='b', marker='x', markeredgewidth=3, ms=8)
    
    # Annotate the best score for that scorer
    ax.annotate("%0.2f" % best_score, (x[best_index], best_score + 0.005))

    print('Saving fig...')
    pltsave(pkfile.split('.')[0]+'.png')

    print('Success...')

def main():
    #plt_curve('Best_las_Ea.pk')
    plt_bep()

if __name__ == '__main__':
    main()
