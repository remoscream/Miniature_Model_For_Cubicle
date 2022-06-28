# https://qiita.com/tm_nagoya/items/904ba8a23868ddcdcc54
# https://qiita.com/tm_nagoya/items/32d7e5becf73ba8a6110


import time
import busio
import board
import adafruit_amg88xx
import matplotlib.pyplot as plt
import functions_common as fun

datafolder = '/home/pi/NAS/'

# Initialization
i2c_bus = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_amg88xx.AMG88XX(i2c_bus, addr=0x68)
time.sleep(.1)  # Wait for initialization

# Get data
_, timestamp = fun.get_time_now()
sensordata = sensor.pixels

# Plot
fig1 = plt.imshow(sensordata, cmap="inferno", interpolation="bicubic")
plt.colorbar()

plt.savefig(datafolder + timestamp + '.png')    # Save figure to NAS
plt.show()

fun.save_list_to_csv(datafolder + timestamp + '.csv', sensordata)   # Save data to NAS





