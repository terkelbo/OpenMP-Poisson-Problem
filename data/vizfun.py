import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

df1 = pd.read_csv('statfun.dat',delim_whitespace=True,header=None,names=["Threads","MaxIter","Memory","MFlops","te"])

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
