import sys
import base64
from Crypto.Util.number import *
from pwn import *
s=11515195063862318899931685488813747395775516287289682636499965282714637259206269 
s1=long_to_bytes(s)
print(s1)