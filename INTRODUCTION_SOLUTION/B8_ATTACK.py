import json
import socket

# Tạo một đối tượng JSON
data = {
    "buy": "flag"
}
json_data = json.dumps(data)

# Kết nối đến socket.cryptohack.org qua cổng 11112
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("socket.cryptohack.org", 11112))

# Gửi đối tượng JSON đến socket
s.sendall(bytes(json_data, encoding="utf-8"))

# Nhận dữ liệu từ socket và in ra màn hình
data = s.recv(1024)
print(data)