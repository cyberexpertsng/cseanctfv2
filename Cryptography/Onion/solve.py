import base64

with open("wav", "r") as f:
    enc = f.read()

while True:
    try:
        enc = base64.b64decode(enc)
        print(enc)
    except Exception as e:
        pass
