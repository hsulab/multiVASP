#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: get_CH3ab_paras.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 9/10-2018
#########################################################################
## system lib
import os
import string
## my script
import pos2cif as p2c
import adjust_atoms as aa
import get_group as gg
### standard contcar form for Rutile    
def std_contcars(CONTCAR, group):
    ### get basic information of a cell
    abc, elements, numbers, xyzs = p2c.get_cell(CONTCAR)
    contcar_name = os.path.basename(CONTCAR)
    dopM = contcar_name.split('_')[-3]
    ### Special edition
    if 'IrO2' in CONTCAR:
        for xyz in xyzs:
            if xyz[1] > 0.75:
                xyz[1] = xyz[1] -1
    ## round xyz by 8
    for xyz in xyzs:
        for i in range(len(xyz)):
            xyz[i] = round(xyz[i], 8)
    ## std xyz
    for xyz in xyzs:
        if xyz[2] >= 0.99:
            xyz[2] -= 1.00
    ### make dict
    ## get element name and number
    element_dict = {}
    count = 0
    for element, number in zip(elements, numbers):
        for i in range(int(number)):
            element_dict[element + str(i+1)] = xyzs[count]
            count += 1
    ###
    metals = ['Ti', 'V', 'Ge', 'Mo', 'Ru', 'Rh', 'Os', 'Ir'] 
    ### first layer
    H_dict={}
    C_dict={}
    O_dict={}
    M_dict={}
    for element_name in element_dict.keys():
        if element_name.strip(string.digits) == 'H':
            H_dict[element_name] = element_dict[element_name]
        elif element_name.strip(string.digits) == 'C':
            C_dict[element_name] = element_dict[element_name]
        elif element_name.strip(string.digits) == 'O':
            O_dict[element_name] = element_dict[element_name]
        elif element_name.strip(string.digits) in metals:
            M_dict[element_name] = element_dict[element_name]
    ### get_layer
    l1, l2, xyzs = aa.adjust_atoms(dopM, element_dict, O_dict, M_dict)
    ###
    group_dict = gg.get_group(H_dict, C_dict, group)
    ###
    return abc, elements, numbers, xyzs, l1, l2, group_dict
###
def main():
    print('')
###
if __name__ == '__main__':
    main()
