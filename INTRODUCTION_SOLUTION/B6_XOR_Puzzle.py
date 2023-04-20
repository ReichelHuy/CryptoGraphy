import sys
import base64
from Crypto.Util.number import *
from pwn import *
s=bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
for i in range(0,20):
    print(xor(s,i))