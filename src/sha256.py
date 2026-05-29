def charToHex(msg):
    tmp = msg.encode('utf-8')
    return int(tmp.hex(),16)

def rightRotate(x, n):
    hasil = ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF
    return hasil

def shiftRight(x,n):
    hasil = (x>>n)&0xFFFFFFFF
    return hasil

#Sigma besar 0 dan 1 untuk mengacak variabel kerja a dan e di setiap ronde kompresi.
def Sigma1(x):
    hasil = rightRotate(x,6)^rightRotate(x,11),rightRotate(x,25)
    return hasil

def Sigma0(x):
    hasil = rightRotate(x,2)^rightRotate(x,13),shiftRight(x,22)
    return hasil

# sigma kecil 0 & 1 digunakan untuk ekspansi pesan untuk menghitung nilai $W_{16}$ hingga $W_{63}$
def sigma0(x):
    hasil = rightRotate(x,7)^rightRotate(x,18),shiftRight(x,3)
    return hasil

def sigma1(x):
    hasil = rightRotate(x,17)^rightRotate(x,19),shiftRight(x,10)
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

