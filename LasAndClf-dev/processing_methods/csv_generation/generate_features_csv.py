#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import os
import sys
import time

import re
import shutil
import string
import itertools

import numpy as np
import pandas as pd

# not print decimals in scientific notes 
np.set_printoptions(suppress=True)


"""
Description:
    Generate data csv from VASP output file CONTCAR 
    (surface, H-adsorbed surface, CH3-adsorbed surface). 
Author:
    Jiayan XU, CCC, ECUST, 2018-2019.
Scheme:
    step 0. read all CONTCARs. 
    step 1. transfer atoms' positions into standard order. 
    step 2. calculate geometric features between related atoms. 
    step 3. generate data csv.
Usage:
    >>> python3 ./generate_features_csv.py 'suf' 'd' ['O2', 'M4']
    >>> filename... 
"""


# ====== ====== ====== ====== ======  ====== ====== ====== ====== ====== 
# turn poscar/contcar into cif
# ====== ====== ====== ====== ======  ====== ====== ====== ====== ====== 
def read_car_and_get_cell(CONTCAR):
    """
    Description:
        Read POSCAR/CONTACR and return structure info.
    IN:
        CONTCAR - filepath
    OUT:
        abc - 3x3 array, lattice constant
        atoms - N list, element symbols
        xyzs - Nx3 array, direct coordinates
    """
    # read file 
    with open(CONTCAR, 'r') as f:
        content = f.readlines()

    # init lists
    abc, xyzs = [], []
    elements, numbers = [], []

    # get lattice constant
    for i in range(2,5):
        a_abc = []
        for cor in content[i].strip('\n').split(' '):
            if cor not in ['']: 
                a_abc.append(float(cor))
        abc.append(a_abc)
    abc = np.array(abc)

    # get elements
    for element in content[5].strip('\n').split(' '):
        if element not in ['']:
            elements.append(element)

    # get numbers
    for number in content[6].strip('\n').split(' '):
        if number not in ['']:
            numbers.append(int(number))

    # generate symbol list
    symbols = []
    for element, number in zip(elements, numbers):
        symbols.extend([element]*number)

    # get xyzs
    for i in range(9, 9+sum(numbers)):
        xyz = [] 
        for cor in content[i].strip('\n').split(' '):
            if cor not in ['','T','F']: 
                xyz.append(float(cor)) ###
        xyzs.append(xyz)
    xyzs = np.array(xyzs)

    # generate tuple(symbol, xyz) list 
    atoms = []
    for symbol, xyz in zip(symbols, xyzs):
        atoms.append((symbol,xyz))

    return abc, elements, numbers, xyzs


def write_car_to_cif(abc, elements, numbers, xyzs, cifname):
    """
    Description:
        Write car info to cif.
    IN:
        carname - POSCAR/CONTCAR filepath
        cifname - cif format filepath
    """
    # init cif content
    content = ''

    # write first line
    firstline = 'data_'
    for element in elements:
        firstline += element
    firstline += '\n'
    content += firstline

    # write mainbody of cif
    content += '{:<30}{:<20}\n'.format('_audit_creation_method', '\'pos2cif.py by jyxu\'')

    content += '{:<30}{:<20}\n'.format('_cell_length_a', np.linalg.norm(abc[0]))
    content += '{:<30}{:<20}\n'.format('_cell_length_b', np.linalg.norm(abc[1]))
    content += '{:<30}{:<20}\n'.format('_cell_length_c', np.linalg.norm(abc[2]))

    content += '{:<30}{:<20}\n'.format('_cell_angle_alpha', \
            180/np.pi*np.arccos(np.dot(abc[1], abc[2].T)/np.linalg.norm(abc[1])/np.linalg.norm(abc[2])))
    content += '{:<30}{:<20}\n'.format('_cell_angle_beta' , \
            180/np.pi*np.arccos(np.dot(abc[0], abc[2].T)/np.linalg.norm(abc[0])/np.linalg.norm(abc[2])))
    content += '{:<30}{:<20}\n'.format('_cell_angle_gamma', \
            180/np.pi*np.arccos(np.dot(abc[0], abc[1].T)/np.linalg.norm(abc[0])/np.linalg.norm(abc[1])))

    content += '{:<30}{:<20}\n'.format('_symmetry_space_group_H-M' , '\'P1\'')
    content += '{:<30}{:<20}\n'.format('_symmetry_Int_Tables_number' , '\'1\'')
    content += '{:<30}{:<20}\n'.format('_symmetry_cell_setting' , '\'triclinic\'')

    content += '{:<30}\n'.format('loop_')
    content += '{:<30}\n'.format('_symmetry_equiv_pos_as_xyz')
    content += '{:<30}\n'.format('x,y,z')
    content += '\n{:<30}\n'.format('loop_')
    content += '{:<30}\n'.format('_atom_site_label')
    content += '{:<30}\n'.format('_atom_site_type_symbol')
    content += '{:<30}\n'.format('_atom_site_occupancy')
    content += '{:<30}\n'.format('_atom_site_fract_x')
    content += '{:<30}\n'.format('_atom_site_fract_y')
    content += '{:<30}\n'.format('_atom_site_fract_z')
    content += '{:<30}\n'.format('_atom_site_U_iso_or_equiv')

    # write atom name and coordinate
    j = 0
    for element, number in zip(elements, numbers):
        for i in range(number):
            content += '{:<10}{:<10}{:<8}{:<20}{:<20}{:<20}{:<8}\n'.format\
                    (element + str(i+1), element, str(1.0000),\
                    round(xyzs[j][0], 8), round(xyzs[j][1], 8), round(xyzs[j][2], 8), \
                    str(0.0000))
            j += 1

    # check number of rutile surfaces plus reactants

    # write content to file
    with open(cifname, 'w') as f:
        f.write(content)


