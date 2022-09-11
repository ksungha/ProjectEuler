def isDividiableFrom1To20(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True


number = 20

while True:
    if isDividiableFrom1To20(number):
        break
    number = number + 1

print(number)
