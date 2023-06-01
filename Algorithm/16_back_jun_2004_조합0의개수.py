# https://www.acmicpc.net/problem/2004


# 못품
# 팩토리얼 0의 개수를 구하는 방법과 같다
# 단, 5와 2를 다 구해주는 이유는 5가 더 많은 경우가 있기 때문이다
# 팩토리얼에서는 5가 2보다 많은 경우는 없기 때문에 생략.
"""
n, m = map(int, input().split())


def cnt2(t):
    two = 0
    while t != 0:
        t = t // 2
        two += t
    return two


def cnt5(t):
    five = 0
    while t != 0:
        t = t // 5
        five += t
    return five


print(
    min(
        cnt2(n) - cnt2(n - m) - cnt2(m),
        cnt5(n) - cnt5(n - m) - cnt5(m),
    )
)
"""


import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[1 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, k + 1):
    for j in range(i + 1, n + 1):
        dp[j][i] = dp[j - 1][i - 1] + dp[j - 1][i]


cnt = 0
a = str(dp[n][k])[::-1]
for i in a:
    if i != "0":
        break
    else:
        cnt += 1

print(cnt)
print(dp)
