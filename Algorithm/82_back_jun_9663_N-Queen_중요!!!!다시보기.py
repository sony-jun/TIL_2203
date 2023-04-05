# 이해하기 아주 어려운 문제....다시 한번 검토 할 필요가 있다

n = int(input())

ans = 0
row = [0] * n


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True


def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)


n_queens(0)
print(ans)

# 다른 풀이

# import sys

# def logic(n):
#     if n == N: # 마지막까지 탐색 완료
#         global count # 전역변수 설정

#         count += 1 # 값 증가
#     else:
#         for i in range(N):
#             if visited[i]:
#                 continue

#             board[n] = i # (n, i)에 퀸 올리기

#             if check(n): # 퀸 놓기 조건에 맞다면
#                 visited[i] = True
#                 logic(n+1) # 다음 행으로 넘어가긴
#                 visited[i] = False


# def check(n):
#     for i in range(n):
#         # 이미 놓여진 퀸과 같은 열이거나 대각선 상에 있는지 확인
#         # (행끼리의 차 == 열끼리 차의 절대값)이 True면 대각선 상에 있는 것임
#         if (board[n] == board[i]) or (n - i == abs(board[n] - board[i])):
#             return False

#     return True


# if __name__ == '__main__':
#     N = int(sys.stdin.readline())
#     count = 0
#     board = [0 for _ in range(N)] # 인덱스 번호 == 행, 인덱스 값 == 열
#     visited = [False for _ in range(N)]

#     logic(0)
#     print(count)
