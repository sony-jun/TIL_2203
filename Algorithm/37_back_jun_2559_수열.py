# 문제에 있는 그대로 했더니 시간초과가 나는 문제

# import sys

# input = sys.stdin.readline

# cnt = []

# n, k = map(int, input().split())
# li = list(map(int, input().split()))

# for i in range(n - k + 1):
#     cnt.append(sum(li[i : i + k]))

# print(max(cnt))


n, k = map(int, input().split())
li = list(map(int, input().split()))

cnt = []
cnt.append(sum(li[:k]))  # 맨처음 값을 미리 더해준다

for i in range(n - k):
    cnt.append(cnt[i] - li[i] + li[k + i])  # 한칸 씩 이동하면서 처음값 삭제, 다음값 더하는 식으로 더해준다
# 윗작업보다 빠른 이유는 리스트를 전부 더하는것과 하나빼고 하나더하는것에 계산 차이가 존재하기 때문에...
print(max(cnt))
