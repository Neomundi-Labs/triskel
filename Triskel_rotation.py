import matplotlib.pyplot as plt
from triskel import triskel_trajectory

trajectory = triskel_trajectory(steps=3000, rotation_rate=0.01)

plt.figure(figsize=(6, 6))
plt.plot(trajectory[:, 0], trajectory[:, 1], linewidth=0.8)
plt.axis("equal")
plt.axis("off")
plt.title("Triskel – bounded cyclic circulation", fontsize=10)
plt.show()
