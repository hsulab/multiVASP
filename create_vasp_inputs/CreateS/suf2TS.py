#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: sufH2ab.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 四  3/29 16:41:51 2018
#########################################################################
'''
*Usage*

'''

import numpy as np
import os
import re
import shutil
import sys

import CreateCars
import CheckOut

def cal_CH4_xyz(CONTCAR, tstype):
    'Get TStype'
    if tstype == 'ts':
        theta= 109.5/2
        OH_distance = 1.2 # When coming across <invalid sqrt>, change this term.
        H1C_distance = 1.5
        CM_distance = 2.4
    elif tstype == 'ts_ra':
        theta= 109.5/2
        OH_distance = 1.2
        H1C_distance = 1.5
        CM_distance = 3.2
    else:
        print('Something wrong with the tstype.')
        return 0

    # get xyz, s1 is M.
    abc, xyz, s1, s2, s3, abO = CreateCars.cell_info(CONTCAR)

    # calculate in D-coordinate 3x3
    s2_abO = (abc.T*abO).T - (abc.T*s2).T 
    s3_abO = (abc.T*abO).T - (abc.T*s3).T
    abO_s1 = (abc.T*s1).T - (abc.T*abO).T 

    # e1, e2, e22, e3, 1x3
    e1 = (s2_abO + s3_abO) / np.linalg.norm(s2_abO + s3_abO) # normalized
    e1 = e1.sum(0)
    e2 = abO_s1 / np.linalg.norm(abO_s1) # normalized
    e2 = e2.sum(0)
    e1dote2 = np.dot(e1, e2.T)

    #
    ''' *old way*
    y_e2 = np.sqrt(1.0**2*(1-np.cos(np.pi/2)**2)/(1-e1dote2**2))
    x_e1 = 1.0*np.cos(np.pi/2) - y_e2*e1dote2
    e22 = x_e1*e1 + y_e2*e2
    e22 = e22/np.linalg.norm(e22)
    '''
    e22 = -e1dote2*e1+e2
    e22 = e22 / np.linalg.norm(e22)

    #
    e3 = np.dot(np.linalg.inv(np.vstack((np.vstack((e1, e22)) ,[1, 0, 0]))), \
            [0, 0, 1])
    e3 = e3.T/np.linalg.norm(e3)

    ###
    # set abO as O , e1 as x e22 as y 
    #    H1
    #   /  \  H3 H4
    #  /    \ / /
    # O      C
    #  \     /\
    #   \---M  H2
    ###

    # get M
    rad_e1Oe2 = np.arccos(np.dot(e1, e2.T))
    M_e1x = np.linalg.norm(abO_s1)*np.cos(rad_e1Oe2) 
    M_e22y = np.linalg.norm(abO_s1)*np.sin(rad_e1Oe2)
    M_XYZ = (abc.T*abO).T.sum(0) + M_e1x*e1 + M_e22y*e22

    # get H1
    H1_e1x = np.sqrt(OH_distance**2/(1+np.tan(theta/180*np.pi)**2))
    H1_e22y = H1_e1x*np.tan(theta/180*np.pi)
    H1_XYZ = (abc.T*abO).T.sum(0) + H1_e1x*e1 + H1_e22y*e22

    # calc distance between M and H1
    v_MH1 = M_XYZ - H1_XYZ
    d_MH1 = np.linalg.norm(v_MH1)

    # get C
    def insec(p1,r1,p2,r2):
        # reference: https://www.jb51.net/article/150362.htm
        x, y, R = p1[0], p1[1], r1
        a, b, S = p2[0], p2[1], r2
        d = np.sqrt((abs(a-x))**2 + (abs(b-y))**2) # distance between two circles
        
        if d > (R+S) or d < (abs(R-S)):
            print("Two circles have no intersection")
            return 
        elif d == 0 and R==S :
            print("Two circles have same center!")
            return
        else:
            A = (R**2 - S**2 + d**2) / (2 * d)
            h = np.sqrt(R**2 - A**2)
            x2 = x + A * (a-x)/d
            y2 = y + A * (b-y)/d

            x3 = round(x2 - h * (b - y) / d,2)
            y3 = round(y2 + h * (a - x) / d,2)
            x4 = round(x2 + h * (b - y) / d,2)
            y4 = round(y2 - h * (a - x) / d,2)

            c1=np.array([x3, y3])
            c2=np.array([x4, y4])

        return c1,c2

    ''' *old way, MAYBE WRONG*
    ## set x = ay + b
    #  set uy^2 + vy + w = 0
    a = -(H1_e22y-M_e22y)/(H1_e1x-M_e1x)
    b = (H1C_distance**2-CM_distance**2-(H1_e1x**2-M_e1x**2)-(H1_e22y**2-M_e22y**2))/\
            (-2*(H1_e1x-M_e1x))
    u = a**2+1
    v = 2*a*b-2*a*H1_e1x-2*H1_e22y
    w = b**2-2*b*H1_e1x+H1_e1x**2+H1_e22y**2-OH_distance**2
    #print(v**2-4*u*w)
    C_e22y = (-v+np.sqrt(v**2-4*u*w))/(2*u) # choose the bigger one why?
    C_e1x = a*C_e22y + b
    '''

    C1, C2 = insec([H1_e1x,H1_e22y], H1C_distance, [M_e1x,M_e22y], CM_distance)
    if C1[1] < C2[1]:
        C1, C2 = C2, C1 # choose bigger one
    C_e1x, C_e22y = C1[0], C1[1]
    C_XYZ = (abc.T*abO).T.sum(0) + C_e1x*e1 + C_e22y*e22
    
    ## get H2, H3, H4
    H34_degree = 15
    H_proj = np.cos(H34_degree/180*np.pi)*e1 - np.sin(H34_degree/180*np.pi)*e22
    H_proj = H_proj/np.linalg.norm(H_proj) # set 15 degree bt e1
    H3_XYZ = 1.0*np.tan(109.5/2/180*np.pi)*e3 + H_proj
    H3_XYZ = C_XYZ + H3_XYZ/np.linalg.norm(H3_XYZ)*1.096
    H4_XYZ = - 1.0*np.tan(109.5/2/180*np.pi)*e3 + H_proj
    H4_XYZ = C_XYZ + H4_XYZ/np.linalg.norm(H4_XYZ)*1.096 
    ##
    H2_XYZ = 1.096*np.cos(((360-109.5)/2-H34_degree)/180*np.pi)*e1 + 1.096*np.sin(95.25/180*np.pi)*e22
    H2_XYZ = C_XYZ + H2_XYZ/np.linalg.norm(H2_XYZ)*1.096

    # turn absolute coor into frac coor.
    H1_xyz = (np.dot(np.linalg.inv(abc.T), H1_XYZ)).T
    H2_xyz = (np.dot(np.linalg.inv(abc.T), H2_XYZ)).T # fine
    H3_xyz = (np.dot(np.linalg.inv(abc.T), H3_XYZ)).T # fine
    H4_xyz = (np.dot(np.linalg.inv(abc.T), H4_XYZ)).T # fine
    C_xyz = (np.dot(np.linalg.inv(abc.T), C_XYZ)).T

    # calc computed distance between H1 and C
    v_H1C_calc = H1_XYZ - C_XYZ
    d_H1C_calc = np.linalg.norm(v_H1C_calc)

    return H1_xyz, H2_xyz, H3_xyz, H4_xyz, C_xyz, d_H1C_calc

