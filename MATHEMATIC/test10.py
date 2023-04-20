from sympy.ntheory.modular import crt
# Các đồng dư tuyến tính ban đầu
congruences = [(2, 5), (3, 11), (5, 17)]
# Tính toán mô đun chung
n = 1
for a, m in congruences:
    n *= m
# Tính toán các hệ số trong định lý Trung Hoa dư
coeffs = []
for a, m in congruences:
    mi = n // m
    si, _ = crt([mi, m], [m, mi])
    coeffs.append(a * si * mi)
# Tính toán nghiệm
x = sum(coeffs) % n
# In kết quả
print(x)