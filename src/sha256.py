def rightRotate(x, n):
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

def shiftRight(x, n):
    return (x >> n) & 0xFFFFFFFF

def Sigma0(x):
    return rightRotate(x, 2) ^ rightRotate(x, 13) ^ rightRotate(x, 22)

def Sigma1(x):
    return rightRotate(x, 6) ^ rightRotate(x, 11) ^ rightRotate(x, 25)

def sigma0(x):
    return rightRotate(x, 7) ^ rightRotate(x, 18) ^ shiftRight(x, 3)

def sigma1(x):
    return rightRotate(x, 17) ^ rightRotate(x, 19) ^ shiftRight(x, 10)

def Ch(x, y, z):
    # Memperbaiki bug signed integer NOT di Python
    return (x & y) ^ ((~x & 0xFFFFFFFF) & z)

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

    print(len(msg_bytes))
    return msg_bytes


def expand_msg (W0_15):
    W = list(W0_15)+[0]*48
    print(len(W))

    for i in range(16,64):
        W[i] = (W[i-16] + sigma0(W[i-15]) + W[i-7] + sigma1(W[i-2]) ) & 0xFFFFFFFF

    return W

def compress_block(W, K, H_awal):
    a, b, c, d, e, f, g, h = H_awal

    for i in range(64):
        # Hitung Nilai Tambahan T1 dan T2
        T1 = (h + Sigma1(e) + Ch(e, f, g) + K[i] + W[i]) & 0xFFFFFFFF
        T2 = (Sigma0(a) + Maj(a, b, c)) & 0xFFFFFFFF

        h=g
        g=f
        f=e
        e=(d + T1) & 0xFFFFFFFF
        d=c
        c=b
        b=a
        a=(T1 + T2) & 0xFFFFFFFF

        # Cetak data khusus untuk Iterasi 0 dan Iterasi 1 sesuai soal
        if i == 0 or i == 1:
            print(f"=== HASIL ITERASI {i} ===")
            print(f"a: {hex(a)}, b: {hex(b)}, c: {hex(c)}, d: {hex(d)}")
            print(f"e: {hex(e)}, f: {hex(f)}, g: {hex(g)}, h: {hex(h)}\n")



    H_akhir = [
        (H_awal[0] + a) & 0xFFFFFFFF,
        (H_awal[1] + b) & 0xFFFFFFFF,
        (H_awal[2] + c) & 0xFFFFFFFF,
        (H_awal[3] + d) & 0xFFFFFFFF,
        (H_awal[4] + e) & 0xFFFFFFFF,
        (H_awal[5] + f) & 0xFFFFFFFF,
        (H_awal[6] + g) & 0xFFFFFFFF,
        (H_awal[7] + h) & 0xFFFFFFFF
    ]
    return H_akhir
