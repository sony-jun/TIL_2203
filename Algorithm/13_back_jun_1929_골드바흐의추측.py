from sys import stdin

array = [True for i in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

t = int(input())
for j in range(t):
    n = int(input())
    cnt = 0
    for k in range(2, (n // 2) + 1):
        if array[k] and array[n - k]:
            cnt += 1
    print(cnt)
