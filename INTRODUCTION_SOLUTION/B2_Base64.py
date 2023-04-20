import sys
import base64
from Crypto.Util.number import *
from pwn import *
s='72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
bytes_obj = bytes.fromhex(s)  #convert hex
s1=base64.b64encode(bytes_obj) ## encode
print(s1)