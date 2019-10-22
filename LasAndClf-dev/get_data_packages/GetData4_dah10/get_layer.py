#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: get_layer.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 五  9/14 17:03:09 2018
#########################################################################
def tuple2dict(t):
    d = {}
    for name, xyz in t:
        d[name] = xyz
    return d
def sortbyaxis(d, a, r, m='T'): # d-dict a-axis r-rank m-method
    axis = {'x':0,'y':1,'z':2}
    msort = {'T':True, 'F':False}
    ret = sorted(d, key=lambda e:e[1][axis[a]], reverse=msort[m])
    return tuple2dict(ret[:r])
### get_layer
def get_layer(O_dict, M_dict):
        #Os = O_dict
        #Ms = M_dict
        #O1_new = sortbyaxis(sortbyaxis(Os, 'z', 2), 'x', 2)[1]
        #O2_new = sortbyaxis(sortbyaxis(Os, 'z', 2), 'x', 2)[0]
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

        'get a dict of list element'
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
def main():
    print('')
###
if __name__ == '__main__':
    main()
