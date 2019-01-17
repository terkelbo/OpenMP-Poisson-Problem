import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

font = {'size'   : 14}

mpl.rc('font', **font)

df1 = pd.read_csv('statfun.dat',delim_whitespace=True,header=None,names=["Threads","MaxIter","Memory","MFlops","WallTime","Size"])

df1 = df1.loc[df1['Threads'] < 16]

plt.figure()
df1.set_index("Memory", inplace=True)
ax = df1.groupby("Threads")["MFlops"].plot(legend=True, style ='*-')
plt.legend(loc='upper left')
plt.xlabel('Memory Footprint (Kbyte)')
plt.ylabel('Performance (MFlops)')
plt.gca().set_ylim(bottom=0)
plt.xscale('log',basex=4)
#plt.yscale('log',basey=2)
ax = plt.gca().xaxis 
ax.set_major_formatter(ScalarFormatter()) 
#ax = plt.gca().yaxis 
#ax.set_major_formatter(ScalarFormatter()) 
plt.savefig('MFlops.png', bbox_inches='tight')
plt.close()

plt.figure()
ax = df1.groupby("Threads")["WallTime"].plot(legend=True, style ='*-')
plt.legend(loc='upper left')
plt.xlabel('Memory Footprint (Kbyte)')
plt.ylabel('Elapsed Wall Clock Time (s)')
plt.gca().set_ylim(bottom=0)
plt.xscale('log',basex=4)
#plt.yscale('log',basey=2)
ax = plt.gca().xaxis
ax.set_major_formatter(ScalarFormatter())
#ax = plt.gca().yaxis
#ax.set_major_formatter(ScalarFormatter())
plt.savefig('WallTime.png', bbox_inches='tight')
plt.close()

df1 = pd.read_csv('statfun.dat',delim_whitespace=True,header=None,names=["Threads","MaxIter","Memory","MFlops","WallTime","Size"])
df1 = df1.loc[df1['Size'] >= 100]
plt.figure()
df1.set_index("Threads", inplace=True)
ax = df1.groupby("Size")["WallTime"].plot(legend=True, style ='*-')
plt.legend(loc='upper left')
plt.xlabel('Number of Threads')
plt.ylabel('Elapsed Wall Clock Time (s)')
#plt.gca().set_ylim(bottom=0)
plt.xscale('log',basex=2)
plt.yscale('log',basey=2)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax = plt.gca().xaxis 
ax.set_major_formatter(ScalarFormatter()) 
ax = plt.gca().yaxis 
#ax.set_major_formatter(ScalarFormatter()) 
plt.savefig('ThreadsWallTime.png', bbox_inches='tight')
plt.close()

df1 = pd.read_csv('statfun.dat',delim_whitespace=True,header=None,names=["Threads","MaxIter","Memory","MFlops","WallTime","Size"])
df1 = df1.loc[df1['Size'] >= 100]
plt.figure()
df1 = df1.sort_values(['Size','Threads'],ascending=True)
df_temp = df1.groupby('Size').first().reset_index()[['Size','WallTime']]
df_temp = df_temp.rename({'WallTime':'WallTimeFirst'},axis=1)
df1 = df1.merge(df_temp,on=['Size'])
df1['Speedup'] = df1['WallTimeFirst']/df1['WallTime']
df1.set_index("Threads", inplace=True)
ax = df1.groupby("Size")["Speedup"].plot(legend=True, style ='*-')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel('Number of threads')
plt.ylabel('Speedup')
plt.xscale('log',basex=2)
#plt.yscale('log',basey=2)
ax = plt.gca().xaxis
ax.set_major_formatter(ScalarFormatter())
#ax = plt.gca().yaxis
#ax.set_major_formatter(ScalarFormatter())
plt.savefig('Speedup.png', bbox_inches='tight')
plt.close()

