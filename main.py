import src.constants as const
import src.sha256 as sha
import os

K = const.K
H = const.H

while True:
    msg_initial = input("masukkan teks : ")

    pad_msg = sha.pad_message(msg_initial)

    W0_15 = []
    for i in range(0, len(pad_msg), 4):
        word = int.from_bytes(pad_msg[i:i+4], byteorder='big')
        W0_15.append(word)

    expand_msg = sha.expand_msg(W0_15)
    result = sha.compress_block(expand_msg,K,H)

    print("HASH AKHIR")
    digest=''.join(f'{x:08x}' for x in result)
    print(digest)

    print()
    print()

    confirm = input("press CTRL + C for break or press enter for continue!")
    if(confirm == ""):
        os.system('clear')
    else:
        break