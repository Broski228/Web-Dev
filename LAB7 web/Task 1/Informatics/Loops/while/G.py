x, p, y = map(int, input().split())
years = 0
while x < y:
    x = int(x * (1 + p / 100))
    years += 1
print(years)