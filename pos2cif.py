#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: pos2cif.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 二  4/24 19:16:55 2018
#########################################################################
import os
import sys
import numpy as np
###
def get_cell(CONTCAR):
    abc = []
    xyzs = []
    elements = []
    numbers = []
    with open(CONTCAR, 'r') as f:
        content = f.readlines()
        # get abc
        for i in range(2,5):
            a_abc = []
            for cor in content[i].strip('\n').split(' '):
                if cor not in ['']: 
                    a_abc.append(float(cor))
            abc.append(a_abc)
        # get elements
        for element in content[5].strip('\n').split(' '):
            if element not in ['']:
                elements.append(element)
        # get numbers
        for number in content[6].strip('\n').split(' '):
            if number not in ['']:
                numbers.append(int(number))
        # get xyzs
        for i in range(9, 9+sum(numbers)):
            xyz = [] 
            for cor in content[i].strip('\n').split(' '):
                if cor not in ['','T','F']: 
                    xyz.append(float(cor)) ###
            xyzs.append(xyz)
    xyzs = np.array(xyzs)
    abc = np.array(abc)
    return abc, elements, numbers, xyzs 
###
def  write_cif(cif_name, abc, elements, numbers, xyzs):
    ### write cif
    content = ''
    #
    firstline = 'data_'
    for element in elements:
        firstline += element
    firstline += '\n'
    content += firstline
    #
    content += '{:<30}{:<20}\n'.format('_audit_creation_method', '\'pos2cif.py\'')
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
    #
    atom_sum = 0
    for i in range(len(elements)):
        for j in range(atom_sum, atom_sum + numbers[i]):
            content += '{:<5}{:<5}{:<8}{:<20}{:<20}{:<20}{:<8}\n'.format\
                    (elements[i] + str(j+1), elements[i], str(1.0000),\
                    xyzs[j][0], xyzs[j][1], xyzs[j][2], str(0.0000))
        atom_sum += numbers[i]
                    ###
    with open(cif_name, 'w') as f:
        f.write(content)
###
def main():
    if len(sys.argv) == 1:
        if os.path.exists('./POSCAR'):
            abc, elements, numbers, xyzs = get_cell('./POSCAR')
            write_cif('POSCAR.cif', abc, elements, numbers, xyzs)
            print('POSCAR to POSCAR.cif !')
        elif os.path.exists('./CONTCAR'):
            abc, elements, numbers, xyzs = get_cell('./CONTCAR')
            write_cif('CONTCAR.cif', abc, elements, numbers, xyzs)
            print('CONTCAR to CONTCAR.cif !')
        else:
            print('There is no POSCAR or CONTCAR.')
    elif len(sys.argv) == 2:
        abc, elements, numbers, xyzs = get_cell(sys.argv[1])
        cif_name = os.path.basename(sys.argv[1])+'.cif'
        write_cif(cif_name, abc, elements, numbers, xyzs)
        print('%s to %s.cif' %(sys.argv[1], sys.argv[1]))
    else:
        print('Wrong argvs.')

###
if __name__ == '__main__':
    main()
