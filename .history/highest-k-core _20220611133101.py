#the goal is to find the highest k-core subgraph in a given protein-protein interaction
# network. The interaction network is given as a set of undirected edges that comprise a graph. There are
# no self-edges in the input interaction networks on which your program will be tested.  A k-core in a
# graph is a subgraph in which all the nodes in that induced subgraph have at least degree k. In other
# words each node in a k-core has at least k immediate neighbors. Given an input network, use the O(n3)
# algorithm described in class to find the number of proteins for each value of k such that k is the highest
# k-core they belong to. Report your results for the following test network