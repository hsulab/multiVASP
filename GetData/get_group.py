#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: get_CH.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 五  9/14 17:03:30 2018
#########################################################################
def tuple2dict(t):
    d = {}
    for name, xyz in t:
        d[name] = xyz
    return d
###
def get_group(H_dict, C_dict, group):
    def get_Hab(H_dict):
        Hab_dict = {}
        H_dict_y = sorted(H_dict.items(), key=lambda e:e[1][1], reverse=True)
        H1_tuple = H_dict_y[0]
        Hab_dict['H1'] = list(H1_tuple)
        return Hab_dict
    ###
    def get_CH3(H_dict, C_dict):
        CH3_dict = {}
        ###
        H_dict_y = sorted(H_dict.items(), key=lambda e:e[1][1], reverse=True)
        H1_tuple = H_dict_y[2]
        H34_dict = tuple2dict(H_dict_y[0:2])
        H34_dict_x = sorted(H34_dict.items(), key=lambda e:e[1][0], reverse=True)
        H3_tuple = H34_dict_x[0]
        H4_tuple = H34_dict_x[1]
        ##
        C_dict_x = sorted(C_dict.items(), key=lambda e:e[1][0], reverse=True)
        ##
        CH3_dict['C'] = list(C_dict_x[0])
        CH3_dict['H1'] = list(H1_tuple)
        CH3_dict['H3'] = list(H3_tuple)
        CH3_dict['H4'] = list(H4_tuple)
        return CH3_dict
    ###
    def get_CH4(H_dict, C_dict):
        CH4_dict = {}
        ###
        H_dict_y = sorted(H_dict.items(), key=lambda e:e[1][1], reverse=True)
        H1_tuple = H_dict_y[3]
        H2_tuple = H_dict_y[0]
        H34_dict = tuple2dict(H_dict_y[1:3])
        H34_dict_x = sorted(H34_dict.items(), key=lambda e:e[1][0], reverse=True)
        H3_tuple = H34_dict_x[0]
        H4_tuple = H34_dict_x[1]
        ##
        C_dict_x = sorted(C_dict.items(), key=lambda e:e[1][0], reverse=True)
        ##
        CH4_dict['C'] = list(C_dict_x[0])
        CH4_dict['H1'] = list(H1_tuple)
        CH4_dict['H2'] = list(H2_tuple)
        CH4_dict['H3'] = list(H3_tuple)
        CH4_dict['H4'] = list(H4_tuple)
        return CH4_dict
    ###
    if group == 'Hab2' or group == 'Hab3':
        group_dict = get_Hab(H_dict)
    elif group == 'CH3ab' or group == 'CH3ab2':
        group_dict = get_CH3(H_dict, C_dict)
    elif group == 'ts' or group == 'fs' or group == 'tsra':
        group_dict = get_CH4(H_dict, C_dict)
    else:
        group_dict = {}
    ###
    return group_dict
###
def main():
    print('')
###
if __name__ == '__main__':
    main()
