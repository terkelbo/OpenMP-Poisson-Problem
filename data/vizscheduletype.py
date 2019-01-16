# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:29:01 2019

@author: terke
"""

import pandas as pd
import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

font = {'size'   : 14}

mpl.rc('font', **font)

df1 = pd.read_csv('scheduletype.dat',delim_whitespace=True,header=None,names=["Threads","ScheduleType","MaxIter","Memory","MFlops","te"])

plt.figure()
df1.set_index("Memory", inplace=True)
ax = df1.groupby("ScheduleType")["MFlops"].plot(legend=True, style ='*-')
plt.legend(loc='upper left')
plt.xlabel('Memory (Kbytes)')
plt.ylabel('MFlops')
plt.gca().set_ylim(bottom=0)
plt.xscale('log',basex=4)
#plt.yscale('log',basey=2)
ax = plt.gca().xaxis 
ax.set_major_formatter(ScalarFormatter()) 
#ax = plt.gca().yaxis 
#ax.set_major_formatter(ScalarFormatter()) 
plt.savefig('ScheduletypeExperiment.png', bbox_inches='tight')
plt.close()
