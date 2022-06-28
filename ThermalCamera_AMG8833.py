# https://qiita.com/tm_nagoya/items/904ba8a23868ddcdcc54
# https://qiita.com/tm_nagoya/items/32d7e5becf73ba8a6110


import cv2
import time
import busio
import board

import adafruit_amg88xx

import matplotlib.pyplot as plt

import functions_common as fun

from scipy.interpolate import griddata

import numpy as np

datafolder = '/home/pi/NAS/'

# Initialization
i2c_bus = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_amg88xx.AMG88XX(i2c_bus, addr=0x68)
time.sleep(.1)  # Wait for initialization

# Get data
_, timestamp = fun.get_time_now()
sensordata = sensor.pixels

# Plot
# fig1 = plt.imshow(sensordata, cmap="inferno", interpolation="bicubic")
# plt.colorbar()
#
# plt.savefig(datafolder + timestamp + '.png')    # Save figure to NAS
# plt.show()
#
# fun.save_list_to_csv(datafolder + timestamp + '.csv', sensordata)   # Save data to NAS

# Resize data and plot new figure
# image_array = np.array(sensordata, np.float32)
# data = cv2.cvtColor(image_array,cv2.COLOR_GRAY2BGR)
#
# cv2.imwrite(datafolder + timestamp + '.png', image_array)
#
# data_new = cv2.imread(datafolder + timestamp + '.png')
# print(data_new)

data = np.array(sensordata)

# x = np.arange(0,8,1)
# y = np.arange(0,8,1)
# X, Y = np.meshgrid(x,y)
#
# npts = 100
# px, py = np.random.choice(x, npts), np.random.choice(y, npts)

x = np.arange(0,8,1)
y = np.arange(0,8,1)

X,Y = np.meshgrid(x,y)

print((X, Y))

x_new = np.linspace(0,7,100)
y_new = np.linspace(0,7,100)

xx,yy = np.meshgrid(x_new,y_new)

result = griddata((X, Y), data.flatten(), (xx, yy), method='cubic')

print()

print(result)
# Ti = griddata((px, py), data, (X, Y), method='cubic')