# ====== ====== ====== ====== ======  ====== ====== ====== ====== ====== 
# extract layer and reactant, then standardize them
# ====== ====== ====== ====== ======  ====== ====== ====== ====== ====== 
def tuple2dict(t):
    """Turn a Nx2 tuple into a dict."""
    d = {}
    for name, xyz in t:
        d[name] = xyz
    return d

def extract_layer(O_dict, M_dict):
    """
    Description:
        Extract first layer (8 O and 4 M) from structure. 
    IN:
        O_dict - *dict*, {'AtomName': array([x,y,z]), ...}
        M_dict - *dict*, {'AtomName': array([x,y,z]), ...}
    OUT:
        O_dict - *dict*, {'AtomName': array([x,y,z]), ...}, besides the layer
        M_dict - *dict*, {'AtomName': array([x,y,z]), ...}, besides the layer
        layer - *dict*, {'AtomTag': ['AtomName', array([x,y,z])], ...}
    NOTES:
        >>> Standard first layer
            Z--------------->Y
            | O1      M3
            | M1  O3      O5
            | O2      M4(dop)
            | M2  O4      O6
            V
            X
    """
    # sort O by z-axis, large to small
    O_dict_z = sorted(O_dict.items(), key=lambda e:e[1][2], reverse=True)

    # to get O1 O2, sort by x-axis
    O12_dict = tuple2dict(O_dict_z[:2])
    O12_dict_x = sorted(O12_dict.items(), key=lambda e:e[1][0], reverse=True)
    O1_tuple, O2_tuple = O12_dict_x[1], O12_dict_x[0]

    # get O3 O4 O5 O6
    O3456_dict = tuple2dict(O_dict_z[2:6])
    O3456_dict_y = sorted(O3456_dict.items(), key=lambda e:e[1][1], reverse=True)

    O34_dict = tuple2dict(O3456_dict_y[-2:])
    O34_dict_x = sorted(O34_dict.items(), key=lambda e:e[1][0], reverse=True)
    O3_tuple, O4_tuple = O34_dict_x[1], O34_dict_x[0]

    O56_dict = tuple2dict(O3456_dict_y[:2])
    O56_dict_x = sorted(O56_dict.items(), key=lambda e:e[1][0], reverse=True)
    O5_tuple, O6_tuple = O56_dict_x[1], O56_dict_x[0]

    # get O7 O8
    O78_dict = tuple2dict(O_dict_z[6:8])
    O78_dict_x = sorted(O78_dict.items(), key=lambda e:e[1][0], reverse=True)
    O7_tuple, O8_tuple = O78_dict_x[1], O78_dict_x[0]

    # get M1 M2 M3 M4, sort by z-axis
    M_dict_z = sorted(M_dict.items(), key=lambda e:e[1][2], reverse=True)
    M1234_dict = tuple2dict(M_dict_z[:4])
    M1234_dict_y = sorted(M1234_dict.items(), key=lambda e:e[1][1], reverse=True)

    M12_dict = tuple2dict(M1234_dict_y[-2:])
    M12_dict_x = sorted(M12_dict.items(), key=lambda e:e[1][0], reverse=True)
    M1_tuple, M2_tuple = M12_dict_x[1], M12_dict_x[0]

    M34_dict = tuple2dict(M1234_dict_y[:2])
    M34_dict_x = sorted(M34_dict.items(), key=lambda e:e[1][0], reverse=True)
    M3_tuple, M4_tuple = M34_dict_x[1], M34_dict_x[0]

    # get first layer
    layer = {}

    # get O in first layer
    layer['O1'], layer['O2'] = list(O1_tuple), list(O2_tuple)
    layer['O3'], layer['O4'] = list(O3_tuple), list(O4_tuple)
    layer['O5'], layer['O6'] = list(O5_tuple), list(O6_tuple)

    layer['O7'], layer['O8'] = list(O7_tuple), list(O8_tuple)

    # delete O in first layer 
    for key in ['O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8']:
        O_dict.pop(layer[key][0])

    # get M in first layer
    layer['M1'], layer['M2'] = list(M1_tuple), list(M2_tuple)
    layer['M3'], layer['M4'] = list(M3_tuple), list(M4_tuple)

    # delete M in first layer 
    for key in ['M1', 'M2', 'M3', 'M4']:
        M_dict.pop(layer[key][0])

    return O_dict, M_dict, layer


