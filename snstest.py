#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: snstest.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 二  5/ 8 13:55:56 2018
#########################################################################
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  
import seaborn as sns
sns.set(style="ticks")

# Load the example dataset for Anscombe's quartet
df = sns.load_dataset("anscombe")
print(df)

# Show the results of a linear regression within each dataset
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=None, palette="muted", size=4,
           scatter_kws={"s": 50, "alpha": 1})

