import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range(1, n + 1):
    if i * i <= n:
        cnt += 1
print(cnt)
