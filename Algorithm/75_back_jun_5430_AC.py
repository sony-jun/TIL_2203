# 뒤집기 R을 실행할때 마다 뒤집기가 되면 반드시 시간초과가 나기 때문에 모두 센 후
# R의 개수가 홀수일때만 뒤집기 한번 실행

# 참고부분

# 입력 배열의 파싱 , 0번째 인덱스와 마지막 인덱스를 제외하면
# [1,2,3,4] = > 1,2,3,4 로 만들어지므로
# arr[1:-1] 로 하면 1,2,3,4 라는 문자열이 만들어진다.
# 여기서 split(',') 하면 ['1','2','3','4'] 가 만들어진다.
# R을 할 시에는 배열을 reverse 해준다.
# 하지만 n번의 연산이 필요하다.
# R의 최대 횟수 100,000 , 배열의 최대 크기 100 , 테스트케이스 100개
# 100 100,000 100 = 1,000,000,000 1억번의 시간이 대략 소요가 된다. 시간초과가 날수도 있기때문에
# R을 짝수번 했을경우에는 배열을 reverse시키지 않아도 괜찮다.
# 그래서 R이 나왔을 경우에는 카운트를 해줘서
# D가 나왔을때 R이 짝수일경우에는 popleft , 홀수일경우에는 pop 을 해주고
# 마지막에 R이 홀수일 경우에 배열을 reverse해서 출력해주면 된다.


import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue) - 1
    flag = 0
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in p:
        if j == "R":
            rev += 1
        elif j == "D":
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
