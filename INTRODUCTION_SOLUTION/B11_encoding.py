from pwn import * # pip install pwntools
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import array


r = remote('socket.cryptohack.org', 13377, level = 'debug') # connect

def json_recv():
	line = r.recvline()
	return json.loads(line.decode())

def json_send(hsh):
	request = json.dumps(hsh).encode()
	r.sendline(request)

for i in range(0,101):
	received = json_recv() #received challenge

	if "flag" in received:
		print(received)
		break

	print("\n\n")
	print("Received type: ")
	print(received["type"])
	print("Received encoded value: ")
	print(received["encoded"])

	encoding = received["type"]
	word = received["encoded"]

	if encoding == "base64":#Decode With Base64
		decoded = base64.b64decode(word).decode('utf-8')
	elif encoding == "hex": #Decode With hex
		decode_hex = codecs.getdecoder("hex_codec")
		decoded = decode_hex(word)[0].decode('utf-8')
	elif encoding == "rot13":#Decode ROT 13, CAESER
		decoded = codecs.encode(word, 'rot_13')
	elif encoding == "bigint":
		# Spent way too long troubleshooting this
		# Its a string so to make it work you have
		# to convert it.
		decoded = long_to_bytes(int(word,16)).decode('utf-8')
	elif encoding == "utf-8": #PASSED
		decoded = array.array('b', word).tobytes().decode('utf-8')

	print("DECODED: "+decoded)

	to_send = {
		"decoded": decoded
	}
	json_send(to_send)