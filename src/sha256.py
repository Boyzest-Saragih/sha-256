# Memutar bit ke kanan sebanyak n posisi dan memastikan hasilnya tetap 32 bit
def rightRotate(x, n):
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

# Menggeser bit ke kanan sebanyak n posisi (bit baru di kiri diisi 0)
def shiftRight(x, n):
    return (x >> n) & 0xFFFFFFFF

# Fungsi Sigma Besar (Sigma0 & Sigma1) digunakan dalam proses kompresi blok utama
def Sigma0(x):
    return rightRotate(x, 2) ^ rightRotate(x, 13) ^ rightRotate(x, 22)

def Sigma1(x):
    return rightRotate(x, 6) ^ rightRotate(x, 11) ^ rightRotate(x, 25)

# Fungsi sigma kecil (sigma0 & sigma1) digunakan saat memperluas pesan (Message Schedule)
def sigma0(x):
    return rightRotate(x, 7) ^ rightRotate(x, 18) ^ shiftRight(x, 3)

def sigma1(x):
    return rightRotate(x, 17) ^ rightRotate(x, 19) ^ shiftRight(x, 10)


# Choose: Jika bit pada x adalah 1 maka pilih bit dari y, jika 0 pilih bit dari z
def Ch(x, y, z):
    return (x & y) ^ ((~x & 0xFFFFFFFF) & z)

# Majority: Mengembalikan bit yang paling banyak muncul (mayoritas) di antara x, y, dan z
def Maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)


# memastikan ukuran pesan memenuhi syarat blok berukuran 512-bit (64 byte)
def pad_message(text_input):
    msg_bytes = bytearray(text_input, 'utf-8')
    
    # Menyimpan panjang pesan asli dalam satuan bit
    panjang_asli_bit = len(msg_bytes) * 8
    
    # Menambahkan bit 1 pertama setelah pesan (0x80 dalam biner adalah 10000000)
    msg_bytes.append(0x80)
    
    # Menambahkan byte 0x00 (padding) hingga menyisakan 8 byte (64 bit) kosong di akhir blok 64-byte
    while len(msg_bytes) % 64 != 56:
        msg_bytes.append(0x00)
        

    # Memasukkan panjang asli pesan (8 byte / 64 bit) ke bagian paling akhir blok
    panjang_bita = panjang_asli_bit.to_bytes(8, byteorder='big')
    msg_bytes.extend(panjang_bita)

    print(len(msg_bytes))
    return msg_bytes

# mengambil 16 kata (word) pertama hasil pembagian blok data 512-bit (masing-masing 32-bit), lalu mengekspansinya menjadi total 64 kata untuk digunakan di setiap ronde iterasi
def expand_msg (W0_15):
    # Diperluas dengan membuat array kosong berukuran total 64 kata
    W = list(W0_15)+[0]*48
    print(len(W))

    # ekspansi dari ronde 16 hingga 63 memanfaatkan fungsi sigma kecil
    for i in range(16,64):
        W[i] = (W[i-16] + sigma0(W[i-15]) + W[i-7] + sigma1(W[i-2]) ) & 0xFFFFFFFF

    return W

def compress_block(W, K, H_awal):
    # Menginisialisasi 8 register kerja (working variables) dengan nilai hash blok sebelumnya
    a, b, c, d, e, f, g, h = H_awal

    for i in range(64):
        # Hitung Nilai Tambahan T1 dan T2
        T1 = (h + Sigma1(e) + Ch(e, f, g) + K[i] + W[i]) & 0xFFFFFFFF
        T2 = (Sigma0(a) + Maj(a, b, c)) & 0xFFFFFFFF

        # Pergeseran nilai register (register diturunkan ke bawah, kecuali 'e' dan 'a')
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
