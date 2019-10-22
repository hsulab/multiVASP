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
paper figure 3.
structure file, Hab2, Hab3, CH3ab, CH3ab2.
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
    

def plot_adsorptions():
    """paper fig 2"""
    # read H contcars 
    abc, new_xyzs = get_structure_from_contcar('./cons/Hab2.con', 49)
    hab2 = Atoms('HO32Ir15Ge', positions=new_xyzs, cell=abc, pbc=[0, 0, 0])

    abc, new_xyzs = get_structure_from_contcar('./cons/Hab3.con', 49)
    hab3 = Atoms('HO32Ir15Ge', positions=new_xyzs, cell=abc, pbc=[0, 0, 0])

    # read CH3 contcars 
    abc, new_xyzs = get_structure_from_contcar('./cons/CH3ab.con', 52)
    ch3ab = Atoms('H3CO32Ir15Ge', positions=new_xyzs, cell=abc, pbc=[0, 0, 0])

    abc, new_xyzs = get_structure_from_contcar('./cons/CH3ab2.con', 52)
    ch3ab2 = Atoms('H3CO32Ir15Ge', positions=new_xyzs, cell=abc, pbc=[0, 0, 0])

    # figure general setting 
    fig, axarr = plt.subplots(2, 4, figsize=(16, 8))
    plt.tight_layout(pad=2.0, w_pad=2.0, h_pad=2.0)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=0.85, \
            wspace=None, hspace=0.2)

    plt.suptitle(r'Adsorption Conformations of H and $\bf{CH_3}$', \
            fontsize=20, fontweight='bold')

    plt.text(-50, 35, r'(a) Adsorption of ${H}$', fontsize=16, fontweight='normal')
    plt.text(-15, 35, r'(b) Adsorption of ${CH_3}$', fontsize=16, fontweight='normal')

    # plot H atoms 
    plot_atoms(hab2, axarr[0][0], rotation=('0x,0y,270z'))
    axarr[0][0].set_title(' Over View of On-Top Position ($sp^2$) ', fontsize=12)
    axarr[0][0].set_axis_off()

    plot_atoms(hab2, axarr[0][1], rotation=('0x,270y,270z'))
    axarr[0][1].set_title(' Side View of On-Top Position ($sp^2$) ', fontsize=12)
    axarr[0][1].set_axis_off()

    plot_atoms(hab3, axarr[1][0], rotation=('0x,0y,270z'))
    axarr[1][0].set_title(' Side View of Inclined Position ($sp^3$) ', fontsize=12)
    axarr[1][0].set_axis_off()

    plot_atoms(hab3, axarr[1][1], rotation=('0x,270y,270z'))
    axarr[1][1].set_title(' Side View of Inclined Position ($sp^3$) ', fontsize=12)
    axarr[1][1].set_axis_off()

    # plot CH3 atoms 
    plot_atoms(ch3ab, axarr[0][2], rotation=('0x,270y,135z'))
    axarr[0][2].set_title(' Over View of Vertical Position ', fontsize=12)
    axarr[0][2].set_axis_off()

    plot_atoms(ch3ab, axarr[0][3], rotation=('45x,0y,90z'))
    axarr[0][3].set_title(' Side View of Vertical Position ', fontsize=12)
    axarr[0][3].set_axis_off()

    plot_atoms(ch3ab2, axarr[1][2], rotation=('0x,0y,270z'))
    axarr[1][2].set_title(' Side View of Parallel Position ', fontsize=12)
    axarr[1][2].set_axis_off()

    plot_atoms(ch3ab2, axarr[1][3], rotation=('0x,270y,270z'))
    axarr[1][3].set_title(' Side View of Parallel Position ', fontsize=12)
    axarr[1][3].set_axis_off()

    # plot symbols 
    symbols = ['C', 'H', 'O', 'Ir', 'Ge']
    names = ['Carbon', 'Hydrogen', 'Oxygen', 'Base', 'Dopant']
    lefts = [0.30, 0.40, 0.50, 0.60, 0.70]
    for i, left in enumerate(lefts):
        # set subfigure location 
        ax3 = fig.add_axes([left, -0.00, 0.04, 0.04])
        atom = Atoms(symbols[i], positions=[[0, 0, 0]])
        # plot atoms 
        plot_atoms(atom, ax3, rotation=('0x,0y,0z'))

        ax3.set_title(names[i], fontsize=12)
        ax3.set_axis_off()

    #plt.show()
    plt.savefig('../figures/fig2.png')


if __name__ == '__main__':
    plot_adsorptions()
