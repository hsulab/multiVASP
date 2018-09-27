#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: test_getparas.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 四  9/27 15:44:33 2018
#########################################################################
import unittest
###
import numpy as np
from get_paras import *
class TestGetParas(unittest.TestCase):
    '''Test get_paras.py'''
    '''def calc_distance(abc, XYZ1, XYZ2):
            XYZ must be absolute coordinates [X, Y, Z]
            #   1----2
            ###
            XYZ1 = (abc.T*XYZ1).T.sum(0)
            XYZ2 = (abc.T*XYZ2).T.sum(0)
            return round(np.linalg.norm(XYZ1-XYZ2), 8)'''
    def test_cal_distance(self):
        """Test calculate distance"""
        abc = np.array([[1,0,0],[0,1,0],[0,0,1]])
        XYZ1 = np.array([1,0,0])
        XYZ2 = np.array([1,0,0])
        XYZ3 = np.array([2,0,0])
        self.assertEqual(0, calc_distance(abc, XYZ1, XYZ2))
        self.assertNotEqual(0, calc_distance(abc, XYZ1, XYZ3))
if __name__ == '__main__':
    unittest.main()
