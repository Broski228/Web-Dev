x, y = map(float, input().split())
day = 1
while x < y:
    x *= 1.1
    day += 1
print(day)