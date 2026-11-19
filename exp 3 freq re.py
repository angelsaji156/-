import numpy as np
import matplotlib.pyplot as plt

# 1. Basic parameters
R = 1                      # Cell radius (km)
N = 7                      # Cluster size
D = np.sqrt(3 * N) * R     # Reuse distance formula

# Coordinates and colors for the 7 cells
x = [0, 2, 1, -1, -2, -1, 1]
y = [0, 0, 1.73, 1.73, 0, -1.73, -1.73]
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet']

# 2. Function to draw one hexagon cell
def draw_cell(cx, cy, col, name):
    a = np.linspace(0, 2 * np.pi, 7)
    plt.fill(cx + R * np.cos(a), cy + R * np.sin(a), color=col, edgecolor='black', alpha=0.6)
    plt.text(cx, cy, name, ha='center', va='center', fontweight='bold')

# 3. Draw both clusters using one simple loop
plt.figure(figsize=(10, 5))
shift = D + 2              # Distance to shift the second cluster

for i in range(7):
    draw_cell(x[i], y[i], colors[i], f"F{i+1}")           # Cluster 1
    draw_cell(x[i] + shift, y[i], colors[i], f"F{i+1}")   # Cluster 2

# 4. Draw Reuse Distance line between the two F1 cells
plt.plot([0, shift], [0, 0], 'ko--')
plt.text(shift / 2, 0.3, f"Reuse Distance D = {D:.2f} km", ha='center', fontweight='bold')

plt.title(f"Cellular Frequency Reuse (Cluster Size N = {N})")
plt.axis('equal')
plt.axis('off')
plt.show()