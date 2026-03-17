def power(a:int, n:int):
    por = 1
    for i in range(n):
        por *= a

    return por

f = int(input())
r = int(input())
print(power(f, r))