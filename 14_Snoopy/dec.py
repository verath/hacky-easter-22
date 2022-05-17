import re, sys

def decrypt(ct):
    pt = ''
    last = 0
    for i in range(0, len(ct), 4):
        pc = dec_letter(ct[i:i+4], last) 
        pt += pc
        last ^= ord(pc)

    return pt

def dec_letter(ct, last=0):
    c = (ord(ct[2]) - 1) & 0x0f
    d = (ord(ct[3]) - 1) & 0x0f

    x = c*16+d

    pc = chr(x^last)

    return pc

x = sys.stdin.readline()
while x:
    x = re.sub('[^A-P]', '', x.upper())
    print(repr(x))
    print(decrypt(x))
    x = sys.stdin.readline()
