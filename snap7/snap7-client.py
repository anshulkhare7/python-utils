from time import sleep
import snap7
from snap7.util import *

plc = snap7.client.Client()
plc.connect('192.168.1.3', 0, 1) 
area1 = 0x83 #srvAreaMK
area2 = 0x82 #srvAreaPA
area3 = 0x81 #srvAreaPE

start = 0
length = 4
float1 = plc.read_area(area1, 0, start, length)
float2 = plc.read_area(area2, 0, start, length)
float3 = plc.read_area(area3, 0, start, length)

print("Area=MK, [0,4]=",format(get_real(float1,0)))
print("Area=PA, [0,4]=",format(get_real(float2,0)))
print("Area=PE, [0,4]=",format(get_real(float3,0)))

plc.disconnect()