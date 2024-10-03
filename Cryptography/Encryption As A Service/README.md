## Encryption As A Service

Description: We provide a new method of encryption and we use it as our service and yes it’s totally free<br>
Author: h4ckyou<br>
Solves: 6

we were given a challenge.py script

```python

flag = b"" # hmm, prolly interesting?
secret = b"" # for now we make use of a byte as the secret, totally gonna be random in the future

to_bytes = lambda h: bytes.fromhex(h)
to_hex = lambda h: h.hex()


def getFlag():
    return encrypt(to_hex(flag.hex()), secret)


def encrypt(s1, s2):
    m1 = to_bytes(s1)
    m2 = to_bytes(s2)
    r = bytes([m1[i] ^ m2[i % len(m2)] for i in range(len(m1))])
    return to_hex(r) 


def showFlag():
    fleg = to_hex(flag)
    msg = to_bytes(fleg)
    enc = bytes([msg[i] ^ ((ord(secret)+i) % 256) for i in range(len(msg))])
    print(f"Here's the encrypted flag: {to_hex(enc)}")
    return


def showSecret():
    print("lmao, not that easy!")
    return 


def doService():
    try:
        msg = input("Enter plaintext: ")
        key = input("Enter key: ")
        s1 = to_hex(msg.encode())
        s2 = to_hex(key.encode())
        encrypted = encrypt(s1, s2)
        print(f"Your encrypted message: {encrypted}")
    except Exception:
        print("some error occurred!")
    return


def quit():
    exit("Thanks for choosing our service!")


def menu():
    print("1. Make use of our encryption")
    print("2. Get the encrypted flag")
    print("3. Get the secret")
    print("4. Exit")
    try:
        choice = int(input("> "))
        return choice
    except Exception:
        print("dwag, this is crypto")
        return


def main():
    while True:
        choice = menu()
        if choice == 1:
            doService()
        elif choice == 2:
            showFlag()
        elif choice == 3:
            showSecret()
        elif choice == 4:
            quit()


if __name__ == '__main__':
    main()
```

Global Variables:

```flag```: A placeholder for the flag that will eventually be encrypted and revealed.
```secret```: A secret key (byte) that will be used in the encryption process. Right now, it's just an empty byte string, but it will eventually be randomized.
Functions:

```to_bytes(h)```: Converts a hexadecimal string h into a byte sequence.
```to_hex(h)```: Converts a byte sequence h into its hexadecimal representation.
```getFlag()``` Function:

This function encrypts the hexadecimal version of the flag ```(flag.hex())``` using the secret.
The encrypt function is called, which XORs the two inputs ```(s1 and s2)```, both of which are hexadecimal strings converted to bytes.

```encrypt(s1, s2)``` Function:

Takes two hexadecimal strings (```s1 and s2```), converts them into byte arrays (```m1 and m2```).
The function XORs each byte of m1 with a corresponding byte in m2. If m2 is shorter than m1, it wraps around using ```i % len(m2)```.
The result is converted back to hex and returned.

```showFlag()``` Function:

Displays the encrypted version of the flag.
It XORs each byte of the flag with a value derived from the secret key and the byte's position ```((ord(secret) + i) % 256)```, then prints the encrypted result in hexadecimal form.



```doService()``` Function:

This is an encryption service where the user inputs a plaintext message ```(msg)``` and a key ```(key)```.
Both msg and key are converted into hexadecimal strings and encrypted using the same ```encrypt()``` function described earlier.
The result is printed as the encrypted message.


so now we write the solve script

```python
def to_bytes(h):
    return bytes.fromhex(h)

def to_hex(b):
    return b.hex()

def decrypt(enc, secret):
    """Decrypts the given encrypted flag with the provided secret."""
    msg = to_bytes(enc)
    return bytes([msg[i] ^ ((secret + i) % 256) for i in range(len(msg))])

# The encrypted flag (from showFlag output)
encrypted_flag_hex = "4958494c4002534554484c05446840094864440d4c6071321d2074750a3a7a7d"

# Flag prefix
flag_prefix = "csean-ctf{"

# Try every possible byte value for the secret
for secret in range(256):
    decrypted_flag = decrypt(encrypted_flag_hex, secret).decode(errors='ignore')
    
    # Check if the decrypted flag starts with the known prefix
    if decrypted_flag.startswith(flag_prefix):
        print(f"Found secret byte: {secret} -> Decrypted flag: {decrypted_flag}")
```

the hex being the value we got from the server
