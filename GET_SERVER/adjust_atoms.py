#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: adjust_elements.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 五  9/14 16:46:00 2018
#########################################################################
import string
import get_layer as gl
###
def adjust_atoms(dopM, element_dict, O_dict, M_dict):
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
    O2_dict, M2_dict, l1 = gl.get_layer(O_dict, M_dict)
    O3_dict, M3_dict, l2 = gl.get_layer(O2_dict, M2_dict)
    ###
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
    ### set O1 O2 unchanged
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
    ### adjust layer1
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
    ### adjust layer2
    l2['O1'], l2['O2'] = adjust_AtomPair(l1['M1'], l1['M2'], \
            l2['O1'], l2['O2'], -1)
    ###
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
    return l1, l2, xyzs
###
def main():
    print('')
###
if __name__ == '__main__':
    main()
