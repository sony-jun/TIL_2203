# https://www.acmicpc.net/problem/10830


import sys

input = sys.stdin.readline

N, B = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]


def mul(U, V):
    n = len(U)
    Z = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % 1000

    return Z


def square(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A

    tmp = square(A, B // 2)
    if B % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)


result = square(A, B)
for r in result:
    print(*r)


# 자연수의 거듭제곱을 분할정복으로 푸는 아이디어를 그대로 사용한다. 다만 여기선 행렬의 거듭제곱이므로, 행렬의 곱셈을 연산하는 함수를 정의해줘야 한다.

# A^k일 때

# k가 홀수이면, A^(k//2) A^(k//2) A 로 분할

# k가 짝수이면, A^(k//2) * A(k//2) 로 분할

# 행렬의 곱셈 함수는, 행렬의 곱셈 계산 방법을 그대로 코드로 구현하면 된다.

# 행렬의 곱셈 방법은 백준 2740 행렬 곱셈 문제 풀이 포스팅을 참고하자.


# 거듭제곱 함수를 호출할 때, 분할한 문제를 정복할 때 행렬의 곱셈을 수행하는데,

# 행렬 곱셈 함수에서 나머지 연산을 정의해놨으므로 문제 조건을 충족하지만 지수가 1일 경우에는 그 구문을 거치지 않아서 나머지 연산이 수행되지 않는다.

# 따라서 B == 1인 경우, A를 바로 리턴하지 말고, 나머지 연산을 수행 후 리턴해줘야 한다. 입력된 행렬 A의 원소 중에 1000이 있을 수도 있기 때문.
