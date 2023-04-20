import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from pwn import xor

cookie = bytes.fromhex("b94fcc1a9767e05dcd09eb6a984e2336cd51582c9cdd250bc97421a3ccf2b9e4c437fbfa94e0a54dba28b75381ebb30a")


def response(block, iv):
    url = "http://aes.cryptohack.org/flipping_cookie/check_admin/"
    url += block.hex()
    url += '/'
    url += iv.hex()
    url += "/"
    r = requests.get(url)
    js = r.json()
    print(js)

iv = cookie[:16]
block1 = cookie[16:32]
response(block1, xor(xor(b"admin=False;expi", pad(b"admin=True;", 16)), iv))