#liveplot

# adding a python comment here
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import datetime
import serial
import json


class ScalarSensor(object):
    def __init__(self,address = "COM7",baudrate = 9600,timeout =1):
        self.sensor = serial.Serial(port = address, baudrate = baudrate, timeout = timeout)
        self.retry =0
    def get_reading(self,number_retries = 3):
        """Returns the current reading as a dictionary"""
        try:
            output = json.loads(self.sensor.readline().decode())
            control_time = datetime.datetime.now()
            output["controller_time"]=str(control_time)
            self.retry = 0
            return output
        except:
            fail_time  = datetime.datetime.now()
            print(f"failed attempt at {fail_time}")
            self.retry +=1
            if self.retry < number_retries:
                self.get_reading()
            else:
                raise
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sensor.close()

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
sensor = ScalarSensor()
reading = sensor.get_reading()
data ={key:[] for key in reading.keys()}
print(data)
def animate(i):
    reading = sensor.get_reading()
    for key,value in reading.items():
        data[key].append(value)
    x = list(map(lambda x:datetime.datetime.fromisoformat(x),data['controller_time']))
    ax1.clear()
    for key,value in data.items():
        if key!="controller_time":
            ax1.plot(x,value,label = key)
    ax1.legend()
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
sensor.sensor.close(