#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: get_CH3ab_paras.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 9/10-2018
#########################################################################
import time
import os
import shutil
import string
import numpy as np
import pandas as pd
np.set_printoptions(suppress=True)
##
import pos2cif as p2c
### standard contcar form for Rutile    
def std_cons(CONTCAR):
    abc, elements, numbers, xyzs = p2c.get_cell(CONTCAR)
    contcar_name = os.path.basename(CONTCAR)
    dopM = contcar_name.split('_')[-3]
    ### Special edition
    if 'IrO2' in CONTCAR:
        for xyz in xyzs:
            if xyz[1] > 0.75:
                xyz[1] = xyz[1] -1
    ### round xyz by 8
    for xyz in xyzs:
        for i in range(len(xyz)):
            xyz[i] = round(xyz[i], 8)
    ### std xyz
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
    ##
   ### adjust atom location
    def mv_xyz(xyz, d, s):
        if d == 'x':
            xyz[0] = xyz[0] + s
        elif d == 'y':
            xyz[1] = xyz[1] + s
        elif d == 'z':
            xyz[2] = xyz[2] + s
        return xyz
    ##
    O2_dict, M2_dict, l1 = get_layer(O_dict, M_dict)
    O3_dict, M3_dict, l2 = get_layer(O2_dict, M2_dict)
    CH3_dict = get_CH3(H_dict, C_dict)
    ##  C   D
    ##    A   B
    ##      C   D
    def adjust_AtomPair(A, B, C, D, loc):
        if D[1][0] < A[1][0]:
            C[1] = mv_xyz(C[1], 'x', 1)
            D[1] = mv_xyz(D[1], 'x', 1)
        if C[1][0] > B[1][0]:
            C[1] = mv_xyz(C[1], 'x', -1)
            D[1] = mv_xyz(D[1], 'x', -1)
        if loc == 1:
            if C[1][0] < A[1][0] and (A[1][0]<D[1][0]<B[1][0]):
                C[1] = mv_xyz(C[1], 'x', 1)
                C, D = D, C
        elif loc == -1:
            if (A[1][0]<C[1][0]<B[1][0]) and B[1][0]<D[1][0]:
                D[1] = mv_xyz(D[1], 'x', -1)
                C, D = D, C
        return C, D
    ## set O1 O2 unchanged
    if l1['O3'][1][1] < l1['M1'][1][1]:
        l1['O3'][1] = mv_xyz(l1['O3'][1], 'y', 1)
        l1['O4'][1] = mv_xyz(l1['O4'][1], 'y', 1)
        l1['O3'], l1['O5'] = l1['O5'], l1['O3']
        l1['O4'], l1['O6'] = l1['O6'], l1['O4']
    ##
    if l1['O1'][1][0] > l1['M1'][1][0]:
        l1['O2'][1] = mv_xyz(l1['O2'][1], 'x', -1)
        l1['O1'], l1['O2'] = l1['O2'], l1['O1']
    ##
    if l1['M3'][0].strip(string.digits) == dopM:
        l1['M4'][1] = mv_xyz(l1['M4'][1], 'x', -1)
        l1['M3'], l1['M4'] = l1['M4'], l1['M3']
    ##
    l1['O3'], l1['O4'] = adjust_AtomPair(l1['O1'], l1['O2'], \
            l1['O3'], l1['O4'], 1)
    ##
    l1['O5'], l1['O6'] = adjust_AtomPair(l1['O1'], l1['O2'], \
            l1['O5'], l1['O6'], 1)
    ##
    l1['M1'], l1['M2'] = adjust_AtomPair(l1['O1'], l1['O2'], \
            l1['M1'], l1['M2'], 1)
    ##
    l1['M3'], l1['M4'] = adjust_AtomPair(l1['M1'], l1['M2'], \
            l1['M3'], l1['M4'], -1)
    #l1['M3'], l1['M4'] = l1['M4'], l1['M3']
    ##
    l1['O7'], l1['O8'] = adjust_AtomPair(l1['M1'], l1['M2'], \
            l1['O7'], l1['O8'], -1)
    ##
    l2['O1'], l2['O2'] = adjust_AtomPair(l1['M1'], l1['M2'], \
            l2['O1'], l2['O2'], -1)
    ##
    ##
    std_layer = []
    for i in l1.values():
        std_layer.append(i)
    for i in l2.values():
        std_layer.append(i)
    ### change xyz
    for A in std_layer:
        element_dict[A[0]] = A[1]
    ##
    xyzs = []
    for key, value in element_dict.items():
        xyzs.append(value)
    ### round xyz by 8
    for xyz in xyzs:
        for i in range(len(xyz)):
            xyz[i] = round(xyz[i], 8)
    ###
    cif_name = os.path.basename(CONTCAR) + '.cif'
    p2c.write_cif(CONTCAR+'.cif', abc, elements, numbers, xyzs)
    return abc, l1, l2, CH3_dict, cif_name
