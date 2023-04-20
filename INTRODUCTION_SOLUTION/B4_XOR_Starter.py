import sys
import base64
from Crypto.Util.number import *
from pwn import *
# s1 = "lable"
# result = b""
# for char in s1:
#     result += xor(char.encode('ascii'), 13)
# print(result)


s = "label"
key = 13
result = ""

for char in s:
    # XOR the character with the key
    xored_char = chr(ord(char) ^ key)
    result += xored_char
    print(result)

# Output the result in the required format
print("crypto{" + result + "}")
