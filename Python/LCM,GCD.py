import math

a = int(input("enter 1st numer : "))
b = int(input("enter 2nd numer : "))
c = int(input("enter 3rd numer : "))

X = math.gcd(a,b,c)
Y = math.lcm(a,b,c)

print(" GCD OF 1st,2nd,3rd IS = ", X)
print(" LCM OF 1st,2nd,3rd IS = ", Y)