def standardize_layer(dopM, O_dict, M_dict):
    """
    Description:
        This is only for rutile-type metal oxides 110 surface.
        Adjust atoms in the first layer by the standard configuration.
    IN:
        dopM - *string*, the dopant metal's element symbol
    OUT:
    NOTES:
        >>> Standard first layer
            Z--------------->Y
            | O1      M3
            | M1  O3      O5
            | O2      M4(dop)
            | M2  O4      O6
            V
            X
    """
    # get layers and return rest atoms
    O2_dict, M2_dict, l1 = extract_layer(O_dict, M_dict)

    '''This inner function move atom coordinate by periodic.'''
    def mv_xyz(xyz, d, s):
        axis = {'x':0,'y':1,'z':2} # axises
        xyz[axis[d]] = xyz[axis[d]] + s
        return xyz

    # set dopM unchanged as the reference atom 
    '''
    >>> Problem: M4 must be the dop
        Z--------------->Y
        |  O1
        |  M1  O3  O5
        |  O2    M3(dop)
        |  M2  O4  O6
        V        M4
        X
    1. M4%x-1 2. M3<>M4
    '''
    if l1['M3'][0].strip(string.digits) == dopM and \
            l1['M4'][0].strip(string.digits) != dopM:
        l1['M4'][1] = mv_xyz(l1['M4'][1], 'x', -1)
        l1['M3'], l1['M4'] = l1['M4'], l1['M3']
        print('Change M3 M4.')
    #print(dopM)

    '''
    Make O3, O4, O5, O6 at proper location.
    >>> Problem
        Z--------------->Y
        |  O1      M3
      O3|  M1  O5 
        |  O2      M4(dop)
      O4|  M2  O6
        V
        X
    1. O3%y+1, O4%y+1 2. O3<>O5, O4<>O6
    '''
    if l1['O5'][1][1] < l1['M3'][1][1]:
        l1['O3'][1] = mv_xyz(l1['O3'][1], 'y', 1)
        l1['O4'][1] = mv_xyz(l1['O4'][1], 'y', 1)
        l1['O3'], l1['O5'] = l1['O5'], l1['O3']
        l1['O4'], l1['O6'] = l1['O6'], l1['O4']
        print('Change O3 O4.')

    '''
    Make O1, O2 at proper location.
    >>> Problem
        Z--------------->Y
        |        M3
        |  M1  O3  O5
        |  O1    M4
        |  M2  O4  O6
        V  O2
        X
    1. O2%x-1 2. O1<>O2
    '''
    if l1['O1'][1][0] > l1['O3'][1][0]:
        l1['O2'][1] = mv_xyz(l1['O2'][1], 'x', -1)
        l1['O1'], l1['O2'] = l1['O2'], l1['O1']
        print('Change O1 O2.')
    
    '''
    Currently, O1M1O2M2 must be in a row, \
            and O3456 must be at right of O12, \
            and M4%x is bigger than M3%x.
    Now, set O1 and O2 as the reference atom, other atoms are adjusted.
    >>> Situation
        Z----------->Y
        |  A      -1
        |     C   ^
        |  B     loc
        |     D   V
        |         +1
        V
        X

    loc means relative loc to the reference.
    This inner function make AB and CD in proper order.
    '''
    def adjust_AtomPair(A, B, C, D, loc):
        # check if CD is in the back cell
        if D[1][0] < A[1][0]:
            C[1] = mv_xyz(C[1], 'x', 1)
            D[1] = mv_xyz(D[1], 'x', 1)

        # check if AD is in the front cell
        if C[1][0] > B[1][0]:
            C[1] = mv_xyz(C[1], 'x', -1)
            D[1] = mv_xyz(D[1], 'x', -1)

        # loc: 1 -> move CD to the front -1 -> move CD to the back
        if loc == 1:
            if C[1][0] < A[1][0] and (A[1][0] < D[1][0] < B[1][0]):
                C[1] = mv_xyz(C[1], 'x', 1)
                C, D = D, C
        elif loc == -1:
            if (A[1][0] < C[1][0] < B[1][0]) and B[1][0] < D[1][0]:
                D[1] = mv_xyz(D[1], 'x', -1)
                C, D = D, C
        return C, D

    # move O34 refer to M34
    l1['O3'], l1['O4'] = adjust_AtomPair(l1['M3'], l1['M4'], \
            l1['O3'], l1['O4'], 1)

    # move O56 refer to M34
    l1['O5'], l1['O6'] = adjust_AtomPair(l1['M3'], l1['M4'], \
            l1['O5'], l1['O6'], 1)

    # move M12 refer to M34
    l1['M1'], l1['M2'] = adjust_AtomPair(l1['M3'], l1['M4'], \
            l1['M1'], l1['M2'], 1)

    # move O12 refer to M12
    l1['O1'], l1['O2'] = adjust_AtomPair(l1['M1'], l1['M2'], \
            l1['O1'], l1['O2'], -1)

    # move O78 refer to M12
    l1['O7'], l1['O8'] = adjust_AtomPair(l1['M1'], l1['M2'], \
            l1['O7'], l1['O8'], -1)
    
    # check atoms configuration in the first layer
    if l1['M4'][0].strip(string.digits) != dopM:
        #print(l1['M4'][0], dopM)
        raise ValueError('Wrong dopant location.')

    if not l1['O1'][1][0] < l1['M1'][1][0] \
            < l1['O2'][1][0] < l1['M2'][1][0]:
        raise ValueError('Wrong Config in O1 M1 O2 M2 x.')
    elif not l1['O1'][1][0] < l1['O3'][1][0] \
            < l1['O2'][1][0] < l1['O4'][1][0]:
        raise ValueError('Wrong Config in O1 O3 O2 O4 x.')
    elif not l1['M3'][1][0] < l1['O3'][1][0] \
            < l1['M4'][1][0] < l1['O4'][1][0]:
        #print(l1['M3'][1][0], l1['O3'][1][0], l1['M4'][1][0], l1['O4'][1][0])
        raise ValueError('Wrong Config in M3 O3 M4 O4 x.')
    elif not l1['M3'][1][0] < l1['O5'][1][0] \
            < l1['M4'][1][0] < l1['O6'][1][0]:
        raise ValueError('Wrong Config in M3 O5 M4 O6 x.')

    if not l1['O1'][1][1] < l1['O3'][1][1] \
            < l1['M3'][1][1] < l1['O5'][1][1]:
        raise ValueError('Wrong Config in O1 O3 M3 O5 y.')
    elif not l1['M1'][1][1] < l1['O3'][1][1] \
            < l1['M4'][1][1] < l1['O5'][1][1]:
        raise ValueError('Wrong Config in M1 O3 O5 y.')
    elif not l1['O2'][1][1] < l1['O4'][1][1] \
            < l1['M4'][1][1] < l1['O6'][1][1]:
        raise ValueError('Wrong Config in O2 M4 y.')
    elif not l1['M2'][1][1] < l1['O4'][1][1] \
            < l1['M4'][1][1] < l1['O6'][1][1]:
        raise ValueError('Wrong Config in M2 O4 O6 y.')

    return l1


