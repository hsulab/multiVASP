#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: readlog.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六 10/ 6 15:54:32 2018
#########################################################################
def read_las(las, n_top):
    with open(las, 'r') as f:
        content = f.readlines()
        'Get Features Location'
        fea_startline = 0
        fea_endline = 0
        for nl in range(len(content)):
            if 'Features' in content[nl]:
                fea_startline = nl
                break
        for nl in range(fea_startline, len(content)):
            if 'Summary' in content[nl]:
                fea_endline = nl
                break
        'Get Feas Dict'
        feas_dict = {}
        for nl in range(fea_startline+1, fea_endline):
            if len(content[nl].strip()) != 0:
                line = content[nl].split('|')
                if len(line) == 2:
                    fea1 = line[0].split('-->')
                    fea2 = line[1].split('-->')
                    feas_dict[fea1[0].strip(' ')] =  float(fea1[1])
                    feas_dict[fea2[0].strip(' ')] =  float(fea2[1])
                else:
                    print('Wrong in %d!' %nl)
        'Get Top N'
        if 0 < n_top <= len(feas_dict.keys()):
            count = 0
            top_feas = {}
            for key, value in feas_dict.items():
                if count < n_top:
                    top_feas[key] = value
                    count += 1
                else:
                    break
            return top_feas
        elif n_top > len(feas_dict.keys()):
            return feas_dict
        else:
            print('Wrong number!')
            return 0
###
if __name__ == '__main__':
    las = './Logs/las_20181008.txt'
    print(read_las(las, 30))
