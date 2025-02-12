import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add edges (nodes are added automatically)
G.add_edges_from([(1, 2), (1, 5), (2, 5), (2, 6), (3, 6), (3, 7), (3, 10),
                  (4,7),(4,11),(5,6),(5,9),(6,9),(7,11),
                  (8,9),(8,12),(9,10),(9,12),(9,13),(10,11),(10,14),
                  (12,16),(13,14),(13,17),(14,17),(15,16),
                  (16,17)])

# Draw the graph
pos = nx.spring_layout(G, k=0.8)  # Higher 'k' spreads the nodes further apart
plt.figure(figsize=(10, 10))
nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='black', node_size=1500, font_size=12)
plt.show()

L = nx.laplacian_matrix(G).toarray()

# Calculate the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(L)

sorted_indices = np.argsort(eigenvalues)  # Get the sorted indices based on eigenvalues
eigenvalues_sorted = eigenvalues[sorted_indices]  # Sort eigenvalues
eigenvectors_sorted = eigenvectors[:, sorted_indices] 

# Print the eigenvalues
print("Eigenvalues:")

for i,eigenvalue in enumerate(eigenvalues_sorted):
    print("lambda"+str(i+1)+"="+str(round(eigenvalue,2))+" -> "+str([float(round(row[i],2)) for row in eigenvectors_sorted])+"\n")