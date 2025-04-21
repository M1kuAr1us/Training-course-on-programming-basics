def gcd(a,b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

a = int(input("enter the first number to calculate the NSD: "))
b = int(input("enter the second number to calculate the NSD: "))
print(gcd(a,b))