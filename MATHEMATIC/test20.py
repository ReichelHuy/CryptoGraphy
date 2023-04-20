from sage.all import *
from Crypto.Util.number import long_to_bytes, inverse

with open('/Users/duynguyendinh/Downloads/coderun/python/Cryptography/MATHEMATIC/output4.txt', 'r') as f:
  p, e = f.read().split('\n', 1)
  q = int(p.split(' ')[2].lstrip('(').rstrip(','))
  h = int(p.split(' ')[3].rstrip(')'))
  e = int(e.split(' ')[2])

def gaussian_reduction(v, u):
  while True:
    if u.norm() < v.norm(): v, u = u, v
    m = floor(v.dot_product(u) / v.dot_product(v))
    if m == 0: break
    u = u - m*v
  return v, u
 
v = vector([1, h])
u = vector([0, q])
# check "An Introduction to Mathematical Cryptography"
(f, g), _ = gaussian_reduction(v, u)

def decrypt(q, h, f, g, e):
    a = (f*e) % q
    m = (a*inverse(f, g)) % g
    return m

print(long_to_bytes(decrypt(q, h, f, g, e)).decode())  