#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: get_Hab3_paras.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 五  4/27 11:02:57 2018
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
            xyz[1] = 1 - xyz[1]
    ### round xyz by 8
    for xyz in xyzs:
        for i in range(len(xyz)):
            xyz[i] = round(xyz[i], 8)
    ### std xyz
    for xyz in xyzs:
        if xyz[2] >= 0.99:
            xyz[2] -= 1.00
    ### make dict
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
    O_dict={}
    M_dict={}
    for element_name in element_dict.keys():
        if element_name.strip(string.digits) == 'H':
            H_dict[element_name] = element_dict[element_name]
        elif element_name.strip(string.digits) == 'O':
            O_dict[element_name] = element_dict[element_name]
        elif element_name.strip(string.digits) in metals:
            M_dict[element_name] = element_dict[element_name]
    ##
    def tuple2dict(t):
        d = {}
        for name, xyz in t:
            d[name] = xyz
        return d
    ##
    def get_layer(O_dict, M_dict):
        ## 
        O_dict_z = sorted(O_dict.items(), key=lambda e:e[1][2], reverse=True)
        # get O1 O2
        O12_dict = tuple2dict(O_dict_z[:2])
        O12_dict_x = sorted(O12_dict.items(), key=lambda e:e[1][0], reverse=True)
        O1_tuple = O12_dict_x[1]
        O2_tuple = O12_dict_x[0]
        # get O3 O4 O5 O6
        O3456_dict = tuple2dict(O_dict_z[2:6])
        O3456_dict_y = sorted(O3456_dict.items(), key=lambda e:e[1][1], reverse=True)
        #
        O34_dict = tuple2dict(O3456_dict_y[-2:])
        O34_dict_x = sorted(O34_dict.items(), key=lambda e:e[1][0], reverse=True)
        O3_tuple = O34_dict_x[1]
        O4_tuple = O34_dict_x[0]
        #
        O56_dict = tuple2dict(O3456_dict_y[:2])
        O56_dict_x = sorted(O56_dict.items(), key=lambda e:e[1][0], reverse=True)
        O5_tuple = O56_dict_x[1]
        O6_tuple = O56_dict_x[0]
        # get O7 O8
        O78_dict = tuple2dict(O_dict_z[6:8])
        O78_dict_x = sorted(O78_dict.items(), key=lambda e:e[1][0], reverse=True)
        O7_tuple = O78_dict_x[1]
        O8_tuple = O78_dict_x[0]
        ## get M1 M2 M3 M4
        M_dict_z = sorted(M_dict.items(), key=lambda e:e[1][2], reverse=True)
        M1234_dict = tuple2dict(M_dict_z[:4])
        M1234_dict_y = sorted(M1234_dict.items(), key=lambda e:e[1][1], reverse=True)
        #
        M12_dict = tuple2dict(M1234_dict_y[-2:])
        M12_dict_x = sorted(M12_dict.items(), key=lambda e:e[1][0], reverse=True)
        M1_tuple = M12_dict_x[1]
        M2_tuple = M12_dict_x[0]
        #
        M34_dict = tuple2dict(M1234_dict_y[:2])
        M34_dict_x = sorted(M34_dict.items(), key=lambda e:e[1][0], reverse=True)
        M3_tuple = M34_dict_x[1]
        M4_tuple = M34_dict_x[0]
        ##
        layer = {}
        layer['O1'] = list(O1_tuple)
        O_dict.pop(O1_tuple[0])
        layer['O2'] = list(O2_tuple)
        O_dict.pop(O2_tuple[0])
        layer['O3'] = list(O3_tuple)
        O_dict.pop(O3_tuple[0])
        layer['O4'] = list(O4_tuple)
        O_dict.pop(O4_tuple[0])
        layer['O5'] = list(O5_tuple)
        O_dict.pop(O5_tuple[0])
        layer['O6'] = list(O6_tuple)
        O_dict.pop(O6_tuple[0])
        layer['O7'] = list(O7_tuple)
        O_dict.pop(O7_tuple[0])
        layer['O8'] = list(O8_tuple)
        O_dict.pop(O8_tuple[0])
        layer['M1'] = list(M1_tuple)
        M_dict.pop(M1_tuple[0])
        layer['M2'] = list(M2_tuple)
        M_dict.pop(M2_tuple[0])
        layer['M3'] = list(M3_tuple)
        M_dict.pop(M3_tuple[0])
        layer['M4'] = list(M4_tuple)
        M_dict.pop(M4_tuple[0])
        return O_dict, M_dict, layer
    ###
    def get_Hab(H_dict):
        Hab_dict = {}
        #
        H_dict_y = sorted(H_dict.items(), key=lambda e:e[1][1], reverse=True)
        H1_tuple = H_dict_y[0]
        #
        Hab_dict['H1'] = list(H1_tuple)
        return Hab_dict
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
    Hab_dict = get_Hab(H_dict)
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
    return abc, l1, l2, Hab_dict, cif_name
