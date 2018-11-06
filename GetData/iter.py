#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: iter.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六 11/ 3 12:32:35 2018
#########################################################################
import itertools

def main():
    ijs = list(itertools.combinations(list(range(4)), 2))
    kls = []
    for ij in ijs:
        ij = list(ij)
        print('ij', ij)
        kl = list(range(4))
        print('kl', kl)
        print('ij0', ij[0])
        kl.remove(ij[0])
        kl.remove(ij[1])
        #kls.append(kl)


if __name__ == '__main__':
    main()
