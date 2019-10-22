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
paper figure 3.
structure file, Hab2, Hab3, CH3ab, CH3ab2.
"""


def write_adsorption_png(atoms, rot, povname):
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
            if (symbols[i] == 'O' and symbols[j] == 'Ge' and
                atoms.get_distance(i, j) < 2.40):
                bondatoms.append((i, j))
            elif (symbols[i] == 'Ge' and symbols[j] == 'O' and
                atoms.get_distance(i, j) < 2.40):
                bondatoms.append((i, j))
            elif (symbols[i] == 'C' and symbols[j] == 'Ge' and
                  atoms.get_distance(i, j) < 2.50):
                bondatoms.append((i, j))
            elif (symbols[i] == 'Ge' and symbols[j] == 'C' and
                  atoms.get_distance(i, j) < 2.50):
                bondatoms.append((i, j))
            elif (symbols[i] == 'O' and symbols[j] == 'Ge' and
                atoms.get_distance(i, j) < 2.40):
                bondatoms.append((i, j))
            elif (symbols[i] == 'Ge' and symbols[j] == 'O' and
                atoms.get_distance(i, j) < 2.40):
                bondatoms.append((i, j))
            elif (symbols[i] == 'O' and symbols[j] == 'Ir' and
                  atoms.get_distance(i, j) < 2.40):
                bondatoms.append((i, j))
            elif (symbols[i] == 'Ir' and symbols[j] == 'O' and
                  atoms.get_distance(i, j) < 2.40):
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
    

def plot_adsorptions():
    """paper fig 3"""
    # figure general setting 
    fig, axarr = plt.subplots(2, 4, figsize=(16, 9))
    plt.tight_layout(pad=2.0, w_pad=2.0, h_pad=2.0)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=0.85, \
            wspace=None, hspace=0.2)

    plt.suptitle(r'Adsorption Configurations of H and $\bf{CH_3}$', \
            fontsize=24, fontweight='bold')

    axarr[0][0].text(300, -50, r'(a) Adsorption of ${H}$', fontsize=20, fontweight='normal')
    axarr[0][2].text(300, -50, r'(b) Adsorption of ${CH_3}$', fontsize=20, fontweight='normal')

    def plt_ax(ax, picname, title_text):
        img = imread(picname)
        ax.imshow(img)
        ax.set_title(title_text, fontsize=16)
        ax.set_axis_off()

    # plot H atoms 
    plt_ax(axarr[0][0], 'Hab2o.png', ' Over View of On-Top Position ')
    plt_ax(axarr[0][1], 'Hab2s.png', ' Side View of On-Top Position ')
    plt_ax(axarr[1][0], 'Hab3o.png', ' Over View of Inclined Position ')
    plt_ax(axarr[1][1], 'Hab3s.png', ' Sied View of Inclined Position ')

    # plot CH3 atoms 
    plt_ax(axarr[0][2], 'CH3abo.png', ' Over View of Vertical Position ')
    plt_ax(axarr[0][3], 'CH3abs.png', ' Sied View of Vertical Position ')
    plt_ax(axarr[1][2], 'CH3ab2o.png', ' Over View of Parallel Position ')
    plt_ax(axarr[1][3], 'CH3ab2s.png', ' Side View of Parallel Position ')

    # plot symbols 
    symbols = ['C', 'H', 'O', 'Ir', 'Ge']
    names = ['Carbon', 'Hydrogen', 'Oxygen', 'Base', 'Dopant']
    lefts = [0.30, 0.40, 0.50, 0.60, 0.70]
    for i, left in enumerate(lefts):
        # set subfigure location 
        ax = fig.add_axes([left, -0.00, 0.04, 0.04])
        atom = Atoms(symbols[i], positions=[[0, 0, 0]])

        # plot atoms 
        img = imread('../atoms/%s.png' %symbols[i])
        ax.imshow(img)

        ax.set_title(names[i], fontsize=16)
        ax.set_axis_off()

    #plt.show()
    plt.savefig('../../figures/fig3.png')


if __name__ == '__main__':
    atoms = read('./Hab2.con', format='vasp')
    if not os.path.exists('Hab2o.png'):
        write_adsorption_png(atoms, '90x,-45y,0z', 'Hab2o')
        write_adsorption_png(atoms, '0x,0y,45z', 'Hab2s')

    atoms = read('./Hab3.con', format='vasp')
    if not os.path.exists('Hab3o.png'):
        write_adsorption_png(atoms, '90x,-45y,0z', 'Hab3o')
        write_adsorption_png(atoms, '0x,0y,45z', 'Hab3s')

    atoms = read('./CH3ab.con', format='vasp')
    if not os.path.exists('CH3abo.png'):
        write_adsorption_png(atoms, '0x,0y,-90z', 'CH3abo')
        write_adsorption_png(atoms, '0x,-90y,-90z', 'CH3abs')

    atoms = read('./CH3ab2.con', format='vasp')
    if not os.path.exists('CH3ab2o.png'):
        write_adsorption_png(atoms, '90x,-45y,0z', 'CH3ab2o')
        write_adsorption_png(atoms, '0x,0y,45z', 'CH3ab2s')

    plot_adsorptions()