# ====== ====== ====== ====== ======  ====== ====== ====== ====== ====== 
# Extract functional group and standardize them.
# ====== ====== ====== ====== ======  ====== ====== ====== ====== ====== 
def extract_reactant(H_dict, C_dict, group):
    """
    Description:
        Extract functional group (H, CH3, CH4) from H and C dictionary.
    IN:
        H_dict - *dict*, {'AtomName': array([x,y,z]), ...}
        C_dict - *dict*, {'AtomName': array([x,y,z]), ...}
        group - *str*, Hab2, Hab3, CH3ab, CH3ab2, ...
    OUT:
        group_dict - *dict*, {'AtomTag': ['AtomName', array([x,y,z])], ...}
    """
    # get H1 from Hab
    def get_Hab(H_dict):
        Hab_dict = {}
        H_dict_y = sorted(H_dict.items(), key=lambda e:e[1][1], reverse=True)
        H1_tuple = H_dict_y[0]

        Hab_dict['H1'] = list(H1_tuple)

        return Hab_dict

    # get CH3 from CH3
    def get_CH3(H_dict, C_dict):
        CH3_dict = {}

        H_dict_y = sorted(H_dict.items(), key=lambda e:e[1][1], reverse=True)
        H1_tuple = H_dict_y[2]

        H34_dict = tuple2dict(H_dict_y[0:2])
        H34_dict_x = sorted(H34_dict.items(), key=lambda e:e[1][0], reverse=True)
        H3_tuple = H34_dict_x[0]
        H4_tuple = H34_dict_x[1]

        C_dict_x = sorted(C_dict.items(), key=lambda e:e[1][0], reverse=True)

        CH3_dict['C'] = list(C_dict_x[0])
        CH3_dict['H1'] = list(H1_tuple)
        CH3_dict['H3'] = list(H3_tuple)
        CH3_dict['H4'] = list(H4_tuple)

        return CH3_dict

    # get CH4 from ts, tsra, fs, fsra
    def get_CH4(H_dict, C_dict):
        CH4_dict = {}

        H_dict_y = sorted(H_dict.items(), key=lambda e:e[1][1], reverse=True)
        H1_tuple = H_dict_y[3]
        H2_tuple = H_dict_y[0]

        H34_dict = tuple2dict(H_dict_y[1:3])
        H34_dict_x = sorted(H34_dict.items(), key=lambda e:e[1][0], reverse=True)

        H3_tuple = H34_dict_x[0]
        H4_tuple = H34_dict_x[1]

        C_dict_x = sorted(C_dict.items(), key=lambda e:e[1][0], reverse=True)

        CH4_dict['C'] = list(C_dict_x[0])
        CH4_dict['H1'] = list(H1_tuple)
        CH4_dict['H2'] = list(H2_tuple)
        CH4_dict['H3'] = list(H3_tuple)
        CH4_dict['H4'] = list(H4_tuple)

        return CH4_dict

    # choose group to extract
    if group == 'suf':
        group_dict = {}
    elif group == 'Hab2' or group == 'Hab3':
        group_dict = get_Hab(H_dict)
    elif group == 'CH3ab' or group == 'CH3ab2':
        group_dict = get_CH3(H_dict, C_dict)
    elif group == 'ts' or group == 'fs' \
            or group == 'tsra' or group == 'fsra':
        group_dict = get_CH4(H_dict, C_dict)
    else:
        raise ValueError('No such group to extract.')

    return group_dict

