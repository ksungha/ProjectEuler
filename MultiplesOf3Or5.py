sum = 0
n = input("enter how many digits: ")
for i in range(1, int(n)):
    if(i % 3 == 0 or i % 5 == 0):
        sum = sum + i
    i = i + 1
    print(sum)
