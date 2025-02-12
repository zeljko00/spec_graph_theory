import matplotlib.pyplot as plt

# Data for the graph
x = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
e1 = [-0.5, -0.5, -0.5, -0.5, 0, 0, 0, 0, 0, 0]
e2 = [0, 0, 0, 0, -0.58, -0.58, -0.58, 0, 0, 0]
e3 = [0, 0, 0, 0, 0, 0, 0, 0.71, 0.71, 0 ]
e4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ]

# Create the plot
plt.stem(x, e1, linefmt='b-', markerfmt='bo', basefmt='k-', label="e1")
plt.stem(x, e2, linefmt='r-', markerfmt='ro', basefmt='k-', label="e2")
plt.stem(x, e3, linefmt='g-', markerfmt='go', basefmt='k-', label="e3")
plt.stem(x, e4, linefmt='m-', markerfmt='mo', basefmt='k-', label="e4")

# Add a title and labels
plt.title("")
plt.xlabel("Indeks cvora grafa")
plt.ylabel("Vrijednost koordinate sopstvenog vektora")
plt.legend()

# Save the plot as a PNG file
# plt.savefig("plot.png")
plt.show()

# Optionally, close the plot if not showing in the same script
plt.close()
