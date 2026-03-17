x = input()
res = ""
for i in range(len(x) - 1, -1, -1):
    res += x[i]
print(res)