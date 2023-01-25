from random import uniform
from time import sleep
from opcua import Server

server=Server()
server.set_endpoint("opc.tcp://127.0.0.1:4840/")
server.register_namespace("Room1")
objects=server.get_objects_node()

temsens=objects.add_object('ns=2; s="TS1"', "Temp Sensor1")

temsens.add_variable('ns=3; s="TS1_VendorName"', "Sensor","Sensor King")
temp=temsens.add_variable('ns=3; s="humidity"', "Sensor", "12345")

bulb=objects.add_object(2, 'Light Bulb')
state=bulb.add_variable(2, "State of Light Bulb", False)

temperature= 22
print("Start server")
server.start()
while True:
    temperature += uniform(-1, 1)
    temp.set_value(temperature)
    print("New temp: " + str(temp.get_value()))
    print("State of light bulb")
    print(str(state.get_value()))
    sleep(2)
server.stop()


