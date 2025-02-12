import numpy as np
import networkx as nx

# Define the Laplacian matrix
# L = np.array(
# [
#     [ 2,  -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  -1],
#     [ -1,  2,  -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  -1,  2,  -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  -1,  2,  -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  -1,  2,  -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  -1,  2,  -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  -1,  2,  -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  -1,  2,  -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0,  -1,  2,  -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0,  0,  -1,  2,  -1,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  -1,  2,  -1,  0,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  -1,  2,  -1,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  -1,  2,  -1,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  -1,  2,  -1,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  -1,  2,  -1,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  -1,  2,  -1,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  -1,  2,  -1,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  -1,  2,  -1,  0],
#     [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  -1,  2,  -1],
#     [ -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  -1,  2],
# ]
# )

G = nx.truncated_icosahedron_graph()

# Compute the Laplacian matrix
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

