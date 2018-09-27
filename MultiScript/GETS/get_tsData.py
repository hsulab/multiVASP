#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: get_tsData.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 二  4/24 16:38:38 2018
#########################################################################
###
import numpy as np
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
def ts_contcar_std(CONTCAR):
    abc = []
    xyz = []
    ### get abc and xyz list
    with open(CONTCAR, 'r') as f:
        content = f.readlines()
        for i in range(2,5):
            a_abc = []
            for cor in content[i].strip('\n').split(' '):
                if cor not in ['']: 
                    a_abc.append(float(cor))
            abc.append(a_abc)
        for i in range(9,62):
            a_xyz = [] 
            for cor in content[i].strip('\n').split(' '):
                if cor not in ['','T','F']: 
                    a_xyz.append(float(cor)) ###
            xyz.append(a_xyz)
    ### turn type to np.array
    xyz = np.array(xyz)
    abc = np.array(abc)
    ### make z less than 0.95, x & y > 0, 
    #   which make Rutile srtucture the same
    for i in range(len(xyz)):
        if xyz[i][0] < float(0):
            xyz[i][0] += 1
        if xyz[i][1] < float(0):
            xyz[i][1] += 1
        if xyz[i][2] >= float(0.95):
            xyz[i][2] -= 1
    return abc, xyz
###
def cell_information(CONTCAR):
    ### get CH4, M and O xyz
    CH4_xyz = xyz[0:5]
    O_xyz = xyz[5:37]
    M_xyz = xyz[37:53]
    ### get O1, C, H1, H2, H3/H4
    #   
    #    O1 ~   H1 
    #    /\     \  H3 H4
    #   /  M3    \ / /
    #  /    \     C
    # M2     O3    \
    #  \     |      H2
    #   O2---M1
    ### get O1
    O_xyz_sortbyz = O_xyz[O_xyz[:,2].argsort()]
    ab_O_xyz = O_xyz_sortbyz[-2:]
    ab_O_xyz_sortbyx = ab_O_xyz[ab_O_xyz[:,0].argsort()]
    ###
    M_xyz_sortbyz = M_xyz[M_xyz[:,2].argsort()]
    top_M_xyz = M_xyz_sortbyz[-4:]
    #
    dop_M_xyz_sortbyx = dop_M_xyz[dop_M_xyz[:,0].argsort()]
    dop_s1_xyz = dop_M_xyz_sortbyx[2]
    dop_s2_xyz = dop_M_xyz_sortbyx[1]
    dop_s3_xyz = dop_M_xyz_sortbyx[3]
    #
    ab_O_b_xyz = ab_O_xyz_sortbyx[1]
    ####
    return abc, xyz, dop_s1_xyz, dop_s2_xyz, dop_s3_xyz, ab_O_b_xyz
###

###
def main():
    print()
###
if __name__ == '__main__':
    main()