###
def get_Hab3_paras(abc, l1, l2, Hab, cif_name):
    ### XYZ must be absolute coordinates [X, Y, Z]
    def get_distance(abc, XYZ1, XYZ2):
        XYZ1 = (abc.T*XYZ1).T.sum(0)
        XYZ2 = (abc.T*XYZ2).T.sum(0)
        return round(np.linalg.norm(XYZ1-XYZ2), 8)
    ###   1
    #    /
    #   / ) theta
    #   2 ----- 3
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
    ###
    if 'pure' in cif_name:
        name = cif_name.split('_')[0] + '_' + cif_name.split('_')[1]+'2'
        cell = cif_name.split('_')[0].strip('pure')
        dop = 'pure'
    else:
        name = cif_name.split('_')[0] + '_' + cif_name.split('_')[1] + '_Hab3'
        cell = cif_name.split('_')[0].strip('dop')
        dop = cif_name.split('_')[1]
    ### get geometry paras
    ## d_O2_H1
    dH1_O2 = get_distance(abc, Hab['H1'][1], l1['O2'][1])
    dO2_M4 = get_distance(abc, l1['O2'][1], l1['M4'][1])
    dM4_l2O2 = get_distance(abc, l1['M4'][1], l2['O2'][1])
    ## angle
    aH1_O2_M4 = get_angle(abc, Hab['H1'][1], l1['O2'][1], l1['M4'][1])
    aO8_O2_H1 = get_angle(abc, l1['O8'][1], l1['O2'][1], Hab['H1'][1]) 
    ##
    Hab3_paras = [cell, dop, name, dH1_O2, dO2_M4, dM4_l2O2, \
            aH1_O2_M4, aO8_O2_H1]
    return Hab3_paras
    
    
###
def main():
    cons_dir = './data/Hab3_data/Hab3_cons'
    cifs_dir = './data/Hab3_data/Hab3_cifs'
    ###
    MS_dir = os.path.join(os.path.expanduser('~'), 'Documents/USRP/DopRutile_Files/Documents')
    MS_Hab3_cifs_dir = os.path.join(MS_dir, 'Hab3_cifs')
    ###
    Hab3_csv_name = 'Hab3_data_' + time.strftime("%Y%m%d", time.localtime()) + '.csv'
    Hab3_csv = os.path.join(os.path.expanduser('~'), 'Desktop/' + Hab3_csv_name)
    ### pd.DataFrame
    Hab3_df = pd.DataFrame(columns=('cell', 'dop', 'name', 'dH1_O2', \
            'dO2_M4', 'dM4_l2O2', 'aH1_O2_M4' ,'aO8_O2_H1'))
    row_index = 1
    ###
    for con_name in os.listdir(cons_dir):
        print(con_name)
        con = os.path.join(cons_dir, con_name)
        ms_xsd = os.path.join(MS_Hab3_cifs_dir, os.path.basename(con)+'.xsd')
        ###
        abc, l1, l2, CH4, cif_name = std_cons(con)
        Hab3_paras = get_Hab3_paras(abc, l1, l2, CH4, cif_name)
        Hab3_df.loc[row_index] = Hab3_paras
        row_index += 1
        ##
        cif = os.path.join(cifs_dir, cif_name)
        if not os.path.exists(ms_xsd):
            ms_cif = os.path.join(MS_Hab3_cifs_dir, cif_name)
            shutil.copy(con+'.cif', cif)
            shutil.move(con+'.cif', ms_cif)
        else:
            os.remove(con+'.cif')
    ###
    Hab3_df = Hab3_df.sort_values(by=['cell','dop', 'name'], ascending=True)
    Hab3_df = Hab3_df.reset_index(drop=True)
    Hab3_df.to_csv(Hab3_csv)
###
if __name__ == '__main__':
    main()
