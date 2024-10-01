## ChatGPT

Description: Your mission should you choose to accept
it, is to extract the secret from the communication between I and an AI model

author: h4ckyou

[source](https://chatgpt.com/share/66f4a973-ed08-800a-9950-2ce1d86b6ff4)

----
Solution
---

Clicking on the link shows a communication between a user and chatgpt
![image](https://github.com/user-attachments/assets/b3e33084-63cc-4557-b621-69d36a47f66a)
![image](https://github.com/user-attachments/assets/3bb2fd19-bf1b-4e1b-aed0-13806b37e9b8)
![image](https://github.com/user-attachments/assets/a267860d-a797-456c-929b-3f2608e3ccb6)

Basically the first and second message isn't that useful because it just tells the bot to generate random flag

But at the end of the message the user said this:

```
RapAlaNivDwoOsM NwiOksT RapAlaNivDwoOsM

np problem?
```

Looking at the first line we can see a weird looking value

At first it might seem like maybe some sort of cipher but that's not right

If you notice it well you will see that there are so many reoccuring capitalized character

Parsing them out yields this:

```
RANDOM NOT RANDOM
```

And now we just put it well in the flag format and that's the flag 🙂

```
Flag: csean-ctf{random_not_random}24
```
