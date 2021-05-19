import time;
import math;
import numpy as np;
import pandas as pd;

data = pd.DataFrame(pd.read_csv('raw.csv').rolling(window=1).mean())

xList = data.iloc[:]['Acceleration x (m/s^2)']
yList = data.iloc[:]['Acceleration y (m/s^2)']
zList = data.iloc[:]['Acceleration z (m/s^2)']

def getRoll(y,z):
  return math.atan2(y, z) * 57.3

def getPitch(x,y,z):
  return math.atan2(math.sqrt((y*y) + (z*z)), -x) * 57.3

# for i in range(len(xList)):
i = 0
print(getPitch(xList[i],yList[i],zList[i]))
