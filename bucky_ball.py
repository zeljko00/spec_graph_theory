import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = [
[ 0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0 ],
[ 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1 ],
[ 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0 ],
[ 0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0 ],
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0 ],
[ 0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0 ],
[ 0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0 ],
[ 0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0 ],
[ 0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0 ],
[ 0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1 ],
[ 0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0 ]
]

D = np.diag([3] * 60)
L = D - A

eigenvalues, eigenvectors = np.linalg.eig(L)

sorted_indices = np.argsort(eigenvalues)
eigenvalues_sorted = eigenvalues[sorted_indices]
eigenvectors_sorted = eigenvectors[:, sorted_indices] 

for i,eigenvalue in enumerate(eigenvalues_sorted[0:10]):
    print("lambda"+str(i+1)+"="+str(round(eigenvalue,2))+" -> "+str([float(round(row[i],2)) for row in eigenvectors_sorted])+"\n")


adj_list = {
    1: [2, 3, 4],
    2: [1, 55, 56],
    3: [1, 58, 60],
    4: [1, 57, 59],
    5: [8, 13, 14],
    6: [8, 12, 15],
    7: [8, 11, 16],
    8: [5, 6, 7],
    9: [13, 15, 25],
    10: [14, 16, 26],
    11: [7, 12, 24],
    12: [6, 11, 23],
    13: [5, 9, 18],
    14: [5, 10, 17],
    15: [6, 9, 19],
    16: [7, 10, 20],
    17: [14, 18, 30],
    18: [13, 17, 29],
    19: [15, 28, 32],
    20: [16, 27, 31],
    21: [26, 30, 46],
    22: [25, 29, 45],
    23: [12, 28, 38],
    24: [11, 27, 37],
    25: [9, 22, 32],
    26: [10, 21, 31],
    27: [20, 24, 35],
    28: [19, 23, 36],
    29: [18, 22, 43],
    30: [17, 21, 44],
    31: [20, 26, 42],
    32: [19, 25, 41],
    33: [35, 42, 53],
    34: [36, 41, 54],
    35: [27, 33, 40],
    36: [28, 34, 39],
    37: [24, 38, 40],
    38: [23, 37, 39],
    39: [36, 38, 52],
    40: [35, 37, 51],
    41: [32, 34, 50],
    42: [31, 33, 49],
    43: [29, 44, 48],
    44: [30, 43, 47],
    45: [22, 48, 50],
    46: [21, 47, 49],
    47: [44, 46, 60],
    48: [43, 45, 59],
    49: [42, 46, 58],
    50: [41, 45, 57],
    51: [40, 52, 56],
    52: [39, 51, 55],
    53: [33, 56, 58],
    54: [34, 55, 57],
    55: [2, 52, 54],
    56: [2, 51, 53],
    57: [4, 50, 54],
    58: [3, 49, 53],
    59: [4, 48, 60],
    60: [3, 47, 59]
}

edges = set()
for node, neighbors in adj_list.items():
    for neighbor in neighbors:
        edges.add((node - 1, neighbor - 1))  # Convert to 0-based index

e2_1 = [-0.01, -0.02, -0.07, 0.07, 0.02, 0.07, -0.07, 0.01, 0.16, -0.13, -0.05, 0.03, 0.09, -0.04, 0.15, -0.14, -0.01, 0.07, 0.19, -0.19, -0.14, 0.18, 0.07, -0.11, 0.2, -0.17, -0.18, 0.14, 0.12, -0.06, -0.21, 0.22, -0.2, 0.17, -0.18, 0.14, -0.08, 0.02, 0.06, -0.12, 0.21, -0.22, 0.08, -0.02, 0.18, -0.14, -0.07, 0.11, -0.19, 0.19, -0.07, 0.01, -0.16, 0.13, 0.04, -0.09, 0.14, -0.15, 0.05, -0.03]
e2_2 = [-0.01, -0.1, 0.03, 0.04, 0.1, -0.03, -0.04, 0.01, 0.09, 0.07, -0.12, -0.11, 0.14, 0.13, 0.01, -0.01, 0.19, 0.2, -0.03, -0.06, 0.14, 0.17, -0.16, -0.17, 0.11, 0.08, -0.14, -0.12, 0.21, 0.2, -0.0, 0.03, -0.11, -0.08, -0.17, -0.14, -0.21, -0.21, -0.2, -0.21, 0.0, -0.03, 0.21, 0.21, 0.14, 0.12, 0.16, 0.17, 0.03, 0.06, -0.2, -0.19, -0.09, -0.07, -0.13, -0.14, 0.01, -0.01, 0.12, 0.11]
e2_3 = [0.22, 0.2, 0.21, 0.21, -0.2, -0.21, -0.21, -0.22, -0.15, -0.15, -0.18, -0.18, -0.17, -0.17, -0.17, -0.17, -0.11, -0.11, -0.1, -0.1, -0.01, -0.01, -0.11, -0.11, -0.07, -0.07, -0.07, -0.07, -0.03, -0.03, -0.05, -0.05, 0.07, 0.07, 0.01, 0.01, -0.05, -0.05, 0.03, 0.03, 0.05, 0.05, 0.05, 0.05, 0.07, 0.07, 0.11, 0.11, 0.1, 0.1, 0.11, 0.11, 0.15, 0.15, 0.17, 0.17, 0.17, 0.17, 0.18, 0.18]

