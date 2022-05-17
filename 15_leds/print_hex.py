from intelhex import IntelHex

ih = IntelHex() 
ih.loadfile("leds.hex", format="hex")
with open('hexdump.txt', 'w') as f:
    ih.dump(f, width=16)
