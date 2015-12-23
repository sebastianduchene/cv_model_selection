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
phylogs_file = sys.argv[2]

p4.read(test_set_file)
a = p4.var.alignments[0]

p4.read(phylogs_file)

for i in range(len(p4.var.trees)):
    print i
    t = p4.var.trees[i]
    t.data = p4.Data(a)
    t.newComp(free = 1, spec = 'equal')
    t.newRMatrix(free = 0, spec = 'ones')
    t.setNGammaCat(partNum = 0, nGammaCat=1)
#    t.newGdasrv(partNum=0,free = 1, val = gamma.ix[i])
    t.setPInvar(free = 0, val = 0.0)
    t.calcLogLike()
    t.model = None
