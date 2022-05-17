# The Unicorn

> Ain't no CTF without a unicorn!
> 
> unicorn.png
> 


![unicorn.png](img/9_unicorn.png)

The image is pretty large (almost 0.5mb), seems odd for a .png. Run it through
[binwalk](https://github.com/ReFirmLabs/binwalk) we find that the .png is made
up of multiple images:

```
$ binwalk --dd='.*' --directory=./out unicorn.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 512, 8-bit/color RGBA, non-interlaced
54            0x36            TIFF image data, big-endian, offset of first image directory: 8
106516        0x1A014         PNG image, 512 x 512, 8-bit/color RGBA, non-interlaced
106570        0x1A04A         TIFF image data, big-endian, offset of first image directory: 8
213032        0x34028         PNG image, 512 x 512, 8-bit/color RGBA, non-interlaced
213086        0x3405E         TIFF image data, big-endian, offset of first image directory: 8
319548        0x4E03C         PNG image, 512 x 512, 8-bit/color RGBA, non-interlaced
319686        0x4E0C6         Zlib compressed data, best compression
352486        0x560E6         PNG image, 512 x 512, 8-bit/color RGBA, non-interlaced
352540        0x5611C         TIFF image data, big-endian, offset of first image directory: 8
459002        0x700FA         PNG image, 512 x 512, 8-bit/color RGBA, non-interlaced
459056        0x70130         TIFF image data, big-endian, offset of first image directory: 8
```

One of these contains a QR code with the flag:

![qr code](img/9_4E03C.png)


flag: `he2022{1_c_un1c0rns_3v3rywh3r3!}`
