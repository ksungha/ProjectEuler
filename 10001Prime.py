import sympy

count = 0
n = 10001
i = 2
while count != n:
    if sympy.isprime(i):
        count = count + 1
    i = i + 1
print(i - 1)
