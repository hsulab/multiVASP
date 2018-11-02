#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: mpitest.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 四 11/ 1 09:59:17 2018
#########################################################################
''
import numpy as np

'MPI'
from mpi4py import MPI

def main():
    'Init MPI'
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()


    'Scatter Data'
    if rank == 0:
        data = [[1,2],[3,4]]
    elif rank == 1:
        data = [[5,6],[7,8]]
    else:
        data = None

    local_data = comm.scatter(data, root=0)
    print("rank = ",rank," data = ", local_data)

    'Processing Data'
    num_sum = 0
    for num in local_data:
        num_sum += num
    print('rank = ', rank, 'SUM = ', num_sum)

    'Gather Data'
    gather_data = comm.gather(num_sum,root=0)

    return gather_data

if __name__ == '__main__':
    print(main())
