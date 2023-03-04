# 1로만들기랑 같은 방법이지 않을까?
# dp로 접근함
# 아니였음...
# 찾아보니 BFS문제였음...
# 보고 BFS임을 어떻게 떠올릴 수 있을까?
# BFS구조에대해서 내가 잘 몰라서 그런가?
from collections import deque


def BFS():
    queue = deque()
    queue.append(N)
    while queue:
        present = queue.popleft()
        if present == K:
            print(dist[present])
            break
        for not_present in (present + 1, present - 1, present * 2):
            if 0 <= not_present <= MAX and not dist[not_present]:
                dist[not_present] = dist[present] + 1
                queue.append(not_present)


MAX = 10**5
dist = [0] * (MAX + 1)
N, K = map(int, input().split())
BFS()
