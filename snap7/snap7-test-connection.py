import snap7
from snap7.util import *

plc = snap7.client.Client()
plc.connect('192.168.1.70', 0, 1)
print("Connection succeeded: ", plc.get_connected())
plc.disconnect()