# https://www.acmicpc.net/problem/10986


# import sys

# total, tar = map(int, sys.stdin.readline().split())

# tem = list(map(int, sys.stdin.readline().split()))

# prepix = [0 for i in range(tar)]
# presum = 0

# prepix[0] = 1


# for i in range(total):
#     presum += tem[i]
#     # prepix.append(presum%tar)

#     prepix[presum % tar] += 1

# # print(prepix)
# """
# 나머지가 같은 두 부분합을 고르면 두 구간은 결국 tar의 배수가 된다.
# 나머지가 0인 경우는 부분합 자체가 tar의 배수인 경우이므로 두 구간이 아니라 본인 구간도 될 수 있기 때문에
# index가 0인 (부분합 0) 것을 포함
# """
# ans = 0
# for i in prepix:
#     ans += i * (i - 1) // 2

# print(ans)


import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * n
c = [0] * m
ans = 0

s[0] = a[0]
for i in range(1, n):
    s[i] = s[i - 1] + a[i]

for i in range(n):
    re = s[i] % m
    if re == 0:
        ans += 1
    c[re] += 1

for i in range(m):
    if c[i] > 1:
        ans += c[i] * (c[i] - 1) // 2

print(ans)
