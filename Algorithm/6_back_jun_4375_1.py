# https://www.acmicpc.net/problem/4375


n = int(input())

cnt = 1
while True:
    cnt = 10 * cnt + 1
    if cnt % n == 0:
        break
a = str(cnt)
print(a.count("1"))
