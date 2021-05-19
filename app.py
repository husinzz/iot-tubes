import paho.mqtt.client as mqtt
import time
import math # Perlu buat atan

addr,port = "localhost", 9000; # init address broker sama port
xAxis = mqtt.Client("X Axis"); # init client buat kedua axis
yAxis = mqtt.Client("Y Axis");
zAxis = mqtt.Client("Z Axis");

xList = []; # list buat simpen hasil gerakan gyro
yList = [];
zList = [];

def on_messageX(client, userdata, message):
  # print("xMessage recevied");
  xList.insert(0,float(message.payload.decode("utf-8")));

def on_messageY(client, userdata, message):
  # print("yMessage recevied");
  yList.insert(0,float(message.payload.decode("utf-8")));

def on_messageZ(client, userdata, message):
  # print("zMessage recevied");
  zList.insert(0,float(message.payload.decode("utf-8")));

# def getRoll(x,y):
#   return(math.atan2(y,x))

# def getPitch(x,y,z):
#   roll = getRoll(x,y)
#   return(math.atan(
#     -x/(
#       (y * math.sin(roll)) + 
#       (z * math.cos(roll))
#   )))

# def getHeading(x,y,z):
#   pitch = getPitch(x,y,z);
#   roll = getRoll(x,y)
#   return(math.atan2(
#     ((z*math.sin(roll)) - (y*math.cos(roll))),
#     ((x*math.cos(pitch)) + (y*math.sin(pitch)*math.sin(roll)) + (z*math.sin(pitch)*math.cos(roll)))
#   ))

def getRoll(y,z):
  return math.atan2(y, z) * 57.3

def getPitch(x,y,z):
  return math.atan2(-x, math.sqrt(y*y + z*z)) * 57.3


xAxis.on_message = on_messageX; # init nama fungsi yang nanti di panggil saat loop
yAxis.on_message = on_messageY;
zAxis.on_message = on_messageZ;

print("Connecting to broker")
xAxis.connect(addr,port=port) # menghubungkan dengan broker ( Mosquito yang skrng di pake)
yAxis.connect(addr,port=port)
zAxis.connect(addr,port=port)

while True:
  xAxis.loop_start(); # awal loop
  yAxis.loop_start();
  zAxis.loop_start();
  xAxis.subscribe("topic/Accelerometer/x") # sub ke topic, sesuai sama yang di set di 
  yAxis.subscribe("topic/Accelerometer/y") # sensor node
  zAxis.subscribe("topic/Accelerometer/z")
  xAxis.loop_stop();
  yAxis.loop_stop();
  zAxis.loop_stop();

   # delay buat nuggu masuk gyro, sesuai sama delay gyro di sensor node
  if (xList != []) & (yList != []) & (zList != []):
    print(getPitch(xList[0],yList[0],zList[0]))
    print(len(xList),len(yList),len(zList))