###
def get_CH3ab_paras(abc, l1, l2, CH3, cif_name):
    ### XYZ must be absolute coordinates [X, Y, Z]
    #   1----2
    ##
    def get_distance(abc, XYZ1, XYZ2):
        XYZ1 = (abc.T*XYZ1).T.sum(0)
        XYZ2 = (abc.T*XYZ2).T.sum(0)
        return round(np.linalg.norm(XYZ1-XYZ2), 8)
    ###   1
    #    /
    #   / ) theta
    #   2 ----- 3
    ##
    def get_angle(abc, XYZ1, XYZ2, XYZ3, unit = 'rad'):
        XYZ1 = (abc.T*XYZ1).T.sum(0)
        XYZ2 = (abc.T*XYZ2).T.sum(0)
        XYZ3 = (abc.T*XYZ3).T.sum(0)
        vec1 = XYZ1 - XYZ2
        vec2 = XYZ3 - XYZ2
        costheta =  np.dot(vec1, vec2.T)/\
                (np.linalg.norm(vec1)*np.linalg.norm(vec2))
        theta_rad = np.arccos(costheta)
        if unit == 'rad':
            return round(theta_rad, 8)
        else:
            return round(theta_rad/np.pi*180, 4)
    ### dihedral
    #     1
    #    / \
    #   / 5 \
    #  3-----4
    #   \ 6 /
    #    \ /
    #     2
    def get_dihedral(abc, XYZ1, XYZ2, XYZ3, XYZ4, unit='rad'):
        XYZ1 = (abc.T*XYZ1).T.sum(0)
        XYZ2 = (abc.T*XYZ2).T.sum(0)
        XYZ3 = (abc.T*XYZ3).T.sum(0)
        XYZ4 = (abc.T*XYZ4).T.sum(0)
        ##
        a=-((XYZ1[0]-XYZ4[0])*(XYZ4[0]-XYZ3[0])+\
                (XYZ1[1]-XYZ4[1])*(XYZ4[1]-XYZ3[1])+\
                (XYZ1[2]-XYZ4[2])*(XYZ4[2]-XYZ3[2]))/\
                ((XYZ4[0]-XYZ3[0])**2+\
                (XYZ4[1]-XYZ3[1])**2+\
                (XYZ4[2]-XYZ3[2])**2)
        #
        b=-((XYZ2[0]-XYZ4[0])*(XYZ4[0]-XYZ3[0])+\
                (XYZ2[1]-XYZ4[1])*(XYZ4[1]-XYZ3[1])+\
                (XYZ2[2]-XYZ4[2])*(XYZ4[2]-XYZ3[2]))/\
                ((XYZ4[0]-XYZ3[0])**2+\
                (XYZ4[1]-XYZ3[1])**2+\
                (XYZ4[2]-XYZ3[2])**2)
        ##
        vec1 = [XYZ1[0]-XYZ4[0]+(XYZ4[0]-XYZ3[0])*a,\
                XYZ1[1]-XYZ4[1]+(XYZ4[1]-XYZ3[1])*a,\
                XYZ1[2]-XYZ4[2]+(XYZ4[2]-XYZ4[2])*a]
        vec1 = np.array(vec1)
        #
        vec2 = [XYZ1[0]-XYZ4[0]+(XYZ4[0]-XYZ3[0])*b,\
                XYZ1[1]-XYZ4[1]+(XYZ4[1]-XYZ3[1])*b,\
                XYZ1[2]-XYZ4[2]+(XYZ4[2]-XYZ4[2])*b]
        vec2 = np.array(vec2)
        ##
        costheta =  np.dot(vec1, vec2.T)/\
                (np.linalg.norm(vec1)*np.linalg.norm(vec2))
        theta_rad = np.arccos(costheta)
        if unit == 'rad':
            return round(theta_rad, 8)
        else:
            return round(theta_rad/np.pi*180, 4)
    ###
    if 'pure' in cif_name:
        name = cif_name.split('_')[0] + '_' + cif_name.split('_')[1]
        cell = cif_name.split('_')[0].strip('pure')
        dop = 'pure'
    else:
        name = cif_name.split('_')[0] + '_' + cif_name.split('_')[1] + '_' + 'CH3ab'
        cell = cif_name.split('_')[0].strip('dop')
        dop = cif_name.split('_')[1]
    suf_para = {'name':name, 'cell':cell, 'dop':dop}
    ###
    elements = dict(CH3, **l1)
    elements_list = list(elements.keys())
    ### distance
    d_para = {}
    for i in range(len(elements.keys())):
        for j in range(i+1,len(elements.keys())):
            para_name = []
            para_name = 'd_' + elements_list[i] \
                    + '-' + elements_list[j]
            para_value = get_distance(abc, \
                    elements[elements_list[i]][1], \
                    elements[elements_list[j]][1])
            d_para[para_name] = para_value
    ### angle
    a_para = {}
    for i in range(len(elements.keys())):
        for j in range(len(elements.keys())):
            for k in range(len(elements.keys())):
                if not (elements_list[i] == elements_list[j] or
                        elements_list[j] == elements_list[k] or
                        elements_list[i] == elements_list[k]):
                    para_name = 'a_' + elements_list[i] + \
                            '-' + elements_list[j] + \
                            '-' + elements_list[k]
                    para_value = get_angle(abc, \
                            elements[elements_list[i]][1], \
                            elements[elements_list[j]][1], \
                            elements[elements_list[k]][1])
                    a_para[para_name] = para_value
    ### dihedral
    '''
    h_para = {}
    for i in range(len(elements.keys())):
        for j in range(i+1,len(elements.keys())):
            for k in range(i+2,len(elements.keys())):
                for l in range(i+3,len(elements.keys())):
                    para_name = 'h_' + elements[elements_list[i]][0] + '-' \
                            + elements[elements_list[j]][0] + '-' \
                            + elements[elements_list[k]][0] + '-' \
                            + elements[elements_list[l]][0]
                    para_value = get_dihedral(abc, \
                            elements[elements_list[i]][1], \
                            elements[elements_list[j]][1], \
                            elements[elements_list[k]][1], \
                            elements[elements_list[l]][1])
                    h_para[para_name] = para_value
    '''
    ###
    CH3ab_paras = dict(suf_para, **d_para)
    CH3ab_paras = dict(CH3ab_paras, **a_para)
    return CH3ab_paras
    
