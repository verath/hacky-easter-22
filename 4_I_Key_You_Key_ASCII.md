# I Key, You Key, ASCII

> Look what I was drawing in my text editor!
> 
> ```
> .. .. .. 68 65 32 30 .. .. ..  
> .. .. 32 ██ ██ ██ ██ 32 .. ..  
> .. 7b ██ ██ ██ ██ ██ ██ 74 ..  
> .. 68 ██ ██ ██ ██ ██ ██ 31 ..  
> 73 ██ ██ ██ ██ ██ ██ ██ ██ 5f  
> 30 ██ ██ ██ ██ ██ ██ ██ ██ 6e  
> 33 ██ ██ ██ ██ ██ ██ ██ ██ 5f  
> 31 ██ ██ ██ ██ ██ ██ ██ ██ 73  
> 5f ██ ██ ██ ██ ██ ██ ██ ██ 72  
> 33 ██ ██ ██ ██ ██ ██ ██ ██ 33  
> 33 ██ ██ ██ ██ ██ ██ ██ ██ 33  
> .. 6c ██ ██ ██ ██ ██ ██ 79 ..  
> .. 5f ██ ██ ██ ██ ██ ██ 73 ..  
> .. .. 31 ██ ██ ██ ██ 6d .. ..  
> .. .. .. 70 6c 33 7d .. .. ..  
> ```

Given the title of the level, it probably has to do with ASCII encoding.

Taking the hex values top-left -> bottom-right we end up with

```
68 65 32 30 32 32 7b 74 68 31 73 5f 30 6e 33 5f 31 73 5f 72 33 33 33 33 6c 79 5f 73 31 6d 70 6c 33 7d
```

Drop that into a [hex -> ascii converter](https://www.rapidtables.com/convert/number/hex-to-ascii.html)
and we end up with the flag:

`he2022{th1s_0n3_1s_r3333ly_s1mpl3}`
