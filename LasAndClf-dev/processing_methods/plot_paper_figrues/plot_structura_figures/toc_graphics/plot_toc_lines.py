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
paper figure 7.
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



def plot_had(ax, feaname, atoms):
    """"""
    img = imread('./h.png')
    ax.imshow(img)

    ax.text(100, 10, feaname, fontsize=20)

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
                head_width=15, fc='k', zorder=10)

        ax.arrow(atoms[2][0], atoms[2][1], \
                0.15*(atoms[0][0]-atoms[2][0]), \
                0.15*(atoms[0][1]-atoms[2][1]), \
                head_width=15, fc='k', zorder=10)


def plot_ch3ad(ax, atoms):
    """"""
    img = imread('./ch3.png')
    #ax.imshow(img)

    # plot dots and lines 
    xs, ys = [], [] 
    for atom in atoms:
        xs.append(atom[0])
        ys.append(atom[1])

    ax.scatter(xs, ys, color='k', zorder=10)
    ax.plot(xs, ys, 'k-', lw=2)

    if len(atoms) == 4:
        ax.plot([atoms[0][0], atoms[3][0]], \
                [atoms[0][1], atoms[3][1]], \
                'k-', lw=2, zorder=10)

    '''
    if len(atoms) in [3, 4]:
        ax.arrow(atoms[0][0], atoms[0][1], \
                0.25*(atoms[2][0]-atoms[0][0]), \
                0.25*(atoms[2][1]-atoms[0][1]), \
                head_width=15, fc='k', zorder=10)

        ax.arrow(atoms[2][0], atoms[2][1], \
                0.25*(atoms[0][0]-atoms[2][0]), \
                0.25*(atoms[0][1]-atoms[2][1]), \
                head_width=15, fc='k', zorder=10)
    '''

    #ax.set_axis_off() 


def plot_structural_descriptors():
    """"""
    # figure general setting 
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))

    plt.tight_layout(pad=2.0, w_pad=2.0, h_pad=2.0)
    plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, \
            wspace=0.1, hspace=0.1)

    
    ax.text(200, 0, r'$\bf{\stackrel{ss}{\swarrow}CH_4{\stackrel{ra}{\searrow}}}$',
            fontsize=20)
    ax.text(50, 50, r'$\bf{H^* + CH_3^*}$', \
            fontsize=20)
    ax.text(300, 50, r'$\bf{CH_3(g) + H^*}$', \
            fontsize=20)
    ax.set_axis_off()
    #ax.text(0, 450, r'$\bf{E_a \propto Geometrical\ Descriptors}$', fontsize=20)

    M_cus = [380, 255]
    O_br = [135, 150]
    H_ch3 = [285, 70]
    H_h = [180, 105]
    C = [355, 95]

    
    # 1 angle 
    ax.set_xlim(0,550)
    ax.set_ylim(450,0)
    '''
    plot_ch3ad(ax, [O_br, H_ch3, C, M_cus])

    ax.plot([O_br[0], 0.5*(H_ch3[0]+M_cus[0])], [O_br[1], 0.5*(H_ch3[1]+M_cus[1])], 'k-', lw=2)
    ax.plot([C[0], 0.5*(H_ch3[0]+M_cus[0])], [C[1], 0.5*(H_ch3[1]+M_cus[1])], 'k-', lw=2)

    m_HM = [0.5*(H_ch3[0]+M_cus[0]), 0.5*(H_ch3[1]+M_cus[1])]

    c, m, x, y  = draw_arc([C, M_cus])
    ax.plot(x, y, 'k-.', lw=2)
    ax.text(m[0]+20, m[1]-20, 'Distance', fontweight='bold', fontsize=16)

    c, m, x, y  = draw_arc([O_br, M_cus, C])
    ax.plot(x, y, 'k-.', lw=2)
    ax.text(m[0]-100, m[1]-20, 'Angle', fontweight='bold', fontsize=16)

    c, m, x, y  = draw_arc([O_br, m_HM, C])
    ax.plot(x, y, 'k-.', lw=2)
    ax.text(m[0]-100, m[1]-20, 'Dihedral', fontweight='bold', fontsize=16)
    '''

    #plt.show()
    fig.savefig("title.png", transparent=True)


if __name__ == '__main__':
    atoms = read('h_ad_suf.con', format='vasp')
    if not os.path.exists('h.png'):
        write_adsorption_png(atoms, '30x,-60y,-120z', 'h')

    atoms = read('ch3_ad_suf.con', format='vasp')
    if not os.path.exists('ch3.png'):
        write_adsorption_png(atoms, '30x,-60y,-120z', 'ch3')

    plot_structural_descriptors()