def create_POSCAR_fort(dir, suf_dir, ts_dir, tstype):
    ''
    CONTCAR = os.path.join(suf_dir, 'CONTCAR')
    H1_xyz, H2_xyz, H3_xyz, H4_xyz, C_xyz, d_H1C = cal_CH4_xyz(CONTCAR, tstype)

    ''
    content = []
    shutil.copyfile(os.path.join(suf_dir, 'CONTCAR'), os.path.join(ts_dir, 'POSCAR'))
    with open(os.path.join(ts_dir, 'POSCAR'), 'r') as f:
        content = f.readlines()
    new_content = ''
    for i in range(5):
        new_content += content[i]
    new_content += '{:>5}{:>5}'.format('H', 'C') + str(content[5])
    new_content += '{:>5}{:>5}'.format('4', '1') + str(content[6])
    for line in content[7:9]:
        new_content += line
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(H1_xyz[0], H1_xyz[1], H1_xyz[2])
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(H2_xyz[0], H2_xyz[1], H2_xyz[2])
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(H3_xyz[0], H3_xyz[1], H3_xyz[2])
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(H4_xyz[0], H4_xyz[1], H4_xyz[2])
    new_content += '  {:<14}  {:<14}  {:<14}   T   T   T\n'.format(C_xyz[0], C_xyz[1], C_xyz[2])
    for line in content[9:58]:
        new_content += line
    with open(os.path.join(ts_dir, 'POSCAR'), 'w') as f:
        f.write(new_content)

    'Create fort.188'
    with open(os.path.join(ts_dir, 'fort.188'), 'w') as f:
        f.write('1\n3\n6\n4\n0.04\n1   5     %f\n0' %d_H1C) # 1.5 H1C_distance

