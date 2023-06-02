# https://school.programmers.co.kr/learn/courses/30/lessons/43165


# 모든 값을 다 미리 계산하는건 너무 커지나...?
# 20이면 음...안되네


def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer
