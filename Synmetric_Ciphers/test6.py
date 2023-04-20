from Crypto.Cipher import AES
import hashlib
import random


# /usr/share/dict/words from
with open("/usr/share/dict/words") as f:
    words = [w.strip() for w in f.readlines()]

#KEY = hashlib.md5(keyword.encode()).digest()

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = password_hash

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted

for key in words:
    pass_key = hashlib.md5(key.encode()).digest()
    code = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
    dec = decrypt(code, pass_key)
    if(b'crypto{' in dec):
        print(dec)