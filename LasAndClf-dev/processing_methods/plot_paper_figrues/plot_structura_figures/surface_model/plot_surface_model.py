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
paper figure 1. 
structure file, surface_model.con
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


def plot_surface():
    """paper fig 1"""
    abc, new_xyzs = get_structure_from_contcar('./cons/surface_model.con', 48)

    rutile = Atoms('O32Ir15Ge', positions=new_xyzs, cell=abc, pbc=[0, 0, 0])

    fig, axarr = plt.subplots(1, 2, figsize=(12, 6))
    plt.suptitle('(110) Surface Model of Rutile-type Metal Oxides', \
            fontsize=20, fontweight='bold')

    # fig a 
    axarr[0].set_title('(a) Over View', fontsize=16, fontweight='normal')
    axarr[0].set_axis_off()

    plot_atoms(rutile, axarr[0], rotation=('0x,0y,270z'))
    axarr[0].text(1.5,3, '$O_{br}$', fontsize=16)
    axarr[0].text(4.5,3, '$M_{cus}$', fontsize=16)

    # fig b 
    axarr[1].set_title('(b) Side View', fontsize=16, fontweight='normal')
    axarr[1].set_axis_off()

    plot_atoms(rutile, axarr[1], rotation=('0x,270y,270z'))

    # plot symbols 
    symbols = ['Ir', 'O', 'Ge']
    names = ['Base', 'Oxygen', 'Dopant']
    lefts = [0.40, 0.50, 0.60]
    for i, left in enumerate(lefts):
        # set subfigure location 
        ax3 = fig.add_axes([left, 0.05, 0.05, 0.05])
        atom = Atoms(symbols[i], positions=[[0, 0, 0]])
        # plot atoms 
        plot_atoms(atom, ax3, rotation=('0x,0y,0z'))

        ax3.set_title(names[i], fontsize=12)
        ax3.set_axis_off()

    fig.savefig("fig1.png")
    #plt.show()


if __name__ == '__main__':
    plot_surface()
