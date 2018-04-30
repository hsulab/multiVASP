#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: get_ts_paras.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 五  4/27 11:02:57 2018
#########################################################################
import os
import shutil
import string
import numpy as np
np.set_printoptions(suppress=True)
##
import pos2cif as p2c
### XYZ must be absolute coordinates [X, Y, Z]
def get_distance(XYZ1, XYZ2):
    return np.linalg.norm(XYZ1-XYZ2)
###   1
#    /
#   / ) theta
#   2 ----- 3
def get_angle(XYZ1, XYZ2, XYZ3, unit = 'rad'):
    vec1 = XYZ1 - XYZ2
    vec2 = XYZ3 - XYZ2
    costheta =  np.dot(vec1, vec2.T)/\
            (np.linalg.norm(vec1)*np.linalg.norm(vec2))
    theta_rad = np.arccos(costheta)
    if unit == 'rad':
        return theta_rad
    else:
        return theta_rad/np.pi*180
### standard contcar form for Rutile    
def std_cons(CONTCAR):
    abc, elements, numbers, xyzs = p2c.get_cell(CONTCAR)
    ### Special edition
    if 'dopIrO2' in CONTCAR:
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
    O_dict={}
    M_dict={}
    for element_name in element_dict.keys():
        if element_name.strip(string.digits) == 'O':
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
    O1 = list(O1_tuple)
    O2 = list(O2_tuple)
    O3 = list(O3_tuple)
    O4 = list(O4_tuple)
    O5 = list(O5_tuple)
    O6 = list(O6_tuple)
    O7 = list(O7_tuple)
    O8 = list(O8_tuple)
    M1 = list(M1_tuple)
    M2 = list(M2_tuple)
    M3 = list(M3_tuple)
    M4 = list(M4_tuple)
    ##
    def mv_xyz(xyz, d, s):
        if d == 'x':
            xyz[0] = xyz[0] + s
        elif d == 'y':
            xyz[1] = xyz[1] + s
        elif d == 'z':
            xyz[2] = xyz[2] + s
        return xyz
    ##
    if M3[1][0] < M1[1][0] < M4[1][0] < M2[1][0]:
        if M1[1][0] < O1[1][0]:
            M1[1] = mv_xyz(M1[1], 'x', 1)
            M1[1], M2[1] = M2[1], M1[1]
            M3[1] = mv_xyz(M3[1], 'x', 1)
            M3[1], M4[1] = M4[1], M3[1]
    ##
    first_layer = [M1, M2, M3, M4]
    ### change xyz
    for A in first_layer:
        element_dict[A[0]] = A[1]
    ##
    xyzs = []
    for key, value in element_dict.items():
        xyzs.append(value)

        print()
    
    ###
    cif_name = os.path.basename(CONTCAR) + '.cif'
    p2c.write_cif(CONTCAR+'.cif', abc, elements, numbers, xyzs)
    return cif_name
###
def get_ts_cifs():
    cons_dir = './data/ts_data/ts_cons'
    cifs_dir = './data/ts_data/ts_cifs'
    MS_dir = os.path.join(os.path.expanduser('~'), 'Documents/USRP/DopRutile_Files/Documents')
    MS_ts_cifs_dir = os.path.join(MS_dir, 'ts_cifs')
    for con in os.listdir(cons_dir):
        print(con)
        con = os.path.join(cons_dir, con)
        cif_name = std_cons(con)
        cif = os.path.join(cifs_dir, cif_name)
        ms_cif = os.path.join(MS_ts_cifs_dir, cif_name)
        shutil.copy(con+'.cif', cif)
        shutil.move(con+'.cif', ms_cif)
###
def main():
    get_ts_cifs()



###
if __name__ == '__main__':
    main()
