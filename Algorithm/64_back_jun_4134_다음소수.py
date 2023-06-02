# https://www.acmicpc.net/problem/4134


import sys
import math

f = sys.stdin.readline


def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


T = int(f())
for i in range(T):
    z = int(f())
    while True:
        if is_prime(z):
            print(z)
            break
        else:
            z += 1
