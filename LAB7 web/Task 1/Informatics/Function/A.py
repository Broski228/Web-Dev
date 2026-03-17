def min(a, b, c, d):
    if (a < b and a < c and a < d):
        return a
    elif (b < c and b < d and b < a):
        return b
    elif(c < a and c < d and c < b):
        return c
    elif(d < a and d < b and d < c):
        return d

print(min(2, 3, 1, 6))