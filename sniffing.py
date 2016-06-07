import struct

ms = struct.pack('hhl', 1,2)
print (ms)
k = struct.unpack('hhl',ms)
print k