plt.figure(figsize=(8, 8))
for i, j in edges:
    x_vals = [e2_1[i], e2_1[j]]
    y_vals = [e2_2[i], e2_2[j]]
    plt.plot(x_vals, y_vals, color='blue', markersize=3)
plt.scatter(e2_1, e2_2, c='r', marker='o', s=50, zorder=50)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xlabel("e2_1")
plt.ylabel("e2_2")
plt.title("Spectral graph drawing")
plt.show()

plt.figure(figsize=(8, 8))
for i, j in edges:
    x_vals = [e2_1[i], e2_1[j]]
    y_vals = [e2_3[i], e2_3[j]]
    plt.plot(x_vals, y_vals, color='blue', markersize=3)
plt.scatter(e2_1, e2_3, c='r', marker='o', s=50, zorder=50)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xlabel("e2_1")
plt.ylabel("e2_2")
plt.title("Spectral graph drawing")
plt.show()

plt.figure(figsize=(8, 8))
for i, j in edges:
    x_vals = [e2_2[i], e2_2[j]]
    y_vals = [e2_3[i], e2_3[j]]
    plt.plot(x_vals, y_vals, color='blue', markersize=3)
plt.scatter(e2_2, e2_3, c='r', marker='o', s=50, zorder=50)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xlabel("e2_1")
plt.ylabel("e2_2")
plt.title("Spectral graph drawing")
plt.show()

# 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(e2_1, e2_2, e2_3, c='r', marker='o', s=50, zorder=50)
ax.set_xlabel('e2_1')
ax.set_ylabel('e2_2')
ax.set_zlabel('e2_3')

for i, j in edges:
    x_vals = [e2_1[i], e2_1[j]]
    y_vals = [e2_2[i], e2_2[j]]
    z_vals = [e2_3[i], e2_3[j]]
    ax.plot(x_vals, y_vals, z_vals, color='blue', markersize=3)

plt.title("Bucky ball")
plt.show()

# # Plot the points and connect them
# plt.figure(figsize=(6, 6))
# plt.plot(alpha2_x, alpha3_y, marker='o', color='blue', linestyle='-', markersize=8, label="čvorovi")  # Connect the dots with lines
# plt.scatter(alpha2_x, alpha3_y, color='red', s=100, zorder=5)  # Emphasize the dots with red color and bigger size
# plt.axhline(0, color='black', linewidth=0.5)
# plt.axvline(0, color='black', linewidth=0.5)
# plt.grid(True, linestyle='--', linewidth=0.5)
# plt.xlabel("e2")
# plt.ylabel("e3")
# plt.title("Spectral graph drawing")
# plt.legend()
# plt.show()


# Create the plot

# Plot the edges
# for edge in G.edges():
#     x_vals = [pos[edge[0]][0], pos[edge[1]][0]]
#     y_vals = [pos[edge[0]][1], pos[edge[1]][1]]
#     z_vals = [pos[edge[0]][2], pos[edge[1]][2]]
#     ax.plot(x_vals, y_vals, z_vals, color='b', alpha=0.7)

# Plot the nodes
# node_x = [pos[node][0] for node in G.nodes()]
# node_y = [pos[node][1] for node in G.nodes()]
# node_z = [pos[node][2] for node in G.nodes()]


# # Add labels for the nodes
# for node in G.nodes():
#     ax.text(pos[node][0], pos[node][1], pos[node][2], str(node), color='black')

# Set labels


