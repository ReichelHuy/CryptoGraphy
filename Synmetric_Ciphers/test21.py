import requests

string = requests.get('https://aes.cryptohack.org/block_cipher_starter/encrypt_flag')
ans = string.json()["ciphertext"]
print(ans)

#as we already have ciphertext now lets use it for requesting decryted message from given url in question
decrypted = requests.get(f'https://aes.cryptohack.org/block_cipher_starter/decrypt/{ans}/')
#it is returning as plaintext in json 
text = decrypted.json()["plaintext"]
print(text)

#now this looks like an hex string, so lets decode it 
flag = bytes.fromhex(text)
print(flag)