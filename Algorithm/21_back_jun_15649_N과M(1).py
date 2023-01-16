# 못품
# 아예 dfs로 푸는 문제라는걸 인지하지 못했음


def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        print(s)
        print(visited)
        visited[i] = False


n, m = map(int, input().split())
s = []
visited = [False] * (n + 1)

dfs()