def prepare_ts(finished_dirs, tstype):
    for root_dir in finished_dirs:
        ''
        suf_dir = os.path.join(root_dir, 'suf')
        ts_dir = os.path.join(root_dir, tstype)

        ''
        if os.path.exists(ts_dir):
            if not os.path.exists(os.path.join(ts_dir, 'print-out')):
                print('Recreate! ', ts_dir)
                shutil.rmtree(ts_dir)
                os.mkdir(ts_dir)
                CreateCars.create_VASPsp(root_dir, suf_dir, ts_dir)
                CreateCars.create_INCAR(root_dir, suf_dir, ts_dir, 1)
                shutil.copyfile(os.path.join(suf_dir, 'KPOINTS'), os.path.join(ts_dir, 'KPOINTS'))
                create_POSCAR_fort(root_dir, suf_dir, ts_dir, tstype)
                CreateCars.create_POTCAR(ts_dir)
        else:
            print('New! ', ts_dir)
            os.mkdir(ts_dir)
            CreateCars.create_VASPsp(root_dir, suf_dir, ts_dir)
            CreateCars.create_INCAR(root_dir, suf_dir, ts_dir, 1)
            shutil.copyfile(os.path.join(suf_dir, 'KPOINTS'), os.path.join(ts_dir, 'KPOINTS'))
            create_POSCAR_fort(dir, suf_dir, ts_dir, tstype)
            CreateCars.create_POTCAR(ts_dir)

def main():
    if len(sys.argv) == 1:
        work_dir = r'./TestDir/'
        if os.path.exists(work_dir):
            finished_dirs = CheckOut.check_printout(work_dir, 'suf')
            print('Finished Dirs: ', finished_dirs)
            prepare_ts(finished_dirs)       
        else:
            print('Test Only.')
            print('suf2ts.py [Dir] [TStype] [Metal]')
    elif len(sys.argv) == 4:
        'Get argvs'
        work_dir = sys.argv[1]
        tstype = sys.argv[2]
        element = sys.argv[3]

        ''
        finished_dirs = []
        converged_dirs = CheckOut.check_printout(work_dir, 'suf')
        for vasp_dir in converged_dirs:
            if re.match(r'.*' + element + r'O2_.*', os.path.basename(vasp_dir)) or \
                    re.match(r'pure' + element + r'O2', os.path.basename(vasp_dir)):
                finished_dirs.append(vasp_dir)
        prepare_ts(finished_dirs,tstype)
    else:
        print('suf2ts.py [Dir] [Metal]')
        sys.exit()
 
if __name__ == '__main__':
    main()
