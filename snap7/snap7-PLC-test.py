import snap7.client as c
from snap7.util import *
from snap7.snap7types import *


def ReadMemory(plc,byte,bit,datatype):
    result = plc.read_area(areas['MK'],0,byte,datatype)
    if datatype==S7WLBit:
        return get_bool(result,0,bit)
    elif datatype==S7WLByte or datatype==S7WLWord:
        return get_int(result,0)
    elif datatype==S7WLReal:
        return get_real(result,0)
    elif datatype==S7WLDWord:
        return get_dword(result,0)
    else:
        return None

def WriteMemory(plc,byte,bit,datatype,value):
    result = plc.read_area(areas['MK'],0,byte,datatype)
    if datatype==S7WLBit:
        set_bool(result,0,bit,value)
    elif datatype==S7WLByte or datatype==S7WLWord:
        set_int(result,0,value)
    elif datatype==S7WLReal:
        set_real(result,0,value)
    elif datatype==S7WLDWord:
        set_dword(result,0,value)
    plc.write_area(areas['MK'],0,byte,result)

if __name__=="__main__":
    plc = c.Client()
    plc.connect('192.168.1.70',0,1)
    print("Connected? ", plc.get_connected())
    print("CPU Info ", plc.get_cpu_state())
    
    start = 100
    length = 1
    bit = 2
    byte = plc.read_area(0x83, 0, start, length)
    print("Before writing MK: ", get_bool(byte, 0, bit))

    bit_ = 0
    result = plc.read_area(0x83, 0, 100, S7WLBit)
    set_bool(result,0,bit_, 0) # last param in this is the value we want to set (http://simplyautomationized.blogspot.com/2016/02/python-snap7-s7-1200-simple-example.html)
    plc.write_area(0x83,0,100,result)

    # byte = plc.read_area(0x83, 0, start, length)
    # print("After writing MK: ", get_bool(byte, 0, bit))

    #DONE!!