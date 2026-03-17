n = int(input())
count = 0
for i in range(1, n + 1):
    o = int(input())
    if(o == 0):
        count += 1
print(count)