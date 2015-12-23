import p4
import sys
import pandas as pd

print '''
The order of the arguments is:
- test set file
- log file
- phylograms file
'''


print sys.argv


test_set_file = sys.argv[1]
log_file = sys.argv[2]
phylogs_file = sys.argv[3]

params_comp = pd.read_csv(log_file, sep= '\t', comment='#')

trees_len = len(open(phylogs_file, 'r').readlines())

print params_comp.shape
print trees_len
params_data = params_comp.ix[(params_comp.shape[0] - trees_len):params_comp.shape[0], ]
params_data.index = [i for i in range(params_data.shape[0])]

gamma = params_data['gammaShape']
freqs = params_data[['rateAC', 'rateAG', 'rateAT', 'rateCG' ,'rateGT']]
ex_rates = params_data[['freqParameter.1','freqParameter.2', 'freqParameter.3', 'freqParameter.4']]

p4.read(test_set_file)
a = p4.var.alignments[0]

p4.read(phylogs_file)
len(p4.var.trees)

for i in range(len(p4.var.trees)):
    print i
    t = p4.var.trees[i]
    t.data = p4.Data(a)
    t.newComp(free = 1, spec = 'empirical', val = list(freqs.ix[i, ]))
    t.newRMatrix(free = 0, spec = 'ones', val = list(ex_rates.ix[i, ]))
    t.setNGammaCat(partNum = 0, nGammaCat=4)
    t.newGdasrv(partNum=0,free = 1, val = gamma.ix[i])
    t.setPInvar(free = 0, val = 0.0)
    t.calcLogLike()
    t.model = None
