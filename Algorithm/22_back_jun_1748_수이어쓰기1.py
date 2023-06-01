# https://www.acmicpc.net/problem/1748


n = input()

le = len(n)

cnt = 0

for i in range(le - 1):
    cnt += 9 * (10**i) * (i + 1)

a = cnt + ((int(n) - (10 ** (le - 1))) + 1) * (le)

print(a)


# 규칙 못찾았을 때
# from sys import stdin

# input = stdin.readline
# n = int(input())

# cnt = 0
# for i in range(1, n + 1):
#     cnt += len(str(i))

# print(cnt)
