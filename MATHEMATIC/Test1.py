def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

array=[]
a=int(input(""))
b=int(input(""))
print(gcd(a, b))
g=gcd(a,b)
for i in range(1,g+1):
    if g%i == 0:
        array.append(i)
print("Cac uoc : ",array)        