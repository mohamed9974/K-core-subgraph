'''the goal is to find the highest k-core subgraph in a given protein-protein interaction
# network. The interaction network is given as a set of undirected edges that comprise a graph. There are
#  no self-edges in the input interaction networks on which your program will be tested.  A k-core in a
# graph is a subgraph in which all the nodes in that induced subgraph have at least degree k. In other
# # words each node in a k-core has at least k immediate neighbors. Given an input network, use the O(n3)
# # algorithm described in class to find the number of proteins for each value of k such that k is the highest
# # k-core they belong to. Report your results for the following test network
# # Your program should output the number of proteins at each k-core starting with k = 1 and going until the
# # number of proteins for larger values of k becomes 0 (zero).

#input: The network data is given as a list of undirected edges. Each line of the file represents an undirected
# edge that connects a pair of tab separated gene ids. There are no self-edges
#Example input:
# A1BG	GRB2
# A1BG	PIK3CA
# A1BG	PIK3R1
# A1BG	PTPN11
# A1BG	SOS1
# A1CF	APOBEC1
# A1CF	APOBEC2
# A1CF	APOBEC3A
# A1CF	APOBEC3B
# A1CF	APOBEC3C
# A1CF	APOBEC3H
# A1CF	APOBEC4
# A2M	KLKB1
# A2M	MMP10
# A2M	MMP11
# A2M	MMP12
# A2M	MMP13
# A2M	MMP19
# A2M	MMP1
# A2M	MMP20
# A2M	MMP2
# A2M	MMP3
# A2M	MMP7
# A2M	MMP8
#output: a file containing the number of proteins at each k-core starting with k = 1 and going until the number of proteins for larger values of k becomes 0 (zero)
#Example output:
# For k = 1 there are 1222 proteins.
# For k = 2 there are 442 proteins.
# For k = 3 there are 217 proteins.
# For k = 4 there are 85 proteins.

# Hint: If you use the Hashtable/Map/Dictionary based adjacency list representation for the PPI network we
# discussed in class, your program should report the result and finish in a few seconds.
# You can use the file ReadNetwork.java as an example.'''

function = lambda x: x.split('\t')
