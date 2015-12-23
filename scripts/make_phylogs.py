#!//anaconda/bin/python

#/Users/sebastianducheneAIr/anaconda/bin/python

print 'using new function to process only last 100 trees'

import dendropy as dp
import sys, re, copy

def get_phylogs(trees_in):
    '''
    The trees should be read as a Tree list in dendropy
    ''' 
    trees_out = list()

    for t in trees_in:
        print 'doing tree'
        print t.print_plot()
        t_new = copy.deepcopy(t)
        
        for b in t_new.postorder_edge_iter():
            b.length = b.length * float(b.head_node.annotations['rate'])
        
        trees_out.append(re.sub('\'|[-]', '',t_new.as_string('newick')))
#        trees_out.append(t_new.as_string('newick'))

    return(trees_out)

input_file = sys.argv[1]

out_file = re.sub('[.].+$', '_phylogs.trees', input_file)
print out_file

trees_in_comp = dp.TreeList.get_from_path(input_file, 'nexus', extract_comment_metadata = True)

# Modified code to run only the last 100 trees
#trees_in = trees_in_comp[(len(trees_in_comp) - 100):len(trees_in_comp)]

trees_in = trees_in_comp
trs = get_phylogs(trees_in)


output = open(out_file, 'w')
for t in trs:
    output.write(t)
output.close()


