def charToHex(msg):
    tmp = msg.encode('utf-8')
    return int(tmp.hex(),16)

def rightRotate(x, n):
    hasil = ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF
    return hasil

def shiftRight(x,n):
    hasil = (x>>n)&0xFFFFFFFF
    return hasil


msg = "abcd"
msg = charToHex(msg)
print(type(msg))

rotateRightHasil = rightRotate(msg,7)
print(hex(msg))
print(hex(rotateRightHasil))
print(hex(shiftRight(msg,7)))
print(format (rotateRightHasil,'032b'))
print(format (shiftRight(msg,7),'032b'))
print(format (msg,'032b'))

