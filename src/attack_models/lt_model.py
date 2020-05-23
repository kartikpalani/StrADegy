import numpy as np
class LinearThresholdModel:

	"""
	input: G: networkx graph , s:source node
	output: list of nodes activated  

	This is one round of the LT process done until no more nodes are reachable
	each node in G has an attribute "threshold" which is chosen uniformly in [0,1]
	each edge in G has an attribute "influence" which is a weight such that sum of weights of all incoming edges to a node is <=1.
	So by,default, "influence" of an edge is (1/in_degree) of node it is headed to.

	"""
	def __init__(self, graph, source):
		self.name = 'LinearThresholdModel'
		self.graph = self.construct_graph(graph)
		self.source = source
	
	def construct_graph(self,graph):
		for node in graph.nodes:
			graph.node[node]['threshold'] = np.random.uniform(0,1)

		return graph

	def diffuse(self):
		G = self.graph
		s = self.source
		potential_activations = set(list(G.successors(s)))
		activated = [s]

		while potential_activations:
			successors = []
			for node in potential_activations:
				activated_predecessors = list(set(list(G.predecessors(node))).intersection(set(activated)))
			 	neighbor_pressure = 0
				for neighbor in activated_predecessors:
					neighbor_pressure += G[neighbor][node]['influence']

			  	print "The threshold for choosing node %d is:  %f" %(node,G.node[neighbor]['threshold'])
			  	if neighbor_pressure >= G.node[neighbor]['threshold']:
			  		activated.append(node)

				successors.extend(list(G.successors(node)))
			potential_activations = set(successors) - set(activated)

			print "Activated till now: " + str(activated)
			print "Next set of potential activations: " + str(potential_activations)
		return activated
