![image](https://github.com/user-attachments/assets/8bddde2f-ad64-4c31-b782-106f62fd4a65)

I downloaded the file to my kali machine

```
┌──(root㉿kali)-[/home/csean_ctf/forensics/sus]
└─# ls -la
total 1388
drwxr-xr-x 2 root      root        4096 Sep 26 20:35 .
drwxr-xr-x 5 root      root        4096 Sep 26 21:05 ..
-rw-r--r-- 1 root      root      544680 Sep 26 20:19 emails.log
```

I analyzed this using sublime text, and then I noticed something

![image](https://github.com/user-attachments/assets/855b7843-8031-478b-a56f-0a266458ef4f)

So , this is a mail between two people. Reading their conversations I saw this

![image](https://github.com/user-attachments/assets/9231101f-d52c-421d-a679-3571cef680a1)

There's a png file that was sent, but then it is in base64 format. So I copied the base64, saved it to my device 

```
┌──(root㉿kali)-[/home/csean_ctf/forensics/sus]
└─# ls -la
total 1388
drwxr-xr-x 2 root      root        4096 Sep 26 20:35 .
drwxr-xr-x 5 root      root        4096 Sep 26 21:05 ..
-rw-r--r-- 1 root      root      544680 Sep 26 20:19 emails.log
-rw-r--r-- 1 root      root      497221 Sep 26 20:32 not_malicious.txt
```

![image](https://github.com/user-attachments/assets/b427c510-b31a-4ed3-89c0-47bdd4b5aed1)


I then uploaded it to cyberchef so I can save the output in png format

![image](https://github.com/user-attachments/assets/40755c5f-1d13-4fce-ad24-d78edd4f36a3)

```
┌──(root㉿kali)-[/home/csean_ctf/forensics/sus]
└─# ls -la
total 1388
drwxr-xr-x 2 root      root        4096 Sep 26 20:35 .
drwxr-xr-x 5 root      root        4096 Sep 26 21:05 ..
-rw-r--r-- 1 root      root      368071 Sep 26 20:35 download.png
-rw-r--r-- 1 root      root      544680 Sep 26 20:19 emails.log
-rw-r--r-- 1 root      root      497221 Sep 26 20:32 not_malicious.txt
                                                                                
┌──(root㉿kali)-[/home/csean_ctf/forensics/sus]
└─# file download.png 
download.png: PNG image data, 525 x 525, 8-bit/color RGBA, non-interlaced
```

Checking the content of the image gave me the flag

![image](https://github.com/user-attachments/assets/3aceeec4-2d42-4fa4-bcdb-bed375bd4b4f)

FLAG:```csean-ctf{4n4lyze_3verything_luffy}24```
