from pwn import remote, context
import random
import string
import time

def substitute(s1, sbox, key):
    sbox = sbox
    key = key
    s = []

    for value in s1:
        r = key
        while value:
            r = sbox[r]
            value -= 1
        s.append(r)

    return bytes(s).hex()


host, port = "0.cloud.chals.io", 31202
context.log_level = "debug"

io = remote(host, port)

io.recvuntil(b">")
io.sendline(b"1")
seed = int(time.time())
io.recvuntil(b"flag: ")
enc = io.recvline().strip().decode()
chunks = []

for i in range(0, len(enc), 2):
    chunks.append(enc[i:i+2])

for trial in range(seed-0x100, seed+0x100):
    random.seed(trial)
    sbox = list(range(256))
    random.shuffle(sbox)

    charset = string.printable
    mapping = {}

    for key in range(0xff):
        for value in charset:
            r = substitute(value.encode(), sbox, key)
            mapping[r] = value

        flag = ""
        try:
            for chunk in chunks:
                flag += mapping[chunk] 
        except KeyError:
            pass

        if "csean-ctf" in flag:
            print(flag)
            break


io.interactive()
