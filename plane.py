import matplotlib.pyplot as plt

# Given coordinates
alpha2_x = [-0.32, -0.3, -0.26, -0.19, -0.1, 0.0, 0.1, 0.19, 0.26, 0.3, 0.32, 0.3, 0.26, 0.19, 0.1, 0.0, -0.1, -0.19, -0.26, -0.3]
alpha3_y = [-0.0, 0.09, 0.18, 0.25, 0.3, 0.32, 0.3, 0.26, 0.19, 0.1, 0.0, -0.09, -0.18, -0.25, -0.3, -0.32, -0.3, -0.26, -0.19, -0.1]

alpha2_x.append(alpha2_x[0])
alpha3_y.append(alpha3_y[0])

# Plot the points and connect them
plt.figure(figsize=(6, 6))
plt.plot(alpha2_x, alpha3_y, marker='o', color='blue', linestyle='-', markersize=8, label="čvorovi")  # Connect the dots with lines
plt.scatter(alpha2_x, alpha3_y, color='red', s=100, zorder=5)  # Emphasize the dots with red color and bigger size
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xlabel("e2")
plt.ylabel("e3")
plt.title("Spectral graph drawing")
plt.legend()
plt.show()
