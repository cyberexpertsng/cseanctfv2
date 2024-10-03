## Ret2Win V2

Description: The last one was so simple so I decided to bring in something better but trust me, it’s still ret2win!
Author: h4ckyou<br>
Solves: 0

---
Solution
---

We are given a zipfile which when extracted gives a binary

Checking the file type and protections enabled on it shows this
![image](https://github.com/user-attachments/assets/2db95a41-2813-479c-b7d2-43d72b4e6996)

So we are working with a 64 bits executable which is dynamically linked and not stripped, from the protections enabled we see that there's Stack Canary present and NX is enabled

Let us run it to get an overview of what it does
![image](https://github.com/user-attachments/assets/779cadb5-7269-4277-b93b-9e4adf1c3650)

So the program asks if we have any feedback, if we do not it exits else it receives 3 feedbacks from us

Interesting! in order to find the vulnerabiltiy we need to decompile the binary and my choice here is IDA

Here's the main function
![image](https://github.com/user-attachments/assets/82d757f3-4df4-4069-ae0d-b29e47263bfe)

It just calls `init()` and the `challenge()` function

The first function just disables buffering on stdin, stdout & stderr
![image](https://github.com/user-attachments/assets/605b401d-fa23-4412-8305-8c5a11aa16e5)

That's just standard pwn stuff

The next function does this
![image](https://github.com/user-attachments/assets/9c15803f-2369-4703-97c3-a5c8858e47c3)

```c
__int64 challenge()
{
  char s1[5]; // [rsp+3h] [rbp-Dh] BYREF
  unsigned __int64 v2; // [rsp+8h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  puts("Welcome to part two of the first pwn challenge");
  puts("What's a CTF without a beginners's pwn :)");
  puts("Would you like to give any feedback?");
  __isoc99_scanf("%4s", s1);
  getchar();
  if ( !strncmp(s1, "yes", 3uLL) )
  {
    feedback();
    return 0LL;
  }
  else
  {
    puts("Goodbye");
    return 1LL;
  }
}
```

So we can see that if our input is `yes` it would call the `feeback()` function so that means our bug is going to be there

Here's the decompilation of the function:
![image](https://github.com/user-attachments/assets/d7a66526-44bf-472a-82bc-3e3eef36e544)

```c
__int64 feedback()
{
  void *buf; // [rsp+8h] [rbp-38h] BYREF
  char v2[40]; // [rsp+10h] [rbp-30h] BYREF
  unsigned __int64 v3; // [rsp+38h] [rbp-8h]

  v3 = __readfsqword(0x28u);
  memset(v2, 0, sizeof(v2));
  buf = 0LL;
  puts("What's your first complaint.");
  read(0, &buf, 8uLL);
  puts("What's your second complaint..");
  read(0, buf, 8uLL);
  puts("What's your final complaint...");
  read(0, v2, 0x60uLL);
  puts("Ok thanks for your opinion");
  return 0LL;
}
```













