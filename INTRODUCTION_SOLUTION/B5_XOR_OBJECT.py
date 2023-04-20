import sys
import base64
from Crypto.Util.number import *
from pwn import *
s1    = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
s1_s2 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
s2_s3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
flag_s1_s2_s3 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

s1_s2_s3=''
flag=''
result=''
for i in range (len(s1)):
    # XOR the character with the key
     xored_value = int(s1[i], 16) ^ int(s2_s3[i], 16)
     s1_s2_s3 += hex(xored_value)[2:]

for i in range (len(s1_s2_s3)):
    # XOR the character with the key
     xored_value = int(s1_s2_s3[i], 16) ^ int(flag_s1_s2_s3[i], 16)
     result += hex(xored_value)[2:]

print(result)
flag = bytes.fromhex(result)  #decode hex
print(flag)


#sai lầm cơ bản!!!!
# for i in range ( min(len(flag_s1_s2_s3),len(s1_s2_s3))):
#     # XOR the character with the key
#     if (ord(flag_s1_s2_s3[i]) !=48 & ord(s1_s2_s3[i]) !=48):  xored_char = chr(ord(flag_s1_s2_s3[i]) ^ ord(s1_s2_s3[i]))
#     else: xored_char = '0'
#     flag+=xored_char 
# print(flag)
# daa='323333694e393730376b3666376437636a30683237643666333535646d31376a3733333030333168363176363368313433333364'
# print(base64.b64encode(daa))

k1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
k2_3=bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flag=bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
print(xor(k1,k2_3,flag))  
    

 

