# https://www.acmicpc.net/problem/2493


# 문제가 이해가 안됨

import sys

r = sys.stdin.readline

# 입력 받기
n = int(r())
t_list = list(map(int, r().split()))
answer = []
stk = []
for i in range(n):
    h = t_list[i]
    if stk:
        # print(stk)
        while stk:
            if stk[-1][0] < h:
                stk.pop()
                if not stk:
                    print(0, end=" ")
            elif stk[-1][0] > h:
                print(stk[-1][1] + 1, end=" ")
                break
            else:
                print(stk[-1][1] + 1, end=" ")
                stk.pop()
                break
        stk.append([h, i])
    else:
        print(0, end=" ")
        stk.append([h, i])
