## Just Rev

Description: Show me your skills<br>
Author: h4ckyou<br>
Solves: 0

---
Solution
---

We are given a binary and checking the file type & properties shows this
![image](https://github.com/user-attachments/assets/9e390aa1-e97c-4b08-a1dd-1c7d5687ab0b)

So this is a 64bit executable which is dynamically linked and stripped

Running it to get an overview of what it does shows this
![image](https://github.com/user-attachments/assets/704a1d96-177e-439a-ae59-ec6865c7c690)

From this we can tell that we need to provide the right flag and if we get it we should get a message that isn't "Wrong"

Using IDA we can decompile the binary and here's the main function
![image](https://github.com/user-attachments/assets/719e6a79-87bb-44ab-8fb4-b16e66e8325f)

Uhhh it's a C++ binary 🤮

First:
- It prints out some words, then it receives our input using `std::cin` and stores it in variable `s`
- It then gets the length of the input string and stores it in variable `v10`
- Then it calls three functions passing the variable `s & v10` as argument
- It then iterates through the length variable `s` and compares `s[i]` against a dword value stored at `dword_4040[i]`
- If the comparism returns False it returns and print the error message "Wrong." else it prints the success message "Correct!"

With that we get the general idea of the main function, so here's my renamed code

```c
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  __int64 v3; // rax
  __int64 v4; // rdx
  __int64 v5; // rdx
  __int64 v6; // rax
  __int64 v8; // rax
  char buf[72]; // [rsp+0h] [rbp-50h] BYREF
  unsigned int len; // [rsp+48h] [rbp-8h]
  int i; // [rsp+4Ch] [rbp-4h]

  v3 = std::operator<<<std::char_traits<char>>(
         &std::cout,
         "Reversing is pain but can you find your way around this?",
         a3);
  std::ostream::operator<<(v3, &std::endl<char,std::char_traits<char>>);
  std::operator<<<std::char_traits<char>>(&std::cout, "Flag: ", v4);
  std::operator>><char,std::char_traits<char>>(&std::cin, buf);
  len = strlen(buf);
  sub_1169(buf, len);
  sub_128B(buf, len);
  sub_134A(buf, len);
  for ( i = 0; i < len; ++i )
  {
    v5 = dword_4040[i];
    if ( buf[i] != v5 )
    {
      v6 = std::operator<<<std::char_traits<char>>(&std::cout, "Wrong.", v5);
      std::ostream::operator<<(v6, &std::endl<char,std::char_traits<char>>);
      return 0LL;
    }
  }
  v8 = std::operator<<<std::char_traits<char>>(&std::cout, "Correct!", v5);
  std::ostream::operator<<(v8, &std::endl<char,std::char_traits<char>>);
  return 0LL;
}
```

Now we need to figure out exactly what the three function does to our input:
- sub_1169(buf, len);
- sub_128B(buf, len);
- sub_134A(buf, len);


For the first function here's the decompilation
![image](https://github.com/user-attachments/assets/19c52fa6-ad03-4b1c-8658-5bb6efe4f1f2)

This might look kinda hard to assimilate but from renaming variable names and data types i got this

```c
__int64 __fastcall sub_1169(char *buf, int len)
{
  void *v2; // rsp
  __int64 result; // rax
  __int64 buf_len; // [rsp+0h] [rbp-30h] BYREF
  char *tmp; // [rsp+8h] [rbp-28h]
  char v6; // [rsp+16h] [rbp-1Ah]
  char v7; // [rsp+17h] [rbp-19h]
  char *v8; // [rsp+18h] [rbp-18h]
  __int64 v9; // [rsp+20h] [rbp-10h]
  int j; // [rsp+28h] [rbp-8h]
  int i; // [rsp+2Ch] [rbp-4h]

  tmp = buf;
  HIDWORD(buf_len) = len;
  v9 = len - 1LL;
  v2 = alloca(16 * ((len + 15LL) / 0x10uLL));
  v8 = &buf_len;
  for ( i = 0; i < HIDWORD(buf_len) - 1; i += 2 )
  {
    v7 = tmp[i];
    v6 = tmp[i + 1];
    v8[i] = v6;
    v8[i + 1] = v7;
  }
  for ( j = 0; ; ++j )
  {
    result = j;
    if ( j >= SHIDWORD(buf_len) )
      break;
    tmp[j] = v8[j];
  }
  return result;
}
```

Now that looks much better
- It defines the tmp variable to be a pointer to the buf variable
- It iterates through the length of the buf while incrementing the iterate by 2
- It stores the current buf value into variable `v7` and then the next buf value into variable `v6`
- Then it stores `v6` into `v8[i]` and `v7` into `v8[i + 1]`

Then after it does this swap it would replace the values of `buf` to `v8`

The conclusion we can draw from what this function does is that it performs a swap of adjacent bytes within the buffer

Now let's see example:

If we input:
- abcd, the function should modify our buf value to: badc

We can confirm by setting a breakpoint before the call to the function and seeing the modified value after this function is called
![image](https://github.com/user-attachments/assets/29fc57ab-e685-4d30-a5b8-dcd335717e96)
![image](https://github.com/user-attachments/assets/53da2231-f18c-49aa-9b33-917c0b9ca849)
![image](https://github.com/user-attachments/assets/e870ef4f-2a19-483f-8681-7b336b97d492)

Now that we have understand what this function does, we just rename it and move to the next one

For the second function here's the decompilation
![image](https://github.com/user-attachments/assets/552243e6-a561-4694-842a-adb27033b2b5)

After renaming and setting the right data type i got this

```c
__int64 __fastcall sub_128B(char *buf, int len)
{
  void *v2; // rsp
  __int64 result; // rax
  __int64 n; // [rsp+0h] [rbp-30h] BYREF
  char *tmp; // [rsp+8h] [rbp-28h]
  char *v8; // [rsp+18h] [rbp-18h]
  __int64 v7; // [rsp+20h] [rbp-10h]
  int j; // [rsp+28h] [rbp-8h]
  int i; // [rsp+2Ch] [rbp-4h]

  tmp = buf;
  HIDWORD(n) = len;
  v7 = len - 1LL;
  v2 = alloca(16 * ((len + 15LL) / 0x10uLL));
  v8 = &n;
  for ( i = 0; i < SHIDWORD(n); ++i )
    v8[i] = tmp[HIDWORD(n) - 1 - i];
  for ( j = 0; ; ++j )
  {
    result = j;
    if ( j >= SHIDWORD(n) )
      break;
    tmp[j] = v8[j];
  }
  return result;
}
```

Now what does this do?
- Again it creates a tmp variable which is a pointer to the buf passed as the first parameter
- It then iterates through the length of buf and sets variable `v8[i]` to `tmp[n - 1 - i]`
- Then it iterates again through the length of buf and sets `tmp[j]` to `v8[j]`

From this we can conclude that this function reverses the content stored in the buf because that's just a basic implementation of how you can reverse a string

Now let's see example:

If we input:
- abcd, the function should modify our buf value to: dcba

Let's check this out

I'll debug the function using badc as the flag value because when the first function is called, it should swap the adjacent bytes of badc, resulting in abcd hence making it match our expected example value
![image](https://github.com/user-attachments/assets/df79feee-ea70-4776-9adb-4f7556492145)
![image](https://github.com/user-attachments/assets/81e532b8-80a5-4ed0-a6d4-f593b5b017b5)
![image](https://github.com/user-attachments/assets/82995780-a654-4cd9-9f05-f0fecc7a98b0)

Cool, we confirmed what this function does now we just rename it and move on

For the last function here's the decompilation
![image](https://github.com/user-attachments/assets/dd98dabf-3f4c-48e2-aa20-f7e8e804d025)

Yet again I renamed variable names and set the variables to the right data type

```c
__int64 __fastcall sub_134A(char *buf, int len)
{
  void *v2; // rsp
  char v3; // al
  char v4; // al
  __int64 n; // [rsp+0h] [rbp-50h] BYREF
  char *tmp; // [rsp+8h] [rbp-48h]
  int v8; // [rsp+18h] [rbp-38h]
  int v9; // [rsp+1Ch] [rbp-34h]
  char *v10; // [rsp+20h] [rbp-30h]
  __int64 v11; // [rsp+28h] [rbp-28h]
  int j; // [rsp+34h] [rbp-1Ch]
  int i; // [rsp+38h] [rbp-18h]
  unsigned int var; // [rsp+3Ch] [rbp-14h]

  tmp = buf;
  HIDWORD(n) = len;
  v11 = len - 1LL;
  v2 = alloca(16 * ((len + 15LL) / 0x10uLL));
  v10 = &n;
  var = 0;
  for ( i = 0; i < SHIDWORD(n); ++i )
  {
    if ( (var & 1) != 0 )
    {
      v4 = tmp[i];
      v9 = (-99 - v4);
      v10[i] = -99 - v4;
    }
    else
    {
      v3 = sub_1255((tmp[i] ^ 0x40), 4LL);
      v8 = (-3 - v3);
      v10[i] = -3 - v3;
    }
    ++var;
  }
  for ( j = 0; j < SHIDWORD(n); ++j )
    tmp[j] = v10[j];
  return var;
}
```

- It creates a tmp variable which is a pointer to the buf passed as the first parameter
- Iterates through the length of the buf and based on if variable `var` is even or odd, it modifies the value of the buf at that current index then increments `var`
- If `var` is an even number then it calls function `sub_1255` passing `tmp[i] ^ 0x40` as the first parameter and `4` as the second parameter then it does some subtraction thingy else it just does some subtraction thingy on `tmp[i]`

From this I can't really tell what this is but we know for sure this is mangling our input so we rename it function `mangle`

Now let us check what function `sub_1255` does
![image](https://github.com/user-attachments/assets/4e6a9376-18ca-4c80-8eb5-a908cd326dbd)

```c
__int64 __fastcall sub_1255(int a1, char a2)
{
  return ((a1 << a2) | (a1 >> (8 - a2)));
}
```

This just rotates the bits of `a1` to the left by `a2` positions. So we know this function is `rol`

Now we know that the main function should look like this
![image](https://github.com/user-attachments/assets/2933103b-8dd2-4bc3-875c-d8aab7e0500c)

Where the encryption is as follows:
- swap adjacent bytes
- reverses the content
- mangles the bytes

Since our input is going to be passed into those following functions and compared against a hardcoded value, we need to reverse the operations of each function such that when we run it against the hardcoded value we would get the expected plaintext

To do that we move backwards:
- demangle bytes
- reverses the content
- swap adjacent bytes


For the last two functions we don't need to make additional changes—reusing these functions accomplishes the same effect as reversing the data

The only function of concern is the mangling of data

To reverse the operation of rotate left we just apply rotate right and this is it's implementation:

```c
uint8 ror(uint8 a1, uint8 a2) {
  return ((a1 >> a2) | (a1 << (8 - a2)));
}
```

Or in python:

```python
def ror(value, shift):
    return (value >> shift) | (value << (8 - shift)) & 0xff
```

Now how do we reverse the operation done based on if `var` is even or odd in the `mangle` function

From looking at it, it looks not too difficult to reverse

For example when `var` is odd, this is the operation done

```
v4 = tmp[i];
v9 = (-99 - v4);
v10[i] = -99 - v4;
```

We can rewrite this as:

```
x = -99 - tmp[i]
```

And basically we have `x` so we can recover `tmp[i]`:

```
x = -99 - tmp[i]
x + 99 = -tmp[i]
-tmp[i] = x + 99
tmp[i] = -(x + 99)
```

You can also do same for when `var` is even

```
v3 = rol((tmp[i] ^ 0x40), 4LL);
v8 = (-3 - v3);
v10[i] = -3 - v3;
```

Rewrite as:

```
x = -3 - rol((tmp[i] ^ 0x40), 4LL)
```

Recover `tmp[i]` because we know `x` and the operation is reversible

```
-3 - rol((tmp[i] ^ 0x40), 4LL) = x
rol((tmp[i] ^ 0x40), 4LL) = 3 - x
tmp[i] ^ 0x40 = ror((3 - x), 4)
tmp[i] = ror((-3 - x), 4) ^ 0x40
tmp[i] = ror(-(3 + x), 4) ^ 0x40
```

With that said the reversed operation for is_even & is_odd are:
- pt = ror(-(3 + enc), 4) ^ 0x40
- pt = -(x + 99)


Wrapping it up, we need to extract the hardcoded value we are comparing our transformed input to
![image](https://github.com/user-attachments/assets/44cb2277-ca9c-4c3e-a92c-ec7e044d1429)

Click on `Hex View-1`
![image](https://github.com/user-attachments/assets/bdb4ca34-e276-4b67-856f-28e8296852d6)

Now we just select the values and extract it `ALT + E`
![image](https://github.com/user-attachments/assets/89fc99cb-3a52-4520-aa22-b7ca2ac457e2)

Here's the final solve [script](https://github.com/h4ckyou/CSEAN24/blob/main/rev/just%20rev/solution/solve.py)

```python
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
```

Running it gives the flag:
![image](https://github.com/user-attachments/assets/0a791527-a0cf-4d59-a5c3-06793cf470ae)

```
Flag: csean-ctf{y0u_c4n_sw4p_r3v3rs3_m4ngl4_and_r0t4t3_4_byt3}24
```
