from sys import stdin

array = [True for i in range(100000001)]

for i in range(2, 10001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

n, m = map(int, input().split())
for k in range(n, m):
    if array[k] == True:
        if str(k) == str(k)[::-1]:
            print(k)
print(-1)