def standardize_reactant(layer, H_dict, C_dict, group):
    """Check reactant(H,CH3,CH4) is in the given order."""
    reactant = extract_reactant(H_dict, C_dict, group)

    if group == 'suf':
        pass
    elif 'C' not in group:
        # check H 
        if layer['M1'][1][0] < reactant['H1'][1][0] \
                < layer['M2'][1][0]:
            pass 
        else:
            err = str(layer['M1'][1][0]) \
                    + ' < ' + str(reactant['H1'][1][0]) \
                    + ' < ' + str(layer['M2'][1][0])
            raise ValueError('H is at the improper location. %s' %err)
            #print('H is at the improper location. %s' %err)
    else:
        if layer['O3'][1][0] < reactant['C'][1][0] \
                < layer['O4'][1][0]:
            pass 
        else:
            #raise ValueError('C is at the improper location.')
            print('C is at the improper location.')
        if layer['O2'][1][1] < reactant['H1'][1][1] \
                    < reactant['C'][1][1]:
                pass 
        else:
            err = str(layer['O2'][1][1]) \
                    + ' < ' + str(reactant['H1'][1][1]) \
                    + ' < ' + str(reactant['C'][1][1])
            raise ValueError('H1 is at the improper location. %s' %err)

    return reactant


# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== 
# standardize contcar form for Rutile    
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== 
def standardize_contcars(CONTCAR, group):
    """
    Description:
        Standardize surface structure of 110 Rutile MO.
    IN:
        CONTCAR - vaspfile, filepath
        group - *string*, Hab2/.../tsra
    OUT:
        abc - *3x3 array*, lattice constant
        atoms - *1xN list*, atoms
        xyzs - *3*N array*, direct coordinates
        layer1 - *dict*, {'AtomTag': ['AtomName', arrat[x,y,z]]}
        reactant - *dict*, {'AtomTag': ['AtomName', arrat[x,y,z]]}
    NOTES:
        xyzs is an np.array object. Therefore, change the element of xyzs in 
        other subroutines (functions, list/dict, ...) will consequently change 
        the original element of xyzs.
    """
    # read car and get info
    abc, elements, numbers, xyzs = read_car_and_get_cell(CONTCAR)

    # current dopped metals
    metals = ['Ti', 'V', 'Ge', 'Mo', 'Ru', 'Rh', 'Os', 'Ir', 'Mn', 'Cr'] 

    # get car name and dop atom
    contcar_name = os.path.basename(CONTCAR)
    if 'pure' in contcar_name:
        for metal in metals:
            if metal in contcar_name.split('_')[0]:
                dopM = metal 
                break
    elif 'dop' in contcar_name:
        dopM = contcar_name.split('_')[1]
    else:
        raise ValueError('Wrong name in contcar_name.')

    # old IrO2 form is different from standard, so change 
    if 'IrO2' in CONTCAR and 'Cr' not in CONTCAR \
            and 'Mn' not in CONTCAR:
        for xyz in xyzs:
            xyz[0] = 1 - xyz[0]
            xyz[1] = 1 - xyz[1]

    # round xyz by 8
    for xyz in xyzs:
        for i in range(len(xyz)):
            xyz[i] = round(xyz[i], 8)

    # move up atoms to the bottom
    for i, xyz in enumerate(xyzs):
        for j, cor in enumerate(xyz):
            if cor >= 0.9:
                xyzs[i][j] -= 1.0

    # old_xyzs = xyzs.copy()

    # make dict, get element name and number
    count = 0
    atoms_dict = {}

    for element, number in zip(elements, numbers):
        for i in range(number):
            atoms_dict[element + str(i+1)] = xyzs[count]
            count += 1

    # classify atoms into different dictionaries by element symbol
    H_dict, C_dict, O_dict, M_dict = {}, {}, {}, {}
    for element_name in atoms_dict.keys():
        if element_name.strip(string.digits) == 'H':
            H_dict[element_name] = atoms_dict[element_name]
        elif element_name.strip(string.digits) == 'C':
            C_dict[element_name] = atoms_dict[element_name]
        elif element_name.strip(string.digits) == 'O':
            O_dict[element_name] = atoms_dict[element_name]
        elif element_name.strip(string.digits) in metals:
            M_dict[element_name] = atoms_dict[element_name]

    # extract and standardize the first layer
    layer1 = standardize_layer(dopM, O_dict, M_dict)

    # extract and standardize the reactant
    reactant = standardize_reactant(layer1, H_dict, C_dict, group)

    # new_xyzs = xyzs.copy()

    '''
    for old, new in zip(old_xyzs, new_xyzs):
        for i in range(3):
            if old[i] != new[i]:
                print(old, new)
    '''

    # move M4 in cube, and other follows
    move_array = -np.floor(layer1['M4'][1])
    for key in layer1.keys():
        layer1[key][1] += move_array

    for key in reactant.keys():
        reactant[key][1] += move_array

    # update xyzs with layer1 and reactant
    for name, xyz in layer1.values():
        if atoms_dict[name].any() != xyz.any():
            print('Some xyzs are changed.')
        atoms_dict[name] = xyz

    for name, xyz in reactant.values():
        if atoms_dict[name].any() != xyz.any():
            print('Some xyzs are changed.')
        atoms_dict[name] = xyz

    # order xyz in elements order

    return abc, elements, numbers, xyzs, layer1, reactant


