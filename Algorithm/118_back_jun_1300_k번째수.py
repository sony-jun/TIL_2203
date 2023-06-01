# 먼저 k보다 작은 수의 곱이 몇개인지 찾으면 된다.
# k보다 작은 수가 몇개인지 찾아내면 k가 몇번째 숫자인지 알아낼 수 있기 때문이다.

# 코드의 mid 는 b 리스트를 일렬로 나열했을 때, cnt번째 값을 나타낸다.
# 즉, a 배열에서 mid 보다 작은 값의 개수가 cnt개인 것이다.


N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in range(1, N + 1):
        temp += min(mid // i, N)  # mid 이하의 i의 배수 or 최대 N

    if temp >= K:  # 이분탐색 실행
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
