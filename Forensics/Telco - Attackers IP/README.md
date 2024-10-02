![image](https://github.com/user-attachments/assets/5aad3886-6693-4f2e-bf2d-72e62fdb9eba)

The very first thing I did was grep out IP address from the logfiles I had

![image](https://github.com/user-attachments/assets/9d501017-2a79-4139-ac8c-e8f238f72235)
![image](https://github.com/user-attachments/assets/ac2411fb-799e-4e27-898a-96d4af9359bf)
![image](https://github.com/user-attachments/assets/6b9da9d7-c473-4bd0-856a-7e6734dcef21)

This showed me that only "log a" had valid Ip Addresses, so to get the Ip Addresses with the most count I wrote a script 

```python
from collections import Counter
import re

# Function to extract IP addresses from a line
def extract_ips(line):
    # Regular expression to match IPv4 addresses
    return re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)

# Read the log file and count IP occurrences
def count_ips(log_file):
    with open(log_file, 'r') as file:
        # Extract all IP addresses
        ips = []
        for line in file:
            ips.extend(extract_ips(line))
        
        # Count occurrences of each IP
        ip_count = Counter(ips)

    # Print the IP addresses and their counts
    for ip, count in ip_count.items():
        print(f"{ip}: {count}")

# Example usage: replace 'logfile.txt' with your actual log file path
log_file = 'logfile_a.xml'
count_ips(log_file)
```
I got interesting stuffs when I ran my script

![image](https://github.com/user-attachments/assets/7a4f399a-f31c-4382-be07-db46a23cf1d9)

The top 3 Ips here are `102.164.18.195`, `181.188.139.179` and `23.4.4.223`, but then `23.4.4.223` isn't a valid ip so I added the next ip that had most count which is `31.189.124.173`

FLAG:```csean-ctf{102.164.18.195, 181.188.139.179, 31.189.124.173}24```

























