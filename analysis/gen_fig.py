#!/usr/bin/env python
import csv, sys
import matplotlib as mpl
import matplotlib.pyplot as plt

BASELINE = 263

if len(sys.argv) < 2:
	print "Usage: gen_fig.py <results filename> [<microbench column>] [<exploit measure column>]"
	sys.exit()
filename = sys.argv[1]
if len(sys.argv) > 2: microbench_column = int(sys.argv[2])
else: microbench_column = -1
if len(sys.argv) > 3: exploit_column = int(sys.argv[3])
else: exploit_column = 2

microbench = list()
exploit = list()

with open(filename, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	for row in csvreader:
		microbench.append(float(row[microbench_column]) * 1e6)
		exploit.append(float(row[exploit_column]))

font = {'size':16}
mpl.rc('font', **font)
plt.scatter(microbench, exploit, marker='.')
xmin = min(microbench)
xmax = max(microbench)
xborder = (xmax-xmin) * 0.05
ymin = min(exploit)
ymax = max(max(exploit), BASELINE)
plt.semilogy()
plt.axis((xmin-xborder, xmax+xborder, ymin/2, ymax*2))
plt.axhline(y=BASELINE, color='r')
plt.title('Post-synchronization NOP Injection\n(Nonatomic Operations Assumed to be Atomic)')
plt.xlabel(r'Microbenchmark ($\mu s$)')
plt.ylabel('Cost to Exploit (loop count)')
plt.savefig(filename[:-3] + 'png', bbox_inches='tight', format='png')
