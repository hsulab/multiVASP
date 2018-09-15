#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: get_CH3ab_paras.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 9/10-2018
#########################################################################
import time
import string
import numpy as np
import pandas as pd
np.set_printoptions(suppress=True)
###
def calc_distance(abc, XYZ1, XYZ2):
    ### XYZ must be absolute coordinates [X, Y, Z]
    #   1----2
    ###
    XYZ1 = (abc.T*XYZ1).T.sum(0)
    XYZ2 = (abc.T*XYZ2).T.sum(0)
    return round(np.linalg.norm(XYZ1-XYZ2), 8)
###
def calc_angle(abc, XYZ1, XYZ2, XYZ3, unit = 'rad'):
    ###   1
    #    /
    #   / ) theta
    #   2 ----- 3
    ###
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
def calc_dihedral(abc, XYZ1, XYZ2, XYZ3, XYZ4, unit='rad'):
    ### dihedral
    #     1
    #    / \
    #   / 5 \
    #  3-----4
    #   \ 6 /
    #    \ /
    #     2
    ###
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
def get_lattice_paras(cif_name, group):
    if 'pure' in cif_name:
        name = cif_name.split('_')[0] + '_' + cif_name.split('_')[1]
        cell = cif_name.split('_')[0].strip('pure')
        dop = 'pure'
    else:
        name = cif_name.split('_')[0] + '_' + cif_name.split('_')[1] + '_' + group
        cell = cif_name.split('_')[0].strip('dop')
        dop = cif_name.split('_')[1]
    lattice_paras = {'name':name, 'cell':cell, 'dop':dop}
    return lattice_paras
###
def get_distance(abc, elements):
    elements_list = list(elements.keys())
    ### distance
    d_para = {}
    for i in range(len(elements_list)):
        for j in range(i+1,len(elements.keys())):
            para_name = []
            para_name = 'd_' + elements_list[i] \
                    + '-' + elements_list[j]
            para_value = calc_distance(abc, \
                    elements[elements_list[i]][1], \
                    elements[elements_list[j]][1])
            d_para[para_name] = para_value
    return d_para
###
def get_angle(abc, elements):
    elements_list = list(elements.keys())
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
                    para_value = calc_angle(abc, \
                            elements[elements_list[i]][1], \
                            elements[elements_list[j]][1], \
                            elements[elements_list[k]][1])
                    a_para[para_name] = para_value
    return a_para
###
def get_dihedral(abc, elements):
    elements_list = list(elements.keys())
    numbers = len(elements.keys())
    ###
    '''
    pairs = []
    for i in range(numbers):
        for j in range(i+1,numbers):
            for k in range(numbers):
                if (k != i and k != j):
                    for l in range(k+1, numbers):
                        if (l!=i and l!=j):
                            pairs.append([i,j,k,l])
    '''
    ### dihedral
    h_para = {}
    for i in range(numbers):
        for j in range(i+1, numbers):
            for k in range(numbers):
                if (k!=i and k!=j):
                    for l in range(k+1, numbers):
                        if (l!=i and l!=j):
                            para_name = 'h_' + elements[elements_list[i]][0] + '-' \
                                    + elements[elements_list[j]][0] + '-' \
                                    + elements[elements_list[k]][0] + '-' \
                                    + elements[elements_list[l]][0]
                            para_value = calc_dihedral(abc, \
                                    elements[elements_list[i]][1], \
                                    elements[elements_list[j]][1], \
                                    elements[elements_list[k]][1], \
                                    elements[elements_list[l]][1])
                            h_para[para_name] = para_value
    return h_para
###
def get_paras(abc, l1, l2, group, group_dict, cif_name, para_type):
    total_paras = {}
    ###
    lattice_paras = get_lattice_paras(cif_name, group)
    total_paras = dict(lattice_paras)
    ###
    elements = dict(group_dict, **l1)
    ###
    if 'd' in para_type:
        d_para = get_distance(abc, elements)
        total_paras = dict(total_paras, **d_para)
    if 'a' in para_type:
        a_para = get_angle(abc, elements)
        total_paras = dict(total_paras, **a_para)
    if 'h' in para_type:
        h_para = get_dihedral(abc, elements)
        total_paras = dict(total_paras, **h_para)
    ###
    return total_paras
###
def main():
    print('')
###
if __name__ == '__main__':
    main()
