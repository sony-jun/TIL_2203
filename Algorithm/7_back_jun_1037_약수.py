# https://www.acmicpc.net/problem/1037


n = int(input())
li = list(map(int, input().split()))
# 숫자 1개라면, 같은값을 곱해주고, 다르면 최소값*최대값
print(max(li) * min(li))