# ====== ====== ====== ====== ======  ====== ====== ====== ====== ====== 
# Calculate geometric features (distance, angle, dihedral) from given atoms.
# ====== ====== ====== ====== ======  ====== ====== ====== ====== ====== 
def calc_distance(abc, XYZ1, XYZ2):
    '''
    Calculate the distance between 1 and 2.
    XYZ must be absolute coordinates [X, Y, Z]
    1----2
    '''
    XYZ1 = (abc.T*XYZ1).T.sum(0)
    XYZ2 = (abc.T*XYZ2).T.sum(0)

    return round(np.linalg.norm(XYZ1-XYZ2), 8)


def calc_angle(abc, XYZ1, XYZ2, XYZ3, unit = 'rad'):
    '''
    Calculate the angle among 1, 2 and 3. Default unit is rad.
       1
      /
     / ) theta
    2 ----- 3
    '''
    XYZ1 = (abc.T*XYZ1).T.sum(0)
    XYZ2 = (abc.T*XYZ2).T.sum(0)
    XYZ3 = (abc.T*XYZ3).T.sum(0)
    vec1 = XYZ1 - XYZ2
    vec2 = XYZ3 - XYZ2
    costheta =  np.dot(vec1, vec2.T)/\
            (np.linalg.norm(vec1)*np.linalg.norm(vec2))

    if costheta > 1 or costheta < -1:
        print('A Wrong! Theta_Rad=%s' %(theta_rad))
        return 'np.nan'
    else:
        theta_rad = np.arccos(costheta)
        if unit == 'rad':
            return round(theta_rad, 8)
        elif unit == 'degree':
            return round(theta_rad/np.pi*180, 4)
        else:
            raise ValueError('No such unit for angle.')


