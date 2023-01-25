#!/bin/python

from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform

# Create an instance of ModbusServer
server = ModbusServer("127.0.0.1", 5021, no_block=True)

try:
    print("Start server...")
    server.start()
    print("Server is online")
    state = [0]
    while True:
        server.data_bank.set_holding_registers(17, [int(uniform(0, 100))])
        if state != server.data_bank.get_holding_registers(17):
            state = server.data_bank.get_holding_registers(17)
            print("Value of Register 17 has changed to " +str(state))
        sleep(0.5)

except:
    print("Shutdown server ...")
    server.stop()
    print("Server is offline")

