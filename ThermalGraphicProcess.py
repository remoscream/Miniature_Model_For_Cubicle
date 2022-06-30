"""
Program for resize a 8x8 thermal graphic from AMG8833 by a new resolution

Referenced program of scipy.griddata is from:
https://stackoverflow.com/questions/50330251/how-to-merge-mesh-grid-points-from-two-rectangles-in-python
https://qiita.com/shu32/items/f19635eab402ea6fc44e

Document for scipy.interpolate:
https://docs.scipy.org/doc/scipy/reference/interpolate.html
"""

import numpy as np
from scipy.interpolate import griddata
import functions_common as fun
import matplotlib.pyplot as plt


# Set new resolution and method of interpolation
resolution = 100
method_interpolation = 'cubic'  # You can use 'linear', 'nearest' and 'cubic'

# Read a data file in NAS(not from sensor)
filename = '/home/pi/NAS/20220629000339.csv'

data = fun.read_csv_as_list(filename)
data = np.array(data)
value = data.flatten()  # Data need to be 1 dimension for scipy.griddata

# As AMG8833 only output 8x8 thermal graphic
# Create points (coordinates) with 8x8 meshgrid
x = np.linspace(0, 7, 8)
y = np.linspace(0, 7, 8)
x, y = np.meshgrid(x, y)
coordinates = np.vstack([x.ravel(), y.ravel()])
points = (np.array(coordinates)).T

# Create new mesh points with a new resolution
x_new = np.linspace(0, 7, resolution)
y_new = np.linspace(0, 7, resolution)
xx, yy = np.meshgrid(x_new, y_new)

# Resize thermal graphic from 8x8 to a new resolution
result = griddata(points, value, (xx, yy), method=method_interpolation)

# Plot data and save to figure
plt.subplots(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(data, cmap="inferno")
plt.colorbar()

plt.subplot(1, 2, 2)
plt.imshow(result, cmap="inferno")
plt.colorbar()

plt.savefig('/home/pi/NAS/data.png')    # Save figure to NAS
plt.show()
