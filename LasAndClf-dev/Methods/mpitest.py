#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: mpitest.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 四 11/ 1 09:59:17 2018
#########################################################################
# mpi_helloworld.py
from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    print('process %d sends %s' % (rank, data))
    comm.send(data, dest=1, tag=11)
elif rank == 1:
    data = comm.recv(source=0, tag=11)
    print('process %d receives %s' % (rank, data))

