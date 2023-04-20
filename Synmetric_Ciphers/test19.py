import requests
from pwn import xor
from Crypto.Util.number import long_to_bytes
CHALLENGE_NAME = 'paper_plane'
flag_enc = {"c0":"b36fbb71ef76fe9a190441d887a0c0f2","ciphertext":"18bb2afa18d0d2f53d9c6c85984070bd23d9251a0cd038935bd19082a08e57c4","m0":"b1b978d7a96925171a3e33c5de4bcb8f"}


def encrypt_flag():
    r = requests.get('https://aes.cryptohack.org/' + CHALLENGE_NAME + '/encrypt_flag/')
    tmp = r.text
    return tmp


def send_msg(ct, m0, c0):
    r = requests.get('https://aes.cryptohack.org/' + CHALLENGE_NAME + '/send_msg/' + ct + '/' + m0 + '/' + c0)
    tmp = r.text.strip()
    return tmp


#retrieve m1
c0 = flag_enc['c0']
m0 = flag_enc['m0']
ct = flag_enc['ciphertext']


#retrieve m1
def get_m1():
    m1 = [0 for _ in range(16)]
    c0_arr = [int(c0[i:i + 2], 16) for i in range(0, 32, 2)]
    for i in range(16):
        padder = i + 1
        xor_with = [0 for _ in range(16)]
        j = 15
        while j > 16 - padder:
            xor_with[j] = padder ^ m1[j]
            j -= 1
        for k in range(256):
            xor_with[15 - i] = k
            t1 = xor(c0_arr, xor_with)
            t3 = t1.hex()
            if 'received' in send_msg(ct[:32], m0, t3):
                m1[15 - i] = k ^ padder
                break
    return m1


#retrieve m2
def get_m2():
    m2 = [0 for _ in range(16)]
    c1_arr = [int(ct[i:i + 2], 16) for i in range(0, 32, 2)]
    m0_arr = [int(m0[i:i + 2],16) for i in range(0, 32, 2)]
    for i in range(16):
        print(i)
        padder = i + 1
        xor_with = [255 for _ in range(16)]
        j = 15
        while j > 16 - padder:
            xor_with[j] = padder ^ m2[j]
            j -= 1
        for k in range(256):
            xor_with[15 - i] = k
            t1 = xor(c1_arr, xor_with)
            t3 = t1.hex() + ct[32:]
            if 'received' in send_msg(t3, xor(m0_arr, xor_with).hex(), c0):
                m2[15 - i] = k ^ padder
                print(m2)
                break
    return m2


#m1 = get_m1()
m1 = [99, 114, 121, 112, 116, 111, 123, 104, 51, 108, 108, 48, 95, 116, 51, 108] #'crypto{h3ll0_t3l'
print(''.join([chr(c) for c in m1]))
#m2 = get_m2()
m2 = [51, 103, 114, 52, 109, 125, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10] #'3gr4m}'
print(''.join([chr(c) for c in m2]))
