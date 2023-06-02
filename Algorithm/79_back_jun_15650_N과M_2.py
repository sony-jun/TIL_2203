# https://www.acmicpc.net/problem/15650


# 전 문제인 N과M_1 과 비교해 보자
n, m = list(map(int, input().split()))

s = []


def dfs(start):
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(start, n + 1):
        if i not in s:
            s.append(i)
            dfs(i + 1)
            s.pop()


dfs(1)


# 78_back_jun_15649_N과M_1
# n, m = list(map(int, input().split()))

# s = []


# def dfs():
#     if len(s) == m:
#         print(" ".join(map(str, s)))
#         return

#     for i in range(1, n + 1):
#         if i not in s:
#             s.append(i)
#             dfs()
#             s.pop()


# dfs()
