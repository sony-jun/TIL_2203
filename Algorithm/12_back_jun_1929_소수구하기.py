# https://www.acmicpc.net/problem/1929


# 못품
# 에라토스테네스의 체


def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True


M, N = map(int, input().split())

for i in range(M, N + 1):
    if isPrime(i):
        print(i)
