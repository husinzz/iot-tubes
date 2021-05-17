import paho.mqtt.client as mqtt
import time
import math # Perlu buat atan

addr,port = "localhost", 9000; # init address broker sama port
xAxis = mqtt.Client("X Axis"); # init client buat kedua axis
yAxis = mqtt.Client("Y Axis");

xList = []; # list buat simpen hasil gerakan gyro
yList = [];
Roll = [];

def on_messageX(client, userdata, message):
  # print("xMessage recevied");
  xList.insert(0,float(message.payload.decode("utf-8")));

def on_messageY(client, userdata, message):
  # print("yMessage recevied");
  yList.insert(0,float(message.payload.decode("utf-8")));

def getRoll(xList,yList):
  return(math.atan2(yList[0],xList[0]))

xAxis.on_message = on_messageX; # init nama fungsi yang nanti di panggil saat loop
yAxis.on_message = on_messageY;

print("Connecting to broker")
xAxis.connect(addr,port=port) # menghubungkan dengan broker ( Mosquito yang skrng di pake)
yAxis.connect(addr,port=port)

while True:
  xAxis.loop_start(); # awal loop
  yAxis.loop_start();

  xAxis.subscribe("topic/Gyroscope/x") # sub ke topic, sesuai sama yang di set di 
  yAxis.subscribe("topic/Gyroscope/y") # sensor node

  time.sleep(1) # delay buat nuggu masuk gyro, sesuai sama delay gyro di sensor node

  xAxis.loop_stop();
  yAxis.loop_stop();

  Roll.insert(0,getRoll(xList,yList))
  Temp = -9999

  if ((Roll[0] < -2)):
    print("Bongkok")
    
    if (Temp != Roll[0]):
      print(Roll[0])
    Temp = Roll[0]
  else:
    print("Tegak")

    if (Temp != Roll[0]):
      print(Roll[0])
    Temp = Roll[0]
    

  # print(xList)
  # print(yList)


