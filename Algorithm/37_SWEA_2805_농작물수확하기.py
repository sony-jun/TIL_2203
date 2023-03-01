# 홀수 matrix 에 마름모를 어떻게 구현할 것인가?
# 숫자가 정해지면 마름모 모양도 자동으로 정해진다

# 5 X 5 기준
# (2,0)
# (1,1) , (2,1) , (3,1)
# (0,2) , (1,2) , (2,2) , (3,2) , (4,2)
# (1,3) , (2,3) , (3,3)
# (2,4)


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    cnt = 0
    x = n // 2
    y = n // 2

    print(matrix)
