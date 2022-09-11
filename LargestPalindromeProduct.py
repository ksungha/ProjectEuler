from configparser import SafeConfigParser
from itertools import product
from operator import truediv

max = 0


def isPalindrome(n):
    curr = str(n)
    reverse = curr[::-1]
    if curr == reverse:
        return True
    else:
        return False


for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        prod = i * j
        if isPalindrome(prod) and max < prod:
            max = prod
            print(max)
        else:
            continue
