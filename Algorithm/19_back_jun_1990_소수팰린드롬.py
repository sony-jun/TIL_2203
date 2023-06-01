# https://www.acmicpc.net/problem/1990


# 무슨 조건이 더 필요하지???
from sys import stdin

n, m = map(int, input().split())
if m > 10000000:
    m = 10000000
array = [True for i in range(m)]

for i in range(2, m**0.5):
    if array[i]:
        for k in range(i + i, m, i):
            array[k] = False


for k in range(n, m):
    if array[k] == True:
        if str(k) == str(k)[::-1]:
            print(k)
print(-1)


# 다른게 뭐지?
# def isPrime(num):
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# a,b=map(int,input().split())
# #10,000,000이상인 팰린드롬수는 존재 X
# if b>10000000 :b=10000000
# palindrome=[n for n in range(a,b+1)if str(n)==str(n)[::-1]]
# for n in palindrome:
#     if isPrime(n):print(n)
# print(-1)
