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

# sigma kecil 0 & 1 digunakan untuk ekspansi pesan untuk menghitung nilai W16 hingga W63
def sigma0(x):
    hasil = rightRotate(x,7)^rightRotate(x,18),shiftRight(x,3)
    return hasil

def sigma1(x):
    hasil = rightRotate(x,17)^rightRotate(x,19),shiftRight(x,10)
    return hasil


# ch = (e and f) xor ((not e) and g)
def Ch(x, y, z):
    return (x & y) ^ (~x & z)

# maj = (a and b) xor (a and c) xor (b and c)
def Maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)


def pad_message(text_input):
    msg_bytes = bytearray(text_input, 'utf-8')
    
    panjang_asli_bit = len(msg_bytes) * 8
    
    msg_bytes.append(0x80)
    

    while len(msg_bytes) % 64 != 56:
        msg_bytes.append(0x00)
        

    panjang_bita = panjang_asli_bit.to_bytes(8, byteorder='big')
    msg_bytes.extend(panjang_bita)
    
    return msg_bytes


msg_padded = pad_message("hello world")

W = []
for i in range(0, len(msg_padded), 4):
    # Ambil 4 bit sekaligus, gabungkan jadi satu integer 32-bit = 1 W
    satu_kata = int.from_bytes(msg_padded[i:i+4], byteorder='big')
    W.append(satu_kata)

print{format(W[15], '032b')}
# msg = "abcd"
# msg = charToHex(msg)
# print(type(msg))

# rotateRightHasil = rightRotate(msg,7)
# print(hex(msg))
# print(hex(rotateRightHasil))
# print(hex(shiftRight(msg,7)))
# print(format (rotateRightHasil,'032b'))
# print(format (shiftRight(msg,7),'032b'))
# print(format (msg,'032b'))

