def ror(value, shift):
    return (value >> shift) | (value << (8 - shift)) & 0xff

def swap(buf):
    tmp_buf = [0]*len(buf)

    for i in range(0, len(buf)-1, 2):
        tmp1 = buf[i]
        tmp2 = buf[i+1]
        tmp_buf[i] = tmp2
        tmp_buf[i+1] = tmp1

    return tmp_buf

def reverse(buf, n):
    tmp_buf = [0]*n

    for i in range(n):
        tmp_buf[i] = buf[n-1-i]

    return tmp_buf

def demangle(buf, n):
    tmp_buf = [0]*n

    j = 0
    for i in range(n):
        val = buf[i]
        if j & 1 == 0:
            r = (ror(-(3 + val) & 0xff, 4) ^ 0x40) & 0xff
            tmp_buf[i] = chr(r)
        else:
            r = -(val + 99) & 0xff
            tmp_buf[i] = chr(r)

        j += 1
    
    return tmp_buf


data = bytes.fromhex("C6 00 00 00 20 00 00 00 6A 00 00 00 29 00 00 00 0C 00 00 00 3B 00 00 00 0C 00 00 00 69 00 00 00 BA 00 00 00 6A 00 00 00 BA 00 00 00 69 00 00 00 DA 00 00 00 6D 00 00 00 BB 00 00 00 3E 00 00 00 EB 00 00 00 2F 00 00 00 B6 00 00 00 3E 00 00 00 8B 00 00 00 31 00 00 00 B6 00 00 00 2F 00 00 00 0C 00 00 00 30 00 00 00 CA 00 00 00 6A 00 00 00 C6 00 00 00 2B 00 00 00 C6 00 00 00 27 00 00 00 0C 00 00 00 2B 00 00 00 B6 00 00 00 2D 00 00 00 CA 00 00 00 26 00 00 00 1B 00 00 00 3E 00 00 00 CB 00 00 00 69 00 00 00 AA 00 00 00 3E 00 00 00 6A 00 00 00 6D 00 00 00 9B 00 00 00 22 00 00 00 CB 00 00 00 29 00 00 00 1B 00 00 00 70 00 00 00 AB 00 00 00 3C 00 00 00 CB 00 00 00 2A 00 00 00 00 00 00 00")
enc = data.replace(b"\x00", b"")
n = len(enc)
buf = demangle(enc, n)

buf = reverse(buf, n)
buf = swap(buf)[:-1]

flag = "".join(buf) + "}"
print(flag)