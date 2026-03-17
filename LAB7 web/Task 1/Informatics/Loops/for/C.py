import math

a, b = map(int, input().split())

for n in range(a, b + 1):
    if n >= 0:
        root = int(math.isqrt(n))
        if root * root == n:
            print(n)