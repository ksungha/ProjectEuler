ans = 0
new = 0
current = 2
prev = 1
while current < 4000000:
    if current % 2 == 0:
        ans = current + ans
        new = prev + current
        prev = current
        current = new
        print(ans)
    else:
        new = prev + current
        prev = current
        current = new
