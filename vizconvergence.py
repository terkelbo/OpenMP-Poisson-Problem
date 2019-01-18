import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

df1 = pd.read_csv('convergence.dat',delim_whitespace=True,header=None,names=["Algorithm", "Iterations", "Euclidian Norm"])

plt.figure()
df1.set_index("Iterations", inplace=True)
ax = df1.groupby("Algorithm")["Euclidian Norm"].plot(legend=True)
plt.legend(loc='upper right')
plt.xlabel('Nb. of iterations')
plt.ylabel('Euclidian Norm')
plt.savefig('convergence.png', bbox_inches='tight')
plt.close()

df1 = pd.read_csv('iterationspersecond.dat',delim_whitespace=True,header=None,names=["Algorithm", "Iterations", "Memory", "MFlops", "Wall Time"])
df1['iterationspersecond'] = df1['Iterations'] / df1["Wall Time"]
plt.figure()
df1.set_index("Memory", inplace=True)
ax = df1.groupby("Algorithm")["iterationspersecond"].plot(legend=True)
plt.legend(loc='upper right')
plt.xlabel('Memory (Kbytes)')
plt.ylabel('Iterations per second')
plt.xscale('log',basex=4)
plt.yscale('log',basey=10)
ax = plt.gca().xaxis 
ax.set_major_formatter(ScalarFormatter())
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f')) 
plt.savefig('iterationspersecond.png', bbox_inches='tight')
plt.close()

