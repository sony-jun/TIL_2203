# https://www.acmicpc.net/problem/1929


import sys

li = [1] * (1000001)
for i in range(2, int(1000001**0.5) + 1):
    if li[i] == 1:
        for j in range(i + i, 1000001, i):
            li[j] = 0

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    a = b = 0
    for i in range(2, n // 2 + 1):
        if li[i] == 1 and li[n - i] == 1:
            a, b = i, n - i
            break
    if a + b:
        print(f"{n} = {a} + {b}")
    else:
        print("Goldbach's conjecture is wrong.")
