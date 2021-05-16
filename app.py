import paho.mqtt.client as mqtt #import the client1
import time

addr,port = "localhost", 9000;
xAxis = mqtt.Client("X Axis");
yAxis = mqtt.Client("Y Axis");

xList = [];
yList = [];

def on_messageX(client, userdata, message):
  print("xMessage recevied");
  xList.append(float(message.payload.decode("utf-8")));

def on_messageY(client, userdata, message):
  print("yMessage recevied");
  yList.append(float(message.payload.decode("utf-8")));

xAxis.on_message = on_messageX;
yAxis.on_message = on_messageY;


print("Connecting to broker")
xAxis.connect(addr,port=port)
yAxis.connect(addr,port=port)

xAxis.loop_start();
yAxis.loop_start();


xAxis.subscribe("topic/Gyroscope/x")
yAxis.subscribe("topic/Gyroscope/y")

time.sleep(5)

xAxis.loop_stop();
yAxis.loop_stop();




