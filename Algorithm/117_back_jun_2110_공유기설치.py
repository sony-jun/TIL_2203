# 바이너리 서치 - 이진탐색 (binary search)
# BigO : O(log N)
# 정렬된 자료를 반으로 나누어 탐색하는 방법
# 주의점 : 자료는 오름차순 으로 정렬된 자료여야 한다.!!!!!!!!!!!!!!!!!!!!!!!
# 이진트리, 바이너리서치는 코딩 인터뷰 단골문제
# 퍼포먼스가 아주 좋고 구현하는 중에 dynamic programming, recursion을 볼 수 있다.

n, c = map(int, input().split())
li = []
for i in range(n):
    a = int(input())
    li.append(a)
y = sorted(li)


def binary_search(y, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = y[0]
        count = 1

        for i in range(1, len(y)):
            if y[i] >= current + mid:
                count += 1
                current = y[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


start = 1
end = y[-1] - y[0]
answer = 0

binary_search(y, start, end)
print(answer)