def calc_dihedral(abc, XYZ1, XYZ2, XYZ3, XYZ4, unit='rad'):
    '''
    Calculate dihedral among 4 atoms.
         1
        / \
       / 5 \
      3-----4
       \ 6 /
        \ /
         2
    '''
    XYZ1 = (abc.T*XYZ1).T.sum(0)
    XYZ2 = (abc.T*XYZ2).T.sum(0)
    XYZ3 = (abc.T*XYZ3).T.sum(0)
    XYZ4 = (abc.T*XYZ4).T.sum(0)

    a=-((XYZ1[0]-XYZ4[0])*(XYZ4[0]-XYZ3[0])+\
            (XYZ1[1]-XYZ4[1])*(XYZ4[1]-XYZ3[1])+\
            (XYZ1[2]-XYZ4[2])*(XYZ4[2]-XYZ3[2]))/\
            ((XYZ4[0]-XYZ3[0])**2+\
            (XYZ4[1]-XYZ3[1])**2+\
            (XYZ4[2]-XYZ3[2])**2)

    b=-((XYZ2[0]-XYZ4[0])*(XYZ4[0]-XYZ3[0])+\
            (XYZ2[1]-XYZ4[1])*(XYZ4[1]-XYZ3[1])+\
            (XYZ2[2]-XYZ4[2])*(XYZ4[2]-XYZ3[2]))/\
            ((XYZ4[0]-XYZ3[0])**2+\
            (XYZ4[1]-XYZ3[1])**2+\
            (XYZ4[2]-XYZ3[2])**2)

    vec1 = [XYZ1[0]-XYZ4[0]+(XYZ4[0]-XYZ3[0])*a,\
            XYZ1[1]-XYZ4[1]+(XYZ4[1]-XYZ3[1])*a,\
            XYZ1[2]-XYZ4[2]+(XYZ4[2]-XYZ4[2])*a]
    vec1 = np.array(vec1)

    vec2 = [XYZ1[0]-XYZ4[0]+(XYZ4[0]-XYZ3[0])*b,\
            XYZ1[1]-XYZ4[1]+(XYZ4[1]-XYZ3[1])*b,\
            XYZ1[2]-XYZ4[2]+(XYZ4[2]-XYZ4[2])*b]
    vec2 = np.array(vec2)

    costheta =  np.dot(vec1, vec2.T)/\
            (np.linalg.norm(vec1)*np.linalg.norm(vec2))
    costheta = round(costheta, 4)
    if not (-1 <= costheta <= 1):
        print('Something wrong with dihedral.%f' %costheta)
        return 'np.nan'
    theta_rad = np.arccos(costheta)

    if unit == 'rad':
        return round(theta_rad, 8)
    elif unit == 'degree':
        return round(theta_rad/np.pi*180, 4)
    else:
        raise ValueError('No such unit for dihedral.')


def generate_lattice_features(cif_name):
    '''Some features with lattice.'''
    if 'pure' in cif_name:
        name = cif_name.split('_')[0]
        cell = cif_name.split('_')[0].strip('pure')
        dop = 'pure'
    else:
        name = cif_name.split('_')[0] + '_' + cif_name.split('_')[1]
        cell = cif_name.split('_')[0].strip('dop')
        dop = cif_name.split('_')[1]

    return {'name':name, 'cell':cell, 'dop':dop}


def generate_distance_features(abc, elements, group):
    '''Generate distance features, return a dict.'''
    # get atom name
    elements_list = list(elements.keys())

    # generate features
    d_feas = {}
    for i in range(len(elements_list)):
        for j in range(i+1,len(elements.keys())):
            fea_name = 'd_' + elements_list[i] \
                    + '-' + elements_list[j] + '_' + group
            fea_value = calc_distance(abc, \
                    elements[elements_list[i]][1], \
                    elements[elements_list[j]][1])
            d_feas[fea_name] = fea_value
    return d_feas


def generate_angle_features(abc, elements, group):
    '''Generate angle features, Nx(N-1)x(N-2)/2 in total.'''
    # get atom name
    elements_list = list(elements.keys())

    # generate features
    a_feas = {}
    num = len(elements_list)
    combinations = []
    for j in range(num):
        n = list(range(num))
        n.remove(j)
        coms = list(itertools.combinations(n, 2))
        for com in coms:
            i = com[0]
            k = com[1]
            fea_name = 'a_' + elements_list[i] + \
                    '-' + elements_list[j] + \
                    '-' + elements_list[k] + \
                    '_' + group
            fea_value = calc_angle(abc, \
                    elements[elements_list[i]][1], \
                    elements[elements_list[j]][1], \
                    elements[elements_list[k]][1])
            a_feas[fea_name] = fea_value
    return a_feas


def generate_dihedral_features(abc, elements, group):
    '''Generate dihedral features, Nx...x(N-3)/8 in total.'''
    # get atom name
    elements_list = list(elements.keys())
    num = len(elements.keys())
    h_feas = {}

    # combinations dihedral
    ijs = [[0,1],[0,2],[0,3]]
    kls = [[2,3],[1,3],[1,2]]

    coms_4 = list(itertools.combinations(list(range(num)), 4))
    for com_4 in coms_4:
        for h in range(3):
            i, j = com_4[ijs[h][0]], com_4[ijs[h][1]]
            k, l = com_4[kls[h][0]], com_4[kls[h][1]]
            fea_name = 'h_' + elements_list[i] + '-' \
                    + elements_list[j] + '-' \
                    + elements_list[k] + '-' \
                    + elements_list[l] + '_' \
                    + group
            fea_value = calc_dihedral(abc, \
                    elements[elements_list[i]][1], \
                    elements[elements_list[j]][1], \
                    elements[elements_list[k]][1], \
                    elements[elements_list[l]][1])
            h_feas[fea_name] = fea_value

    return h_feas


