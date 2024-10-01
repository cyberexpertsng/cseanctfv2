## Guess The Flag

Description: This is me totally not trolling
Author: h4ckyou
Solves: 4

---
Solution
---

We are given a text file and checking the content shows this
![image](https://github.com/user-attachments/assets/d66217bd-0252-4f6e-b71f-583260abdf34)

Looking at it, we can see it's a 2D array that has so many sublists

One distinction between every elements in the sublists is that one is of type(str()) and the other of type(int())

The element of type(str()) are all hex values 

Starting from the bottom we can see this:

```
[['3a', 5], ['2f', 7], ['2f', 6], ['70', 3], ['73', 4], ['74', 2], ['68', 0], ['74', 1]]
```

If we start decoding from when `sublists[1]` is `0` we get this:

```
0 -> h
1 -> t
2 -> t
3 -> p
4 -> s
5 -> :
6 -> /
7 -> /
```

From this we can see that the decoded value is `https://`

With this, we can conclude that the 2D array is made up of sublists, and each sublist contains:
- A hexadecimal string that, when converted to a character, represents part of a message.
- An index that determines where that character should be placed in the final message.


But if you notice the whole structure you can see that the indices are basically shuffled around, so we need to parse it well

To do that we just need to sort the sublists by the second element (index) then we convert the hex strings to characters and arrange them in the correct order

Here's my solution:

```python
import ast

output = open("output.txt", "r").read()
data = ast.literal_eval(output) 
mapping = {}

for i in data:
    mapping[i[1]] = chr(int(i[0], 16))

charset = sorted(mapping)

decoded = ""

for i in charset:
    decoded += mapping[i]

print(decoded)
```

Running that, we get a cyberchef link
![image](https://github.com/user-attachments/assets/5067610d-4e03-4ae1-aba9-dfbb9268c606)

Checking it shows this
![image](https://github.com/user-attachments/assets/c1e22261-5d6b-403d-8558-1639ff39beb3)

Cyberchef magic suggests to auto decode so we just let it do it's thing

But then, it gets stucked here
![image](https://github.com/user-attachments/assets/aab6781c-6d13-4607-8e8d-90d31385cd71)

```
*b}=*(cE*b#>6b4_}'h_2st`)a5`|K&`6'gH4=hB5%'_)b"H|uh=6?_J}pll
```

What is that? Well you can always try use [dcodefr](https://www.dcode.fr/cipher-identifier) to identify stuffs like this
![image](https://github.com/user-attachments/assets/51df86f2-df1b-4d10-ba8e-7397ff4c9159)

It suggests `Rot 47`

Now we use Cyberchef to continue it's magic
![image](https://github.com/user-attachments/assets/8abdd83d-f698-4688-b1d5-7dd199067a1a)

And we get the flag!

```
Flag: csean-ctf{w45_th15_gu355y_0r_ju5t_t00_ez}24
```