###
def main():
    cons_dir = './data/CH3ab_data/CH3ab_cons'
    cifs_dir = './data/CH3ab_data/CH3ab_cifs'
    ###
    MS_dir = os.path.join(os.path.expanduser('~'), 'Documents/USRP/DopRutile_Files/Documents')
    MS_CH3ab_cifs_dir = os.path.join(MS_dir, 'CH3ab_cifs')
    ###
    CH3ab_csv_name = 'CH3ab_data_' + time.strftime("%Y%m%d", time.localtime()) + '.csv'
    CH3ab_csv = os.path.join(os.path.expanduser('~'), 'Desktop/' + CH3ab_csv_name)
    ###
    ### pd.DataFrame
    row_index = 1
    CH3ab_df = []
    ###
    for con_name in os.listdir(cons_dir):
        print(con_name)
        con = os.path.join(cons_dir, con_name)
        ms_xsd = os.path.join(MS_CH3ab_cifs_dir, os.path.basename(con)+'.xsd')
        ###
        abc, l1, l2, CH3, cif_name = std_cons(con)
        CH3ab_paras = get_CH3ab_paras(abc, l1, l2, CH3, cif_name)
        if row_index == 1:
            CH3ab_df = pd.DataFrame(columns=tuple(CH3ab_paras.keys()))
        CH3ab_df.loc[row_index] = list(CH3ab_paras.values())
        row_index += 1
        ###
        cif = os.path.join(cifs_dir, cif_name)
        if not os.path.exists(ms_xsd):
            ms_cif = os.path.join(MS_CH3ab_cifs_dir, cif_name)
            shutil.copy(con+'.cif', cif)
            shutil.move(con+'.cif', ms_cif)
        else:
            os.remove(con+'.cif')
    ###
    CH3ab_df = CH3ab_df.sort_values(by=['cell', 'name', 'dop'], ascending=True)
    CH3ab_df = CH3ab_df.reset_index(drop=True)
    print(CH3ab_df.shape[1])
    CH3ab_df.to_csv(CH3ab_csv)
###
if __name__ == '__main__':
    main()
