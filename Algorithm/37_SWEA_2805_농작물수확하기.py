# 홀수 matrix 에 마름모를 어떻게 구현할 것인가?
# 숫자가 정해지면 마름모 모양도 자동으로 정해진다

# 5 X 5 기준
# (2,0)
# (1,1) , (2,1) , (3,1)
# (0,2) , (1,2) , (2,2) , (3,2) , (4,2)
# (1,3) , (2,3) , (3,3)
# (2,4)


t = int(input())
for p in range(1, t + 1):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    cnt = 0
    x = n // 2
    y = n // 2

    for i in range(n):
        for j in range(x, y + 1):
            cnt += matrix[i][j]

        if i < n // 2:
            x -= 1
            y += 1
        else:
            x += 1
            y -= 1

    print(f"#{p} {cnt}")


"""

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input())) for _ in range(N)]
    ans = 0  # output 변수

    # s: 시작포인트, e: 끝포인트
    s, e = N // 2, N // 2
    for i in range(N):
        for j in range(s, e+1):
            ans += a[i][j]
        # 행의 인덱스가 mid 전까지는 s-e 간격 늘리고 mid 이후로는 간격 줄임
        if i < N // 2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print("#{} {}".format(tc, ans))



"""
