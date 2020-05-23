import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import networkx as nx

from attack_models.lt_model import LinearThresholdModel

def main():
	G = nx.DiGraph()

	G.add_edge(0,1,influence=1)
	G.add_edge(0,2,influence=1)
	G.add_edge(1,3,influence=0.5)
	G.add_edge(1,4,influence=0.2)
	G.add_edge(2,4,influence=0.6)
	G.add_edge(2,5,influence=0.1)
	G.add_edge(1,5,influence=0.1)
	G.add_edge(2,6,influence=0.3)
	G.add_edge(3,7,influence=0.4)
	G.add_edge(4,7,influence=0.05)
	G.add_edge(5,7,influence=0.1)

	source = 0
	edge_count = G.number_of_edges()
	node_count = G.number_of_nodes()
	simulation_count = 1000
	compromised_count = []

	for _ in range(simulation_count):

	  attack = LinearThresholdModel(G,source)
	  compromised_this_attack = attack.diffuse()
	  compromised_count.append(len(compromised_this_attack))
	  print "The expected reachability in your graph is: " + str(np.mean(compromised_count))

	pd.Series(compromised_count).value_counts().plot('bar')
	plt.show()

if __name__ == "__main__":
    main()
