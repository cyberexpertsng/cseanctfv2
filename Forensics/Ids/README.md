![image](https://github.com/user-attachments/assets/242dc6ea-c10c-4722-8482-84a4614bd224)

I downloaded the file to my kali machine

```
┌──(root㉿kali)-[/home/csean_ctf/forensics/ids]
└─# ls -la                
total 52
drwxr-xr-x 2 root      root       4096 Sep 26 20:04 .
drwxr-xr-x 5 root      root       4096 Sep 26 21:05 ..
-rw-r--r-- 1 root      root      41934 Sep 26 20:03 637365616e2d6374667b7930755f676f745f6d337d3234.txt
```

Catting the file gave me some weird stuffs, but then the name of the file gave it away. It's a hexadecimal string. So I just decoded with cyberchef

![image](https://github.com/user-attachments/assets/fed4f46f-5b55-4b48-9a6c-c1f2af4e255c)

FLAG:```csean-ctf{y0u_got_m3}24```
