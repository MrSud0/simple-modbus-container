import logging
from pymodbus.server.async_io import StartAsyncTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.device import ModbusDeviceIdentification
import asyncio
import argparse

# Set up logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

async def run_modbus_server(address, port, hr_values):
    # Convert the comma-separated string of values to a list of integers
    hr_values = [int(x) for x in hr_values.split(",")]

    # Create data store with initial values
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(1, [17]*100),
        co=ModbusSequentialDataBlock(1, [17]*100),
        hr=ModbusSequentialDataBlock(1, hr_values),  # Initialize holding registers with given values
        ir=ModbusSequentialDataBlock(1, [17]*100))
    context = ModbusServerContext(slaves=store, single=True)

    # Create server identity
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
    identity.ProductName = 'pymodbus Server'
    identity.ModelName = 'pymodbus Server'
    identity.MajorMinorRevision = '1.0'

    # Verify initial values
    hr_values = store.getValues(3, 0, count=len(hr_values))  # Start at address 0
    log.info(f"Initial Holding Register Values: {hr_values}")

    # Run async server
    await StartAsyncTcpServer(context, identity=identity, address=(address, port))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Modbus Server Script')
    parser.add_argument('--address', type=str, default='0.0.0.0', help='Address for the Modbus server')
    parser.add_argument('--port', type=int, default=5020, help='Port for the Modbus server')
    parser.add_argument('--hr-values', type=str, default='10,20,30,40', help='Comma-separated list of initial holding register values')

    args = parser.parse_args()

    asyncio.run(run_modbus_server(args.address, args.port, args.hr_values))
