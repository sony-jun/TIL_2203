# 시간초과
t = int(input())
for i in range(t):

    n = int(input())

    cnt = 0

    for i in range(1, n + 1):
        cnt += (n // i) * i
    print(cnt)

"""
from sys import stdin
input = stdin.readline
f = [1] * 1000001
g = [0] * 1000001

for i in range( 2, len(f) ):
    j = 1
    while i*j < len(f):
        f[ i*j ] += i
        j += 1

for i in range( 1, len(g) ):
    g[i] = g[i-1] + f[i]

t = int( input() )
for _ in range( t ):
    n = int( input() )
    print( g[n] )
"""
