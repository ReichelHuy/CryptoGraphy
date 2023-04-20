import requests
from Crypto.Util.Padding import unpad
from Crypto.Cipher import ARC4
from Crypto.Util.number import long_to_bytes

# Helper function, which swaps two values in the box.
def swapValueByIndex(box, i, j):
    temp = box[i]
    box[i] = box[j]
    box[j] = temp

# Initialize S-box.
def initSBox(box):
    if len(box) == 0:
        for i in range(256):
            box.append(i)
    else:
        for i in range(256):
            box[i] = i

# Key schedule Algorithm (KSA) for key whose value is in unicode.
def ksa(key, box):
    j = 0
    for i in range(256):
        j = (j + box[i] + ord(key[i % len(key)])) % 256
        swapValueByIndex(box, i, j)

def send_cmd(ciphertext, nonce):
    res = requests.get(f"http://aes.cryptohack.org/oh_snap/send_cmd/{ciphertext.hex()}/{nonce.hex()}/")
    return res.json()

key = [0]*3
key += [99, 114, 121, 112, 116, 111, 123, 119, 49, 82, 51, 100, 95, 101, 113, 117, 49, 118, 52, 108, 51, 110, 116, 95, 112, 114, 49, 118, 52, 99, 121, 63, 33, 125]

for i1 in range(len(key)-3,34):
    prob = [0] * 256
    for i2 in range(256):
        key[0] = i1+3
        key[1] = 255
        key[2] = i2

        j = 0
        
        box = []
        initSBox(box)

        # Simulate the S-Box after KSA initialization.
        for i in range(key[0]):
            j = (j + box[i] + key[i]) % 256
            swapValueByIndex(box, i, j)
            # Record the original box[0] and box[1] value.
            if i == 1:
                original0 = box[0]
                original1 = box[1]

        i = key[0]
        z = box[1]
        # if resolved condition is possibly met.
        if z + box[z] == key[0]:
            # If the value of box[0] and box[1] has changed, discard this possibility.
            if (original0 != box[0] or original1 != box[1]):
                continue
                
            nonce = long_to_bytes(key[0])+long_to_bytes(key[1])+long_to_bytes(key[2])
            a = send_cmd(b'\x00',nonce)['error']
            keyStreamByte = int(a.split(': ')[1],16)
            
            keyByte = (box.index(keyStreamByte) - j - box[i]) % 256
            prob[keyByte] += 1
        # Assume that the most hit is the correct password.
        higherPossibility = prob.index(max(prob))
    key.append(higherPossibility)
    print(higherPossibility, chr(higherPossibility))
    
for i in key[3:]:
    print(chr(i),end="")