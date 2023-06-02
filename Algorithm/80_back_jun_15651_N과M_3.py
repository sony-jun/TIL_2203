# https://www.acmicpc.net/problem/15651


# 가장 간단한 형태의 DFS 문제 15649문제에서 if문이 빠진걸 알 수 있다

n, m = map(int, input().split())

s = []


def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()


dfs()
