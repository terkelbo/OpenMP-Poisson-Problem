import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

df1 = pd.read_csv('statfun.dat',delim_whitespace=True,header=None,names=["Threads","MaxIter","Memory","MFlops","WallTime","Size"])

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


plt.figure()
df1.reset_index(inplace=True)
#df1.set_index("Threads", inplace=True)
df1 = df1.sort_values(['Size','Threads'],ascending=True)
df_temp = df1.groupby('Size').first().reset_index()[['Threads','Size','WallTime']]
df_temp = df_temp.rename({'WallTime':'WallTimeFirst'},axis=1)
df1 = df1.merge(df_temp,on=['Threads','Size'])
df1['Speedup'] = df1['WallTime']/df1['WallTimeFirst']
ax = df1.groupby("Size")["Speedup"].plot(legend=True, style ='*-')
plt.legend(loc='upper left')
plt.xlabel('Number of threads')
plt.ylabel('Speedup')
#plt.gca().set_ylim(bottom=0)
plt.xscale('log',basex=2)
plt.yscale('log',basey=2)
ax = plt.gca().xaxis
ax.set_major_formatter(ScalarFormatter())
ax = plt.gca().yaxis
ax.set_major_formatter(ScalarFormatter())
plt.savefig('Speedup.png', bbox_inches='tight')
plt.close()

