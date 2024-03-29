import sys
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

sys.path.append('../')

font = {'size'   : 14}

mpl.rc('font', **font)

files_list = ['statfun_ccnuma-cores-close.dat','statfun_ccnuma-cores-spread.dat','statfun_ccnuma-cores-true.dat','statfun_ccnuma-sockets-close.dat','statfun_ccnuma-sockets-spread.dat',
				'statfun_ccnuma-sockets-true.dat']
names_list = [name.split('.')[0] for name in files_list]
files_list = ['../'+file for file in files_list]

for files, names in zip(files_list, names_list):
	df1 = pd.read_csv(files,delim_whitespace=True,header=None,names=["Threads","MaxIter","Memory","MFlops","WallTime","Size"])

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
	plt.savefig('MFlops_%s.png' % names, bbox_inches='tight')
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
	plt.savefig('WallTime_%s.png' % names, bbox_inches='tight')
	plt.close()

	df1 = pd.read_csv(files,delim_whitespace=True,header=None,names=["Threads","MaxIter","Memory","MFlops","WallTime","Size"])
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
	plt.savefig('ThreadsWallTime_%s.png' % names, bbox_inches='tight')
	plt.close()

	df1 = pd.read_csv(files,delim_whitespace=True,header=None,names=["Threads","MaxIter","Memory","MFlops","WallTime","Size"])
	df1 = df1.loc[df1['Size'] >= 100]
	plt.figure()
	df1 = df1.sort_values(['Size','Threads'],ascending=True)
	df_temp = df1.groupby('Size').first().reset_index()[['Size','WallTime']]
	df_temp = df_temp.rename({'WallTime':'WallTimeFirst'},axis=1)
	df1 = df1.merge(df_temp,on=['Size'])
	df1['Speedup'] = df1['WallTimeFirst']/df1['WallTime']
	df1.set_index("Threads", inplace=True)
	ax = df1.groupby("Size")["Speedup"].plot(legend=True, style ='*-')
	plt.plot(np.array([1,2,4,8,16]),np.array([1,2,4,8,16]),'k-',label='Linear Scaling')
	plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
	plt.xlabel('Number of threads')
	plt.ylabel('Speedup')
	plt.xscale('log',basex=2)
	plt.yscale('log',basey=2)
	ax = plt.gca().xaxis
	ax.set_major_formatter(ScalarFormatter())
	ax = plt.gca().yaxis
	ax.set_major_formatter(FormatStrFormatter('%.2f'))
	plt.savefig('Speedup_%s.png' % names, bbox_inches='tight')
	plt.close()

