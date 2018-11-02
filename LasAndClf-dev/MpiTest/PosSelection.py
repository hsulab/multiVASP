#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: PosSelection.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
'SciLibs'
import math
import numpy as np
import pandas as pd

'sklearn'
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso,LassoLars,LassoCV,LassoLarsCV
from sklearn.model_selection import KFold

'Data Operation'
import pickle
from DataOperators import GetDS
from DataOperators import pkload
from DataOperators import pkdump

def PosSelection(feanames, coefs):
    'Get Positive Coef'
    name_coef = {}
    for name, coef in zip(feanames, coefs):
        if abs(coef) > 0:
            name_coef[name] = coef

    # sort fea by abs value
    nc_sorted = sorted(name_coef.items(), key=lambda d:abs(d[1]), reverse=True)
    nc_dict = {}
    for t in nc_sorted:
        nc_dict[t[0]] =t[1]

    return nc_dict


if __name__ == '__main__':
    print('Test.')
