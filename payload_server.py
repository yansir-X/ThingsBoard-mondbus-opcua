"""Pymodbus Server Payload Example.

This example shows how to initialize a server with a
complicated memory layout using builder.
"""
import asyncio
import logging

from pymodbus.constants import Endian
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusServerContext,
    ModbusSlaveContext,
)
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.server.async_io import StartAsyncTcpServer

from pymodbus.version import version

# set logging level for library.
logging.getLogger().setLevel(logging.DEBUG)


async def run_payload_server():
    """Run payload server."""
    # ----------------------------------------------------------------------- #
    # build your payload
    # ----------------------------------------------------------------------- #
    builder = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Little)
    builder.add_string("a")
  
    # ----------------------------------------------------------------------- #
    # use that payload in the data store
    # Here we use the same reference block for each underlying store.
    # ----------------------------------------------------------------------- #

    block = ModbusSequentialDataBlock(1, builder.to_registers())
    store = ModbusSlaveContext(di=block, co=block, hr=block, ir=block)
    context = ModbusServerContext(slaves=store, single=True)

    server = await StartAsyncTcpServer(
        context,
        address=("10.83.240.122", 5021),
        allow_reuse_address=True,
        defer_start=True,
    )

    asyncio.get_event_loop().call_later(20, lambda: server.serve_forever)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(run_payload_server())
