import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (1, 4), (1,5), (2, 3), (2, 4), (3, 4)])

# Draw the graph
pos = nx.spring_layout(G, k=0.8)  # Higher 'k' spreads the nodes further apart
plt.figure(figsize=(10, 10))
nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='black', node_size=1500, font_size=12)
plt.show()

L = nx.laplacian_matrix(G).toarray()
eigenvalues, eigenvectors = np.linalg.eig(L)

sorted_indices = np.argsort(eigenvalues)
eigenvalues_sorted = eigenvalues[sorted_indices]
eigenvectors_sorted = eigenvectors[:, sorted_indices] 

for i,eigenvalue in enumerate(eigenvalues_sorted[0:10]):
    print("lambda"+str(i+1)+"="+str(round(eigenvalue,2))+" -> "+str([float(round(row[i],2)) for row in eigenvectors_sorted])+"\n")



