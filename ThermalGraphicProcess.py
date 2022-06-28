# https://stackoverflow.com/questions/50330251/how-to-merge-mesh-grid-points-from-two-rectangles-in-python
# https://qiita.com/shu32/items/f19635eab402ea6fc44e


import numpy as np
from scipy.interpolate import griddata
import functions_common as fun
import matplotlib.pyplot as plt


filename = '/home/pi/NAS/20220629000339.csv'

data = fun.read_csv_as_list(filename)
data = np.array(data)

# Resize data and plot new figure
# image_array = np.array(sensordata, np.float32)
# data = cv2.cvtColor(image_array,cv2.COLOR_GRAY2BGR)
#
# cv2.imwrite(datafolder + timestamp + '.png', image_array)
#
# data_new = cv2.imread(datafolder + timestamp + '.png')
# print(data_new)


# x = np.arange(0,8,1)
# y = np.arange(0,8,1)
# X, Y = np.meshgrid(x,y)
#
# npts = 100
# px, py = np.random.choice(x, npts), np.random.choice(y, npts)

x = np.linspace(0,7,8)
y = np.linspace(0,7,8)

x, y = np.meshgrid(x, y)
positions = np.vstack([x.ravel(), y.ravel()])
theGridPoints = (np.array(positions)).T


X,Y = np.meshgrid(x,y)


x_new = np.linspace(0,7,1000)
y_new = np.linspace(0,7,1000)

xx,yy = np.meshgrid(x_new,y_new)

result = griddata(theGridPoints, data.flatten().T, (xx, yy), method='cubic')

plt.subplots(figsize=(8, 4))

plt.subplot(1, 2, 1)
fig = plt.imshow(data, cmap="inferno")
plt.colorbar()

plt.subplot(1, 2, 2)
fig = plt.imshow(result, cmap="inferno")
plt.colorbar()
plt.show()
