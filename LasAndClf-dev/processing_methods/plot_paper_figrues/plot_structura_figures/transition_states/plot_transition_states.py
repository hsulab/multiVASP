#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import os 

import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.image import imread 

from ase import Atoms

from ase.visualize import view
from ase.io import read, write 

"""
paper figure 1.
"""


def write_transition_png(atoms, rot, povname):
    # running index for the bonds 
    bondatoms = []
    symbols = atoms.get_chemical_symbols()

    def check_bonding(atom1, atom2, symbol1, symbol2, distance, bond_dis):
        if ((atom1 == symbol1 and atom2 == symbol2) or \
                (atom1 == symbol2 and atom2 == symbol1)) and \
            distance < bonddis: 
                return True
        else: 
            return False

    for i in range(len(atoms)):
        for j in range(i):
            if (symbols[i] == 'O' and symbols[j] == 'Ti' and
                atoms.get_distance(i, j) < 2.40):
                bondatoms.append((i, j))
            elif (symbols[i] == 'Ti' and symbols[j] == 'O' and
                atoms.get_distance(i, j) < 2.40):
                bondatoms.append((i, j))
            elif (symbols[i] == 'C' and symbols[j] == 'Ti' and
                  atoms.get_distance(i, j) < 2.50):
                bondatoms.append((i, j))
            elif (symbols[i] == 'Ti' and symbols[j] == 'C' and
                  atoms.get_distance(i, j) < 2.50):
                bondatoms.append((i, j))
            elif (symbols[i] == 'O' and symbols[j] == 'Ti' and
                atoms.get_distance(i, j) < 2.40):
                bondatoms.append((i, j))
            elif (symbols[i] == 'Ti' and symbols[j] == 'O' and
                atoms.get_distance(i, j) < 2.40):
                bondatoms.append((i, j))
            elif (symbols[i] == 'O' and symbols[j] == 'H' and
                  atoms.get_distance(i, j) < 1.40):
                bondatoms.append((i, j))
            elif (symbols[i] == 'H' and symbols[j] == 'O' and
                  atoms.get_distance(i, j) < 1.40):
                bondatoms.append((i, j))
            elif (symbols[i] == 'H' and symbols[j] == 'C' and
                  atoms.get_distance(i, j) < 1.40):
                bondatoms.append((i, j))
            elif (symbols[i] == 'C' and symbols[j] == 'H' and
                  atoms.get_distance(i, j) < 1.40):
                bondatoms.append((i, j))
            elif (symbols[i] == 'H' and symbols[j] == 'O' and
                  atoms.get_distance(i, j) < 1.10):
                bondatoms.append((i, j))
            elif (symbols[i] == 'O' and symbols[j] == 'H' and
                  atoms.get_distance(i, j) < 1.10):
                bondatoms.append((i, j))

    # set texttures 
    textures = ['ase3' for a in atoms]

    # set rotation 
    #rot = '90x,-45y,0z'  # found using ag: 'view -> rotate'
    
    # Common kwargs for eps, png, pov
    kwargs = {
        'rotation'      : rot, # text string with rotation (default='' )
        'radii'         : .85, # float, or a list with one float per atom
        'colors'        : None,# List: one (r, g, b) tuple per atom
        'show_unit_cell': 0,   # 0, 1, or 2 to not show, show, and show all of cell
        'celllinewidth' : 0.1,  # Radius of the cylinders representing the cell
        'bondatoms'     : bondatoms, # list of tuples 
        'bondlinewidth' : 0.2, # linewidth of bond 
        'textures'      : textures, # Length of atoms list of texture names
        }
    
    # Extra kwargs only available for povray (All units in angstrom)
    kwargs.update({
        'run_povray'   : True, # Run povray or just write .pov + .ini files
        'display'      : False,# Display while rendering
        'pause'        : True, # Pause when done rendering (only if display)
        'transparent'  : False,# Transparent background
        'canvas_width' : None, # Width of canvas in pixels
        'canvas_height': 400, # Height of canvas in pixels 
        'camera_dist'  : 50.,  # Distance from camera to front atom
        'image_plane'  : None, # Distance from front atom to image plane
        'camera_type'  : 'perspective', # perspective, ultra_wide_angle
        'point_lights' : [],             # [[loc1, color1], [loc2, color2],...]
        'area_light'   : [(2., 3., 40.), # location
                          'White',       # color
                          .7, .7, 3, 3], # width, height, Nlamps_x, Nlamps_y
        'background'   : 'White',        # color
        })
       
    # Write the .pov (and .ini) file. If run_povray=False, you must run command
    # `povray filename.ini` to convert .pov file to .png
    write(povname+'.pov', atoms, **kwargs)


def plot_transition_states():
    """paper fig 1"""
    fig, axarr = plt.subplots(1, 2, figsize=(16, 6))
    plt.suptitle('Two Activation Mechanisms on Rutile-type Metal Oxides (110) Surface', \
            fontsize=24, fontweight='bold')

    # ts-ss 
    img = imread('ts.png')
    axarr[0].imshow(img)
    axarr[0].set_title('(a) Surface-stabilized Mechanism Transition State', \
            fontsize=20, fontweight='normal')
    axarr[0].set_xlim(0, 600)
    axarr[0].set_ylim(400, 0)
    axarr[0].set_axis_off()

    C, M = [340, 90], [380, 250] 
    axarr[0].scatter([C[0], M[0]], [C[1], M[1]], color='k', s=18)
    axarr[0].plot([C[0], M[0]], [C[1], M[1]], 'k-.')
    axarr[0].text(C[0]+5, C[1]+5, '$C$', fontsize=16)
    axarr[0].text(M[0]+5, M[1]-5, '$M_{cus}$', fontsize=16)
    #axarr[0].text((C[0]+M[0])/2.0, (C[1]+M[1])/2.0, 'short distance', fontsize=12)
    
    # ts-ra 
    img = imread('ts_ra.png')
    axarr[1].imshow(img)
    axarr[1].set_title('(b) Radical-like Mechanism Transition State', \
            fontsize=20, fontweight='normal')
    axarr[1].set_xlim(0, 600)
    axarr[1].set_ylim(400, 0)
    axarr[1].set_axis_off()

    C, M = [280, 80], [350, 270] 
    axarr[1].scatter([C[0], M[0]], [C[1], M[1]], color='k', s=18)
    axarr[1].plot([C[0], M[0]], [C[1], M[1]], 'k-.')
    axarr[1].text(C[0]+5, C[1]+5, '$C$', fontsize=16)
    axarr[1].text(M[0]+5, M[1]-5, '$M_{cus}$', fontsize=16)
    #axarr[1].text((C[0]+M[0])/2.0, (C[1]+M[1])/2.0, 'large distance', fontsize=12)

    # plot symbols 
    symbols = ['C', 'H', 'O', 'Ti']
    names = ['Carbon', 'Hydrogen', 'Oxygen', 'Titanium']
    lefts = np.arange(0.34, 0.66, 0.08)
    for i, left in enumerate(lefts):
        # set subfigure location 
        ax3 = fig.add_axes([left, 0.05, 0.05, 0.05])

        img = imread('../atoms/%s.png' %symbols[i])
        ax3.imshow(img)

        ax3.set_title(names[i], fontsize=16)
        ax3.set_axis_off()

    fig.savefig("../../figures/fig1.png")
    #plt.show()


if __name__ == '__main__':
    #atoms = read('ts_ra.con', format='vasp')
    #view(atoms)
    #write_transition_png(atoms, '30x,-60y,-120z', 'ts_ra')
    plot_transition_states()
