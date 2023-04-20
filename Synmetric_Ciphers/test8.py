from pwn import xor
enc = bytes.fromhex("78bcadf8a8ec4c157ffe1c6e5e371db5caaa47c6fd65b1a34bbed2a1cda7b85041e0b409af8f7342637030b9608ac181")
iv = enc[:16]
b1 = enc[16:32]
b2 = enc[32:]

print(b1.hex())
d1 = input()
d1 = xor(bytes.fromhex(d1), iv)
print(b2.hex())
d2 = input()
d2 = xor(bytes.fromhex(d2), b1)
print(d1+d2)

