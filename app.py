import paho.mqtt.client as mqtt
import os
import math
import time
import beepy

addr, port = "localhost", 9000
xAxis = mqtt.Client("X Axis")
yAxis = mqtt.Client("Y Axis")
zAxis = mqtt.Client("Z Axis")

xList = []
yList = []
zList = []


def on_messageX(client, userdata, message):
    # print("xMessage recevied");
    xList.insert(0, float(message.payload.decode("utf-8")))


def on_messageY(client, userdata, message):
    # print("yMessage recevied");
    yList.insert(0, float(message.payload.decode("utf-8")))


def on_messageZ(client, userdata, message):
    # print("zMessage recevied");
    zList.insert(0, float(message.payload.decode("utf-8")))


def getRoll(y, z):
    return math.atan2(y, z) * 57.3


def getPitch(x, y, z):
    return math.atan2(math.sqrt(y*y + z*z), -x) * 57.3


def getData():
    xAxis.loop_start()
    xAxis.subscribe("topic/Accelerometer/x")
    xAxis.loop_stop()

    yAxis.loop_start()
    yAxis.subscribe("topic/Accelerometer/y")
    yAxis.loop_stop()

    zAxis.loop_start()
    zAxis.subscribe("topic/Accelerometer/z")
    zAxis.loop_stop()


xAxis.on_message = on_messageX
yAxis.on_message = on_messageY
zAxis.on_message = on_messageZ

print("Connecting to broker")
xAxis.connect(addr, port=port)
yAxis.connect(addr, port=port)
zAxis.connect(addr, port=port)

while True:
    # os.system('clear')
    getData()
    if (xList != []) & (yList != []) & (zList != []):
        roll = getRoll(yList[0], zList[0])
        # print(len(xList), len(yList), len(zList))
        print(roll)

        if (roll > 60) and (roll < 85):
            # os.system("clear")
            print('Youre good')
            print(roll)
        elif (roll > 86) and (roll < 95):
            # os.system("clear")
            beepy.beep(sound=1)
            print(roll)
            print('Correct your posture')
        elif (roll > 96):
            # os.system("clear")
            beepy.beep(sound=2)
            print(roll)
            print("Youre posture is broken")
