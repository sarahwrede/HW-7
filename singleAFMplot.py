import sys
import os
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print("Usage: python singleAFMplot.py <filename>")
    sys.exit()

filename = sys.argv[1]

if not os.path.isfile(filename):
    print(f"Error: {filename} does not exist")
    sys.exit()

data = np.loadtxt(filename, delimiter=',')

plt.imshow(data, cmap='hot', interpolation='nearest')
plt.title(os.path.splitext(os.path.basename(filename))[0])
plt.colorbar()

output_filename = os.path.splitext(filename)[0] + ".png"
plt.savefig(output_filename)

plt.show()
