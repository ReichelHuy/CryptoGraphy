import requests
import string

padding = b""
for i in range(130,150):
	padding += chr(i).encode()

charset = string.ascii_lowercase + string.digits + "{}_"
charset = charset.encode()

print(padding , charset)

known_flag = b'crypto{CRIME_571ll_p4y5}'
candidate = b'a'
pt = padding + candidate + known_flag + padding
r = requests.get(f'https://aes.cryptohack.org/ctrime/encrypt/{pt.hex()}/')
print(len(r.json()["ciphertext"]))

while True:
	best_candidate = None
	best_len = 100000
	count = 0
	candidate_list = []
	for candidate in range(30,128):
		pt = known_flag + chr(candidate).encode() * 5
		r = requests.get(f'https://aes.cryptohack.org/ctrime/encrypt/{pt.hex()}/')
		length = len(r.json()["ciphertext"])
		if length < best_len:
			best_candidate = candidate
			best_len = length
			count = 1
			candidate_list = []
			candidate_list.append(candidate)
		elif length == best_len:
			count += 1
			candidate_list.append(candidate)

	known_flag = known_flag + chr(best_candidate).encode()
	print(known_flag)
	print(candidate_list , count)




