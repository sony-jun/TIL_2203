# https://www.acmicpc.net/problem/2578


import sys

matrix = [list(input().split()) for _ in range(5)]  # 가로
in_matrix = list(map(list, zip(*matrix)))  # 세로
cross = []  # 대각선
cross_2 = []  # 대각선 2
for i, j in zip(range(5), range(5)):
    cross.append(matrix[i][j])
lst = list(range(4, -1, -1))
for x, y in zip(lst, range(5)):
    cross_2.append(matrix[x][y])

# 하나의 리스트로 해답지?를 만듬...
li = []
for _ in range(5):
    a = input().split()
    for o in a:
        li.append(o)
for u in li:
    matrix.pop(u)
    in_matrix.pop(u)
    cross.pop(u)
    cross_2.pop(u)
    # if 공집합 []가 3개면 break, print(u)

"""
# 입력
bingo = [list(map(int, input().split())) for _ in range(5)] # 5*5의 빙고판
check = [0]*12 # 가로, 세로, 대각선 양방향을 체크를 위한 배열

count = 0 # 빙고 카운트
number = 0 # 몇 번째 숫자인지

for _ in range(5):
    teacherL = list(map(int, input().split())) # 선생님이 불러줄 숫자 받기

    for i in range(5):
        t_number = teacherL[i]   # 값 하나 받기
        number += 1 # 몇 번째 들어온 숫자인지 체크

        flag = 0    # 숫자 체크했으면 그만 돌기 위한 플래그
        for x in range(5):  # 빙고 돌면서 t_number 찾아 0으로 바꿔
            for y in range(5):
                if t_number == bingo[x][y]:
                    bingo[x][y] = 0
                    flag = 1    # 찾았으면 그만 돌래 
                    if flag == 1:   # 이미 찾은 애면 더 이상 반복X y포문에서 break
                        break
            if flag == 1:   # 이중포문이라 x밖으로 한 번 더 나가기
                break
                

    # [0 0 0 0 0/ 0 0 0 0 0/ 0/ 0]
    # 가로세로대각선 체크
    # 가로체크
        for y in range(5):  # 다섯번 돌면서 가로 5줄 각각 체크
            s = 0   # 다 합쳐서 0이면 빙고라 더해줄 sum 값
            for x in range(5):
                s += bingo[x][y]
            if s == 0:
                check[y] += 1
                if check[y] == 1:
                    count += 1
                break
    # 세로체크
        for x in range(5):
            s = 0
            for y in range(5):
                s += bingo[x][y]
            if s == 0:
                check[x+5] += 1
                if check[x+5] == 1:
                    count += 1
                break
    # 대각선체크
        s = 0
        for x, y in zip(range(5), range(5)):  # 한 번만
            for _ in range(5):
                s += bingo[x][y]
        if s == 0:
            check[10] += 1
            if check[10] == 1:
                count += 1

        lst = list(range(4, -1, -1))
        s = 0
        for x, y in zip(lst, range(5)): # 한 번만
            for _ in range(5):
                s += bingo[x][y]
        if s == 0:
            check[11] += 1
            if check[11] == 1:
                count += 1
        if count == 3:
            break
            
    # 카운트 3이면 빙고!
    if count == 3:  
        print(number)
        break
"""
