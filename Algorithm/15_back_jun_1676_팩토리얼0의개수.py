# https://www.acmicpc.net/problem/1676


n = int(input())
cnt5 = 0
for i in range(1, n + 1):
    if i % 5 == 0:
        cnt5 += 1
    if i % 25 == 0:
        cnt5 += 1
    if i % 125 == 0:
        cnt5 += 1
print(cnt5)
# 주어진 n의 개수가 500이기 때문에 5^3승까지만 이용하면 5가 들어간 개수를 구 할 수 있다


"""
위에 내용을 간단하게 축약하면 이렇다
n = int(input())
cnt5 = 0
while n >=5:
    cnt5 += n//5
    n//=5
print(cnt5)
"""
