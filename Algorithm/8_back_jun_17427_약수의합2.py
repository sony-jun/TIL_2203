# https://www.acmicpc.net/problem/17427


# 못품! 시간 초과 뜸
n = int(input())
li = []
for j in range(1, n + 1):
    li.append(j)
cnt = 0
for i in li:
    for k in range(1, n + 1):
        if k % i == 0:
            cnt += i
print(cnt)


"""
n = int(input())

cnt = 0

for i in range(1, n + 1):
    cnt += (n // i) * i
print(cnt)
"""
