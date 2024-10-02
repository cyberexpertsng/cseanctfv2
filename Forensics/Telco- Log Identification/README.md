![image](https://github.com/user-attachments/assets/83f9749a-4411-409d-ac4d-eaeadb004e0c)

I downloaded those files to my machine then converted them to xml files

```
┌──(root㉿kali)-[/home/csean_ctf/forensics/telco_log_ident]
└─# ls -la
total 39128
drwxr-xr-x 3 root root     4096 Sep 26 22:46 .
drwxr-xr-x 5 root root     4096 Sep 26 21:05 ..
-rw-r--r-- 1 root root 21041152 Sep 26 21:05 logfile_a.evtx
-rw-r--r-- 1 root root 10555392 Sep 26 21:05 logfile_b.evtx
-rw-r--r-- 1 root root  8458240 Sep 26 21:05 logfile_c.evtx
```

![image](https://github.com/user-attachments/assets/3ee91650-e2c6-48cc-af69-72c553a84b87)

```
┌──(root㉿kali)-[/home/csean_ctf/forensics/telco_log_ident]
└─# ls -la                    
total 108592
drwxr-xr-x 3 root root     4096 Sep 27 09:53 .
drwxr-xr-x 5 root root     4096 Sep 26 21:05 ..
-rw-r--r-- 1 root root 21041152 Sep 26 21:05 logfile_a.evtx
-rw-r--r-- 1 root root 49454974 Sep 27 09:53 logfile_a.xml
-rw-r--r-- 1 root root 10555392 Sep 26 21:05 logfile_b.evtx
-rw-r--r-- 1 root root  3685138 Sep 27 09:53 logfile_b.xml
-rw-r--r-- 1 root root  8458240 Sep 26 21:05 logfile_c.evtx
-rw-r--r-- 1 root root 17986941 Sep 27 09:53 logfile_c.xml
```
The next thing I did was to analyze the xml files using sublime text. The task here is to investigate the name of the log files

For Log A

![image](https://github.com/user-attachments/assets/87c41d2a-9798-4783-a84d-d92fb316c82c)

This is a `Security Event Log`

For Log B

![image](https://github.com/user-attachments/assets/315dd387-6d05-4e05-ac93-cfbb148855cc)

This is a `PowerShell Log`

For Log C

![image](https://github.com/user-attachments/assets/5784a10d-6f35-4e93-99c5-f819c4372247)

This is a `SMBServer Log`

FLAG:```csean-ctf{Security Event Log, PowerShell Log, SMBServer Log}24```
























