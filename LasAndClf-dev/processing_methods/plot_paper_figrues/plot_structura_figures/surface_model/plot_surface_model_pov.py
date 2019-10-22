#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import os 

import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.image import imread 

from ase import Atoms

from ase.io import read, write 
from ase.visualize import view

"""
paper figure 1. 
structure file, surface_model.con
"""

def write_surface_png(atoms, rot, povname):
    # running index for the bonds 
    bondatoms = []
    symbols = atoms.get_chemical_symbols()
    for i in range(len(atoms)):
        for j in range(i):
            if (symbols[i] == 'O' and symbols[j] == 'Ge' and
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
        'canvas_height': 800, # Height of canvas in pixels 
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

if __name__ == '__main__':
    # read atoms
    atoms = read('./surface_model.con', format='vasp')

    if not os.path.exists('./surface_overview.png'):
        write_surface_png(atoms, '90x,-45y,0z', 'surface_overview')

    if not os.path.exists('./surface_sideview.png'):
        write_surface_png(atoms, '0x,0y,45z', 'surface_sideview')
    
    fig, axarr = plt.subplots(1, 2, figsize=(16, 6))
    plt.suptitle('(110) Surface Model of Rutile-type Metal Oxides', \
            fontsize=24, fontweight='bold')

    # fig a 
    axarr[0].set_title('(a) Over View', fontsize=20, fontweight='normal')
    axarr[0].set_axis_off()

    img = imread('./surface_overview.png')
    axarr[0].imshow(img)

    axarr[0].text(125, 480, '$O_{br}$', fontsize=16)
    axarr[0].text(470, 470, '$M_{cus}$', fontsize=16)

    # fig b 
    axarr[1].set_title('(b) Side View', fontsize=20, fontweight='normal')
    axarr[1].set_axis_off()

    img = imread('./surface_sideview.png')
    axarr[1].imshow(img)

    # plot symbols 
    symbols = ['Ir', 'O', 'Ge']
    names = ['Base', 'Oxygen', 'Dopant']
    lefts = [0.40, 0.50, 0.60]
    for i, left in enumerate(lefts):
        # set subfigure location 
        ax = fig.add_axes([left, 0.05, 0.05, 0.05])
        img = imread('../atoms/%s.png' %symbols[i])
        ax.imshow(img)

        ax.set_title(names[i], fontsize=16)
        ax.set_axis_off()

    #plt.show()
    plt.savefig('../../figures/fig2.png')
