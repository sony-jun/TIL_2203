# https://www.acmicpc.net/problem/1978


n = int(input())
num = map(int, input().split())
sosu = 0
for j in num:
    error = 0
    if j > 1:
        for i in range(2, j):
            if j % i == 0:
                error += 1
        if error == 0:
            sosu += 1
print(sosu)
