import numpy as np
class IndependentCascadeModel:

	"""
	input: G: networkx graph , s:source node
	output: list of nodes activated  

	This is one round of the LT process done until no more nodes are reachable
	each node in G has an attribute "threshold" which is chosen uniformly in [0,1]
	each edge in G has an attribute "influence" which is a weight such that sum of weights of all incoming edges to a node is <=1.
	So by,default, "influence" of an edge is (1/in_degree) of node it is headed to.

	"""
	def __init__(self, graph, source):
		self.name = 'IndependentCascadeModel'
		self.graph = graph
		self.source = source

	def diffuse(self):
		new_active, activated = [self.source], [self.source]

		#keep running till no new nodes are activated
		while new_active:
			for node in new_active:
				#np.random.seed(i)
				successors = list(self.graph.successors(node))
				success_criteria = np.random.uniform(0,1,len(successors))
				compromised_this_round = self.compare_lists(success_criteria,node,successors)
				#new_nodes += list(np.extract(comparison_result,successors))
	 			#print "The node {} has the neighbors {} of which {} were compromised because the success_criteria was {}".format(node,successors,compromised_this_round,success_criteria)

	 		new_active = list(set(compromised_this_round) - set(activated))
	 		activated += new_active

	 	return activated

	def compare_lists(self,success_criteria,node,successors):
		compromised = []
		
		for successor in successors:
			if self.graph[node][successor]['influence'] > success_criteria[successors.index(successor)]:
				#print "Edge {} has influence {}".format((node,successor),self.graph[node][successor]['influence'])
				compromised.append(successor)

	 	return compromised