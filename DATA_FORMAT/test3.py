import base64
#DIRECT link
with open('bruce_rsa.pub', 'rb') as f:
  a = f.read()
  a = a.split(b' ')[1]
  a = base64.b64decode(a)
  
  # method
  l = 4+int.from_bytes(a[:4], 'big')
  a = a[l:]
  
  # exponent
  l = 4+int.from_bytes(a[:4], 'big')
  a = a[l:]
  
  # modulus
  a = a[4:]
  print(int.from_bytes(a, 'big'))