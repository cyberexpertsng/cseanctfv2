## DeeStrucTor

Description: I was given this weird file but it does not seem to do anything, can you help me figure it out?<br>
Author: h4ckyou<br>
Solves: 3

---
Solution
---

We are given a binary `chall` and from checking the file properties we get this
![image](https://github.com/user-attachments/assets/b8cf86f9-a503-4ff1-8991-06c69e1f9088)

This is a 64bits executable which is statically linked and stripped

Running it we see it does nothing?
![image](https://github.com/user-attachments/assets/1fb73a9a-179e-4623-b0d5-dc0472e42f47)

There are two ways you can go about this:
- Just "smartly" checking the list of available functions in IDA
- Researching about "destructors in C"

I'll start from the first one. Loading it into IDA we should get this
![image](https://github.com/user-attachments/assets/0156a070-1823-44d5-ac0b-ddd8137cec01)

Since the binary is stripped, the function names are not available. Additionally, because it is statically linked, the binary size is significantly larger due to all the necessary functions being embedded directly within the binary.

Now one easy way to get reference to the main function is by searching for the strings being outputted during runtime?

For example:
- View -> Open Subviews -> Strings

![image](https://github.com/user-attachments/assets/005b4e0e-31cb-489a-93f1-1557bd5ac117)

Now we look for the string "This program does nothing." because that was printed to the screen when we ran the binary
![image](https://github.com/user-attachments/assets/64a3bf87-6b3d-4980-9a5b-954d839cd7ad)

You can just `CTRL + F`

Ok our string is located in the `.rodata` section and when we double click it we should get this
![image](https://github.com/user-attachments/assets/80ebbf78-4460-4707-bdcb-679149e51ded)

Now we check for `Cross Reference` to that string and doing that we should get this
![image](https://github.com/user-attachments/assets/d9e1841c-e3d6-489b-a95c-e773d167f33c)

We can see that function `sub_401805+4` executes an instruction which makes use of the string in that location

Now we just double click on that 🙂
![image](https://github.com/user-attachments/assets/a884bbba-e094-4ea6-81ab-f9b4d6324edb)

This now, is the main function

Press the almighty `F5` key to get the pseudocode (C like decompilation)
![image](https://github.com/user-attachments/assets/ae0c5c3d-135f-41cc-99e2-e5c770966184)

And again because this is stripped we can't tell which function is which

But you can intuitively tell that `sub_404690` is functions `puts()`

Now we just rename the functions!
![image](https://github.com/user-attachments/assets/e4a20162-e7ef-4498-9fb8-90440897f2c3)

That looks more like it!

Now back to the method as to how we solve this!

This program literally does nothing so what comes in mind is:
- Is there a function somewhere that does something interesting?

And due to this we can start looking through other functions and now the reason why we needed to rename this to the main function is to avoid looking through the whole functions available because "that my friend" is pain

![image](https://github.com/user-attachments/assets/3d60d05a-c383-4242-9a0d-20fe08662a30)

Just start clicking the other functions below main and boom the first one `sub_40181F` yields something interesting
![image](https://github.com/user-attachments/assets/ef13ae26-c008-4c17-880f-10d442bf27d3)

You can't view it's pseudocode because this is written in pure assembly and doesn't really do things like storing a value in a variable etc.

Here's the disassembly:

```asm
push rbp
mov rbp, rsp
xor r8, r8
mov r8, 0x637466
xor rdi, rdi
mov rdi, 0x63101107
xor rdi, r8
xor rdi, rdi
mov rdi, 0x6e4e1712
xor rdi, r8
xor rdi, rdi
mov rdi, 0x66180757
xor rdi, r8
xor rdi, rdi
mov rdi, 0x6d131855
xor rdi, r8
xor rdi, rdi
mov rdi, 0x5f1b4414
xor rdi, r8
xor rdi, rdi
mov rdi, 0x5f061a05
xor rdi, r8
xor rdi, rdi
mov rdi, 0x721a0412
xor rdi, r8
xor rdi, rdi
mov rdi, 0x31531a39
xor rdi, r8
xor rdi, rdi
mov rdi, 0x680a1002
xor rdi, r8
xor rdi, rdi
mov rdi, 0x330d551b
xor rdi, r8
nop
pop rbp
retn
```

Ok so first it setups a new stack frame (standard stuffs) then it stores into the `r8` register the value `0x637466` and then it keeps moving some values into the `rdi` register and xors it with the `r8` register

From this we can see that it basically does xor encryption with some values which keeps getting stored in the `rdi` register with a constant key which is in the `r8` register

Now to solve we can just rewrite this in python 

Here's my solve script

```python
key = 0x637466

chunks = [
    0x63101107, 0x6e4e1712, 0x66180757, 0x6d131855,
    0x5f1b4414, 0x5f061a05, 0x721a0412, 0x31531a39,
    0x680a1002, 0x330d551b
]

flag = b""

for i in range(len(chunks)):
    chunk = chunks[i]
    xored = chunk ^ key
    flag += xored.to_bytes((xored.bit_length() + 7) // 8)


print(flag)
```

Running it gives the flag
![image](https://github.com/user-attachments/assets/fff50e48-0a40-4cb6-89a5-341378949841)

```
Flag: csean-ctf{s1mpl3_x0r_encrypt10n_hidd3n!}
```

Now this way is all good but that's not the purpose as to why i created this

If you take your time to research about Destructors in C you should basically get the general idea that it causes the function to be called automatically after main () has completed or exit () has been called

And the location of funtions which are called as destructors is the `.fini_array` section

You can check [this](https://gist.github.com/x0nu11byt3/bcb35c3de461e5fb66173071a2379779#sections) out

So the goal would have been to check the `.fini_array` section to retrieve the function whch would be called as a destructor, then just repeat the same process of reading the assembly code above and writing your solve
