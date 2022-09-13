n = 100
a1 = 0
a2 = 0
diff = 0

for i in range(n+1):
    a1 = + a1 + i ** 2

for i in range(n+1):
    a2 = a2 + i

a2 = a2 ** 2
diff = a2 - a1
print(diff)
