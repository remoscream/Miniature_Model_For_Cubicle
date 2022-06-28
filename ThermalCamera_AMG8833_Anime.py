# -*- coding: utf-8 -*-

import time
import busio
import board

import adafruit_amg88xx

# import matplotlib
# matplotlib.use("QtAgg")  # Do this before importing pyplot!

import matplotlib.pyplot as plt

# I2Cバスの初期化
i2c_bus = busio.I2C(board.SCL, board.SDA)

# センサーの初期化
sensor = adafruit_amg88xx.AMG88XX(i2c_bus, addr=0x68)

# センサーの初期化待ち
time.sleep(.1)

# 8x8ピクセルの画像とbicubic補間をした画像を並べて表示させる
plt.subplots(figsize=(8, 4))

# ループ開始
while True:
    # データ取得
    sensordata = sensor.pixels

    # bicubicのデータ
    fig = plt.imshow(sensordata, cmap="inferno", interpolation="bicubic")

    plt.colorbar()
    plt.show()
    # plt.showだと止まってしまうので、pauseを使用
    # plt.clfしないとカラーバーが多数表示される
    plt.pause(.1)
    plt.clf()