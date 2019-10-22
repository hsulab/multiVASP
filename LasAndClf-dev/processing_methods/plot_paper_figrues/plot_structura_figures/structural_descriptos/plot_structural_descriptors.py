#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from ase.visualize import view
from ase.visualize.plot import plot_atoms
from ase import Atoms


"""
paper figure 7.
"""


def get_structure_from_contcar(confile, n):
    """""" 
    # read contcar 
    with open(confile, 'r') as f:
        content = f.readlines()

    # abc 
    abc = []
    for line in content[2:5]:
        line = line.strip('\n').split(' ')
        v = []
        for i in line:
            if i != '':
                v.append(round(float(i),2))
        abc.append(v)
    abc = np.array(abc)

    # xyzs 
    xyzs = []
    for line in content[9:9+n]:
        line = line.strip('\n').split(' ')
        xyz = []
        for i in line:
            if i not in ['', 'T', 'F']:
                xyz.append(round(float(i),4))
        xyzs.append(np.array(xyz))
    xyzs = np.array(xyzs)

    new_xyzs = []
    for xyz in xyzs:
        xyz_abs = (abc.T*xyz).T.sum(0)
        x = xyz_abs[2]
        y = (xyz_abs[0]/(2**0.5)-xyz_abs[1]/(2**0.5))
        z = (xyz_abs[0]/(2**0.5)+xyz_abs[1]/(2**0.5))
        new_xyzs.append([x, y, z])

    a = np.linalg.norm(abc[0])
    b = np.linalg.norm(abc[1])
    c = np.linalg.norm(abc[2])

    return [a,b,c], new_xyzs

"""
M_cus = [1.5, 3.5]
O_br = [3, 5]
"""

def plot_had(ax, feaname, atoms):
    abc, new_xyzs = get_structure_from_contcar('./cons/h_ad_suf.con', 11)
    hab3 = Atoms('H1O6Ir3Ge', positions=new_xyzs, cell=abc, pbc=[0, 0, 0])

    plot_atoms(hab3, ax, rotation=('30x,-30y,90z'))

    ax.text(2, 6, feaname, fontsize=16)

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)

    # plot dots and lines 
    xs, ys = [], [] 
    for atom in atoms:
        xs.append(atom[0])
        ys.append(atom[1])

    ax.plot(xs, ys, 'k-.', lw=2)
    ax.scatter(xs, ys, color='k', zorder=10)

    ax.set_axis_off() 
        
    if len(atoms) in [3]:
        ax.arrow(atoms[0][0], atoms[0][1], \
                0.15*(atoms[2][0]-atoms[0][0]), \
                0.15*(atoms[2][1]-atoms[0][1]), \
                head_width=0.15, fc='k')

        ax.arrow(atoms[2][0], atoms[2][1], \
                0.15*(atoms[0][0]-atoms[2][0]), \
                0.15*(atoms[0][1]-atoms[2][1]), \
                head_width=0.15, fc='k')



def plot_ch3ad(ax, feaname, atoms):
    """"""
    abc, new_xyzs = get_structure_from_contcar('./cons/ch3_ad_suf.con', 14)
    hab3 = Atoms('H3C1O6Ir3Ge', positions=new_xyzs, cell=abc, pbc=[0, 0, 0])

    plot_atoms(hab3, ax, rotation=('30x,-30y,90z'))

    ax.text(2, 6, feaname, fontsize=16)

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)

    # plot dots and lines 
    xs, ys = [], [] 
    for atom in atoms:
        xs.append(atom[0])
        ys.append(atom[1])

    ax.scatter(xs, ys, color='k', zorder=10)
    ax.plot(xs, ys, 'k-.', lw=2)

    if len(atoms) == 4:
        ax.plot([atoms[0][0], atoms[3][0], atoms[1][0]], \
                [atoms[0][1], atoms[3][1], atoms[1][1]], \
                'k-.', lw=2)

    if len(atoms) in [3, 4]:
        ax.arrow(atoms[0][0], atoms[0][1], \
                0.25*(atoms[2][0]-atoms[0][0]), \
                0.25*(atoms[2][1]-atoms[0][1]), \
                head_width=0.25, fc='k')

        ax.arrow(atoms[2][0], atoms[2][1], \
                0.25*(atoms[0][0]-atoms[2][0]), \
                0.25*(atoms[0][1]-atoms[2][1]), \
                head_width=0.25, fc='k')

    ax.set_axis_off() 


def plot_structural_descriptors():
    """"""
    # figure general setting 
    fig, axarr = plt.subplots(2, 3, figsize=(16, 9))

    plt.tight_layout(pad=2.0, w_pad=2.0, h_pad=2.0)
    plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, \
            wspace=0.1, hspace=0.1)

    plt.suptitle('Selected Structural Descriptors for the Surface-stabilized Pathway', \
            fontsize=20, fontweight='bold')

    M_cus = [5, 2]
    O_br = [2, 3.5]
    H_ch3 = [4, 4.2]
    H_h = [2.5, 4.0]
    C = [4.8, 4.0]

    # 1 angle 
    plot_ch3ad(axarr[0][0], '(a) $A_{O_{br}-M_{cus}-C}^{CH_3^*}$ (0.41)', \
            [O_br, M_cus, C])

    # 2 distance 
    plot_ch3ad(axarr[0][1], '(b) $D_{H-C}^{CH_3^*}$ (-0.32)', \
            [H_ch3, C])

    # 3 dihedral 
    plot_ch3ad(axarr[0][2], '(c) $H_{O_{br}-C-M_{cus}-H}^{CH_3^*}$ (0.30)', \
            [O_br, H_ch3, C, M_cus]) # 1423, 431

    # 4 dihedral 
    plot_ch3ad(axarr[1][0], '(d) $H_{O_{br}-H-M_{cus}-C}^{CH_3^*}$ (-0.29)', \
            [O_br, C, H_ch3, M_cus])

    # 5 angle 
    plot_had(axarr[1][1], '(e) $A_{O_{br}-M_{cus}-H}^{H^*}$ (-0.24)', \
            [O_br, M_cus, H_h])

    # 6 
    ax6 = axarr[1][2] 
    ax6.set_axis_off()

    # plot symbols 
    symbols = ['C', 'H', 'O', 'Ir', 'Ge']
    names = ['Carbon', 'Hydrogen', 'Oxygen', 'Base', 'Dopant']
    lefts = np.arange(0.7, 0.9, 0.05)
    for i, left in enumerate(lefts):
        # set subfigure location 
        ax = fig.add_axes([left, 0.2, 0.04, 0.04]) # left, bottom, width, height 
        atom = Atoms(symbols[i], positions=[[0, 0, 0]])

        # plot atoms 
        plot_atoms(atom, ax, rotation=('0x,0y,0z'))

        ax.set_title(names[i], fontsize=12)
        ax.set_axis_off()

    fig.savefig("fig6.png")
    #plt.show()


if __name__ == '__main__':
    plot_structural_descriptors()
