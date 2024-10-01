## JFun

Description: As we come to an end, you've been yet given another file to reverse engineer. This time around, we provided the source code for the application. Can you help me figure the secret?<br>
Author: h4ckyou<br>
Solves: 6

---
Solution
---

We are given the Java source code
![image](https://github.com/user-attachments/assets/6b7516f1-e232-4190-bdf0-4c5fe369c0f1)

Below the code are some comments
![image](https://github.com/user-attachments/assets/a01b969f-ef4b-4d5f-8262-98c54bcd3460)

From the code we can see that it stores some string in variable `text` and then for every character in the string it generates the SHA256 hash and prints it's value

Since we are given some hash values (the commented ones), we can conclude that our goal is to recover plaintext from the given hashes

We can try crack the hashes which should work but I prefer scripting my solution so I made a solve which involves getting a mapping of all printable characters with it's corresponding hash then lookup the provided hash character value

```python
import hashlib
import string

charset = string.printable
mapping = {}

for val in charset:
    hash = hashlib.sha256(val.encode()).hexdigest()
    mapping[hash] = val

hashes = [
   "2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6",
   "043a718774c572bd8a25adbeb1bfcd5c0256ae11cecf9f9c3f925d0e52beaf89",
   "3f79bb7b435b05321651daefd374cdc681dc06faa65e374e38337b88ca046dea",
   "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb",
   "1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9",
   "3973e022e93220f9212c18d0d0c543ae7c309e46640da93a4a0314de999f5112",
   "2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6",
   "e3b98a4da31a127d4bde6e43033f66ba274cab0eb7eb1c70ec41402bf6273dd8",
   "252f10c83610ebca1a059c0bae8255eba2f95be4d1d7bcfa89d7248a82d9f111",
   "021fb596db81e6d02bf3d2586ee3981fe519f275c0ac9ca76bbcf2ebb4097d96",
   "aaa9402664f1a41f40ebbc52c9993eb66aeb366602958fdfaa283b71e64db123",
   "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9",
   "148de9c5a7a44d19e56cd9ae1a554bf67847afb0c58f6e12fa29ac7ddfca9940",
   "4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce",
   "d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde",
   "a1fce4363854ff888cff4b8e7875d600c2682390412a8cf79b37d0b11148b0fa",
   "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9",
   "0bfe935e70c321c7ca3afc75ce0d0ca2f98b5422e008bb31c00c6d7f1f1c0ad6",
   "d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde",
   "aaa9402664f1a41f40ebbc52c9993eb66aeb366602958fdfaa283b71e64db123",
   "4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a",
   "18ac3e7343f016890c510e93f935261169d9e3f565436429830faf0934f4f8e4",
   "d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde",
   "252f10c83610ebca1a059c0bae8255eba2f95be4d1d7bcfa89d7248a82d9f111",
   "0bfe935e70c321c7ca3afc75ce0d0ca2f98b5422e008bb31c00c6d7f1f1c0ad6",
   "1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9",
   "1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9",
   "1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9",
   "1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9",
   "1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9",
   "1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9",
   "d10b36aa74a59bcf4a88185837f658afaf3646eff2bb16c3928d0e9335e945d2",
   "d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35",
   "4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a"
]

flag = ""

for hash in hashes:
    flag += mapping[hash]

print(flag)
```

Running it gives the flag
![image](https://github.com/user-attachments/assets/8f22aa4e-7f54-46a1-ad1e-5ca70a85e032)

```
Flag: csean-ctf{h0p3_y0u_h4d_funnnnnn}24
```
