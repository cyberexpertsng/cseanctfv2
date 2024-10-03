## My Box

Description: Get me free from this box<br>
Author: h4ckyou<br>
Solves: 2 


## CSEAN CTF 2024

  - Challenge: My Box
  - Solver: Nano (Pwn-Stars)


![image](https://github.com/user-attachments/assets/b1363983-5010-45ea-966c-ee1a6a6af935)

We are given a zip file which contains the code running on the remote instance
![image](https://github.com/user-attachments/assets/db7bf13c-0059-41b3-8019-c5cbaf0bdbad)
![image](https://github.com/user-attachments/assets/6438ec4e-aea4-46e6-9d4b-2f58eac67e2f)

From the source code i'll start from the main function
![image](https://github.com/user-attachments/assets/ebdc8fb1-ebf3-44c1-9bd0-26478993393d)

We have three options to choose from:
- Generate
- Confirm
- Quit

The third function basically exits the process

![image](https://github.com/user-attachments/assets/bbf8ad00-a20c-4025-97e1-3e7426f48c42)

The second function basically checks if the input received matches the value stored in `e_flag`
![image](https://github.com/user-attachments/assets/997bb0f6-c124-4be7-b466-38caeb4e340b)

That means the main stuff is the "Generate" function
![image](https://github.com/user-attachments/assets/4ac2c877-dae3-4823-91aa-1104385de0a1)

```python
#!/usr/bin/env python3
import random
import time

flag = b"csean-ctf{[redacted]}24"
e_flag = b""

def generate():
    global e_flag

    key = random.randint(0, 0x100)
    ct = int(time.time())
    random.seed(ct)
    sbox = list(range(256))
    random.shuffle(sbox)

    s = []

    for val in flag:
        r = key
        while val:
            r = sbox[r]
            val -= 1
        s.append(r)

    e_flag = bytes(s)

    print(f'Encrypted flag: {e_flag.hex()}')
```

From looking at this we can tell that this function encrypts the flag using a randomly generated key and an S-box

S-box means substitution box

The Sbox is a list of integers from 0 to 255 that is randomly shuffled based on a seed generated from the current time (ct) and the key is a random integer between 0 and 256

To be honest i don't really understand what it does exactly but basically it will do multiple substitution based on the shuffled sbox value and the number of substitution it does is based on the key generated

The way i solved this is by generating a mapping of the ascii values and it's substituted value

That works because random is seeded with the current time and that means we can also predict what the shuffled list will be and since the key is just withtin a byte range we can brute force it

Also if you notice the `confirm` choice actually gives us the current time so we can leverage that to brute force the seed (which is the time)




















