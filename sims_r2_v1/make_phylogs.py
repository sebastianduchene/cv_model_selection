#!//anaconda/bin/python

#/Users/sebastianducheneAIr/anaconda/bin/python


import dendropy as dp
import sys, re

def get_phylogs(trees_in):
    '''
    The trees should be read as a Tree list in dendropy
    ''' 
    trees_out = list()

    for i in range(len(trees_in)):
        tr = dp.Tree.get_from_string(trees_in[i].as_string('nexus'), 'nexus')

        for b in tr.postorder_edge_iter():
            b.length = b.length * float(b.head_node.annotations['rate'])

        trees_out.append(tr.as_string('newick'))

    return(trees_out)

input_file = sys.argv[1]

trees_in = dp.TreeList.get_from_path(input_file, 'nexus', extract_comment_metadata = True)

trs = get_phylogs(trees_in)

out_file = re.sub('[.].+$', '_phylogs.trees', input_file)

output = open(out_file, 'w')
for t in trs:
    output.write(t)
output.close()


