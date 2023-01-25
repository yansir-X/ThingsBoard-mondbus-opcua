"""
This is the opc ua demo server python script.
Running this script will start a demo opc ua server with default parameters i.e. temperature & pressure.
You can edit the code to add more parameters as per your requirement

NOTE: Change the URL with the IP address of your system. If 4840 port is blocked, you can use any other port

"""

from opcua import Server
from random import randint
import time


server = Server()
url = "opc.tcp://10.83.240.122:4840/"
server.set_endpoint(url)
name = "Rocket_Systems_OPCUA_Simulation_Server"
idx = server.register_namespace(name)

device = server.get_objects_node().add_object(idx, "Device1")
name = device.add_variable(idx, "serialNumber", "OPCUADevice")
name.set_writable()


temperature_and_humidity = device.add_object(idx, "TemperatureAndHumiditySensor")
temperature = temperature_and_humidity.add_variable(idx, "Temperature", 56.7)
humidity = temperature_and_humidity.add_variable(idx, "Humidity", 68.7)
temperature.set_writable()
humidity.set_writable()

server.start()
print("Server started at {}".format(url))

while True:
   temp= randint(-10, 40)
   press= randint(200, 999)
   print(temp, press)#
   temperature.set_value(temp)
   humidity.set_value(press)#
   time.sleep(4)#
