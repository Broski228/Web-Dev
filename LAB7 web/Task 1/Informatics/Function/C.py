def xor(x, y):
    return (x or y) and not (x and y)

x, y = map(int, input().split())
print(1 if xor(x, y) else 0)