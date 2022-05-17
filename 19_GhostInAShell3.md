# Ghost in a Shell 3

> ```
>   _, _,_  _,  _, ___   _ _, _    _,    _, _,_ __, _,  _,    ,  ,  ,  
>  / _ |_| / \ (_   |    | |\ |   /_\   (_  |_| |_  |   |     |  |  |  
>  \ / | | \ / , )  |    | | \|   | |   , ) | | |   | , | ,   |  |  |  
>   ~  ~ ~  ~   ~   ~    ~ ~  ~   ~ ~    ~  ~ ~ ~~~ ~~~ ~~~   ~  ~  ~  
> ______________________________________________________________________  
>  ,--.     ,--.     ,--.  
> | oo |   | oo |   | oo |   
> | ~~ |   | ~~ |   | ~~ |   o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  
> |/\/\|   |/\/\|   |/\/\|     
> ______________________________________________________________________  
> 
> ```
> 
> Connect to the server, snoop around, and find the flag!
> 
> ssh 46.101.107.117 -p 2203 -l pinky
> password is: !speedy!



```
> ssh 46.101.107.117 -p 2203 -l pinky
> pinky@46.101.107.117's password: !speedy!

165efc503881:~$ ls -la
total 28
drwxr-xr-x    1 root     root          4096 May 15 08:02 .
drwxr-xr-x    1 root     root          4096 Mar 16 09:52 ..
-rwxr-xr-x    1 root     root            15 May 15 08:01 .bashrc
-rw-r--r--    1 root     root            64 May 15 08:13 flag.enc
-r--------    1 root     root            32 Mar 13 18:22 flag.txt
```

We are not allowed to read flag.txt, because its owned by root. The flag.enc
is not human readable. Given its extension it is probably encrypted.


Running ps we find a reference to cron running:
```
165efc503881:~$ ps
PID   USER     TIME  COMMAND
    1 root      0:00 bash /entry.sh /usr/sbin/sshd -D -e -f /etc/ssh/sshd_config
  403 root      0:00 crond
  405 root      0:00 sshd: /usr/sbin/sshd -D -e -f /etc/ssh/sshd_config [listener] 0 of 10-100 startups
  503 root      0:00 sshd: pinky [priv]
  505 pinky     0:00 sshd: pinky@pts/0
  506 pinky     0:00 -sh
  515 pinky     0:00 ps
```

We find a job that looks interesting in the crontabs:

```
165efc503881:~$ cat /etc/cron/crontab
* * * * * /opt/bannerkoder/cipher.sh > /dev/null 2>&1
# empty line needed!
```

`/opt/bannerkoder/cipher.sh` creates our flag.enc file:

```
165efc503881:~$ cat /opt/bannerkoder/cipher.sh ; echo
#!/bin/bash
date +%s | md5sum | base64 | head -c 32 > /tmp/7367111C2875730D00686C13B98E7F36
openssl enc -aes-256-cbc -e -in /home/pinky/flag.txt -out /home/pinky/flag.enc -kfile /tmp/7367111C2875730D00686C13B98E7F36
```

The keyfile is readable by us, and so is the encrypted flag.enc. So we use
openssl to decrypt the flag for us:

```
$ openssl enc -d -aes-256-cbc -in /home/pinky/flag.enc -kfile /tmp/7367111C2875730D00686C13B98E7F36 ; ec
ho
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
he2022{0p3n-35-35-37-f0r-pr0fit}
```

Flag: `he2022{0p3n-35-35-37-f0r-pr0fit}`.
