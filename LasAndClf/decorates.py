#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: decorates.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 四  9/27 23:05:55 2018
#########################################################################
import time
###
'Count Time'
def timer(func):
     def inner(*args, **kwargs): #1
         start = time.time()
         ret = func(*args, **kwargs)
         end = time.time()
         print(end-start)
         return ret #2
     return inner
###
'lasso wrapper'
def printer(file_name, outs):
    def logger(func):
        def writer(*args, **kwargs): 
            'Run Func'
            start = time.time()
            ret = func(*args, **kwargs)
            end = time.time()
            'Get Content'
            model_params = ret[0]
            fea_coef = ret[1]
            with open(file_name, 'w+') as f:
                f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n')
                f.write('{:<10}{:<10}'.format('Cpu Time:', round(end-start,8))+'\n')
                f.write('Model Parameters: \n')
                'Write Model Params'
                count = 1
                for param, value in model_params.items():
                    content = '{:<15}{:^5}{:<15}'.format(str(param),'-->',str(value))
                    f.write(content)
                    if count % 2 == 0:
                        f.write('\n')
                    else:
                        f.write(' '*10)
                    count += 1
                f.write('\nFeatures and Coefficients: \n')
                'Write Feas and Coefs'
                count = 1
                fea_counts={'suf':0, 'CH3ab':0, 'Hab2':0, 'Hab3':0}
                geo_counts={'E':0, 'd':0, 'a':0, 'h':0}
                fc_sorted = {}
                fc = sorted(fea_coef.items(), key=lambda d: abs(d[1]), reverse=True)
                for t in fc:
                    fc_sorted[t[0]] = t[1]
                'Write Feas'
                for fea, coef in fc_sorted.items():
                    if abs(coef) > 0:
                        fea_belong = fea.split('_')[-1]
                        geo_belong = fea.split('_')[0]
                        fea_counts[fea_belong] = fea_counts[fea_belong] + 1
                        geo_counts[geo_belong] = geo_counts[geo_belong] + 1
                        content = '{:<25}{:^5}{:<20}'.format(str(fea),'-->',str(round(coef, 8)))
                        f.write(content)
                        if count % 2 == 0:
                            f.write('\n')
                        else:
                            f.write(''*10)
                        count += 1
                f.write('\n'+str(fea_counts))
                f.write('\n'+str(geo_counts))
            ###
            if outs == 'out':
                print(file_name)
                with open(file_name, 'r') as f:
                    content = f.readlines()
                    for i in range(len(content)):
                        print(content[i], end='')
            return ret
        return writer
    return logger
###
def main():
    print()
###
if __name__ == '__main__':
    main()
