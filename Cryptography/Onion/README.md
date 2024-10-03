## Onion

Description: My radio only accepts readings in MHz. However, I managed to intercept some signals at 0.05 GHz<br>
Solves: 5

---
Solution
---

We are given a file called `wav` which has a size of `44mb` that's oddly too large

Checking the content reveals that it's likely a base64 encoded value

After decoding we noticed that it gives another base64 encoded value

This means this plaintext content was likely base64 encoded multiple times

To solve I wrote a script to decoded the file till it isn't decodable

```python
import base64

with open("wav", "r") as f:
    enc = f.read()

while True:
    try:
        enc = base64.b64decode(enc)
        print(enc)
    except Exception as e:
        pass
```

Doing that gave the flag

```
Flag: csean-ctf{5l0w_5cr1pt}24
```
