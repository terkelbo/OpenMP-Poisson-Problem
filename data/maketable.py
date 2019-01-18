# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:37:56 2019

@author: terkelbo-pc
"""

import pandas as pd

datafile_1 = 'statfun_poisson_naive.dat'
datafile_2 = 'statfun_poisson_openmp1.dat'
datafile_3 = 'statfun_ccnuma-sockets-spread.dat'

df1 = pd.read_csv(datafile_1,header=None,delim_whitespace=True,names=['Threads','Iterations','Memory','MFlops','Wall Time','Size'])
df2 = pd.read_csv(datafile_2,header=None,delim_whitespace=True,names=['Threads','Iterations','Memory','MFlops','Wall Time','Size'])
df3 = pd.read_csv(datafile_3,header=None,delim_whitespace=True,names=['Threads','Iterations','Memory','MFlops','Wall Time','Size'])

df1 = df1[['Threads','Memory','Wall Time']]
df2 = df2[['Threads','Memory','Wall Time']]
df3 = df3[['Threads','Memory','Wall Time']]

df1 = df1.pivot(index='Memory',columns='Threads',values='Wall Time').rename({1:'1_naive',
                                                                             2:'2_naive',
                                                                             4:'4_naive',
                                                                             8:'8_naive',
                                                                             16:'16_naive'},axis=1)

df2 = df2.pivot(index='Memory',columns='Threads',values='Wall Time').rename({1:'1_openmp1',
                                                                             2:'2_openmp1',
                                                                             4:'4_openmp1',
                                                                             8:'8_openmp1',
                                                                             16:'16_openmp1'},axis=1)

df3 = df3.pivot(index='Memory',columns='Threads',values='Wall Time').rename({1:'1_ccnuma',
                                                                             2:'2_ccnuma',
                                                                             4:'4_ccnuma',
                                                                             8:'8_ccnuma',
                                                                             16:'16_ccnuma'},axis=1)
combined = df1.merge(df2.merge(df3,on='Memory'),on='Memory')

header = pd.MultiIndex.from_product([[' 1',' 2',' 4',' 8','16'],
                                     ['1st','2nd', '3rd']],
                                    names=['Threads','Implementation number'])

double_header_df = pd.DataFrame(combined[['1_naive', '1_openmp1','1_ccnuma','2_naive','2_openmp1','2_ccnuma',
                                          '4_naive','4_openmp1','4_ccnuma','8_naive', '8_openmp1','8_ccnuma',
                                          '16_naive','16_openmp1','16_ccnuma']].values,
                                columns=header,
                                index=combined.index)
double_header_df = double_header_df.reset_index()

with open('table_runtimes.tex','w') as f:
    f.write(double_header_df.to_latex(index=False,float_format=lambda x: '%.3f' % x))
