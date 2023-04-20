from sage.all import *
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD
n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373
p= 752708788837165590355094155871 #factor
q= 986369682585281993933185289261 #factor
phi = (p - 1) * (q - 1)
d = inverse_mod(e, phi)
pt = pow(ct,d,n)
print(long_to_bytes(pt))
print(n-1-phi)