import numpy as np
import matplotlib.pyplot as plt
import sys

file_names = sys.argv[1:]

first_data = np.loadtxt(file_names[0], delimiter=',')
mean_surface = np.zeros_like(first_data)

avg_height = None

for file_name in file_names:
    data = np.loadtxt(file_name, delimiter=',')

    data = np.resize(data, first_data.shape)

    mean_surface += data

    height = np.mean(data, axis=1)
    if avg_height is None:
        avg_height = height
    else:
        avg_height += height

mean_surface /= len(file_names)
avg_height /= len(file_names)

plt.imshow(mean_surface)
plt.colorbar()
plt.savefig("mean_surface.png")
plt.show()

plt.plot(avg_height, label='All Files', color='k')

for file_name in file_names:
    data = np.loadtxt(file_name, delimiter=',')
    height = np.mean(data, axis=0)
    plt.plot(height, label=file_name, alpha=0.3, color='k')

plt.xlabel('X-axis')
plt.ylabel('Average Height')
plt.savefig("surface_compare.png")
plt.show()