def generate_all_features(abc, fea_atoms, group, fea_type, cif_name):
    """
    Description:
        Generate all of parameters including distance, 
        angle and dihedral.
    IN:
        abc - *3x3 array*, lattice constant
        layer - atoms
    """
    # init the total paras
    total_paras = {}

    # get name, cell, dop
    lattice_paras = generate_lattice_features(cif_name)
    total_paras = dict(lattice_paras)

    # take atom in layer as an element
    elements = fea_atoms

    # distance 
    if 'd' in fea_type:
        d_para = generate_distance_features(abc, elements, group)
        total_paras = dict(total_paras, **d_para)

    # angle
    if 'a' in fea_type:
        a_para = generate_angle_features(abc, elements, group)
        total_paras = dict(total_paras, **a_para)

    # dihedral
    if 'h' in fea_type:
        h_para = generate_dihedral_features(abc, elements, group)
        total_paras = dict(total_paras, **h_para)

    return total_paras


# ====== ====== ====== ====== ======  ====== ====== ====== ====== ====== 
# Finally, we generate csv full of featurs.
# ====== ====== ====== ====== ======  ====== ====== ====== ====== ====== 
def generate_csv(group, fea_type, atomtags=[], datadir='../../../data/'):
    """
    Description:
        Generate CSV data.
    >>> get_csv('CH3ab', 'da')
    """
    # set cons and cifs dirpath
    cons_dir = datadir + group + '_data/' + group + '_cons'
    cifs_dir = datadir + group + '_data/' + group + '_cifs'

    # set MS dir
    MS_dir = os.path.join(os.path.expanduser('~'), \
            r'Documents/Materials Studio Projects/DopRutile_Files/Documents')
    MS_cifs_dir = os.path.join(MS_dir, group+'_cifs')

    # csv file
    csv_name = group + '_data_' + time.strftime("%Y%m%d", time.localtime()) + '.csv'
    csv_path = os.path.join(os.path.expanduser('~'), 'Desktop/CH4_DS/' + csv_name)

    # init pandas DataFrame
    row_index = 1
    group_df = pd.DataFrame()

    # remove cif already exists
    for file_name in os.listdir(cons_dir):
        f = os.path.join(cons_dir, file_name)
        if re.match(r'.*.cif', file_name):
            os.remove(f)

    # write the following lines
    for con_name in os.listdir(cons_dir):
        # print current working file
        print('{:<5}{:^5}{:<30}{:^3}'.format(row_index, ' --> ', con_name, ' | '))

        # prepare to write cif
        con = os.path.join(cons_dir, con_name)
        cif = os.path.join(cifs_dir, os.path.basename(con) + '.cif')

        abc, elements, numbers, xyzs, first_layer, reactant = standardize_contcars(con, group)
        write_car_to_cif(abc, elements, numbers, xyzs, cif)

        # copy cif to MS dir for visualization
        ms_xsd = os.path.join(MS_cifs_dir, os.path.basename(con)+'.xsd')
        if not os.path.exists(ms_xsd):
            ms_cif = os.path.join(MS_cifs_dir, os.path.basename(cif))
            shutil.copy(cif, ms_cif)

        # choose what atom to generate features
        all_atoms = dict(first_layer, **reactant)
        fea_atoms = {}
        if atomtags != []:
            for tag in atomtags:
                if tag in all_atoms.keys():
                    fea_atoms[tag] = all_atoms[tag]
                else:
                    raise ValueError('There is no such tag in all_atoms.')

        # generate features
        all_features = generate_all_features(abc, fea_atoms, group, \
                fea_type, os.path.basename(cif))

        # add features name or value
        # write the first line which contains feature names
        if row_index == 1:
            group_df = pd.DataFrame(columns=tuple(all_features.keys()))

        group_df.loc[row_index] = list(all_features.values())
        row_index += 1
        
    # postprocessing of csv
    group_df = group_df.sort_values(by=['cell', 'name', 'dop'], ascending=True)
    group_df = group_df.reset_index(drop=True)

    print('\n', 'There is %d geometrical descriptors in total.' %(group_df.shape[1]-3), '\n')
    group_df.to_csv(csv_path)


if __name__ == '__main__':
    fea_atoms = ['O2', 'M4', 'H1', 'C']
    if len(sys.argv) == 1:
        print('get geometry features\nget_main.py [group] [paras]\nTest Only.')
        generate_csv('tsra', 'dah', fea_atoms)
    elif len(sys.argv) == 2:
        group = str(sys.argv[1]) 
        generate_csv(group, 'dah', fea_atoms)
    elif len(sys.argv) == 3:
        group = str(sys.argv[1])
        paras = str(sys.argv[2])
        generate_csv(group, paras, fea_atoms)
    elif len(sys.argv) == 4:
        group = str(sys.argv[1])
        paras = str(sys.argv[2])
        fea_atoms = str(sys.argv[3])
        generate_csv(group, paras, fea_atoms)
    else:
        print('Wrong argvs!')
        sys.exit()
