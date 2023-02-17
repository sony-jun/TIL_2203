import pprint

n = int(input())

matrix = [list(map(int, (input().split()))) for _ in range(n)]

print(matrix)


# 일단, 섬인지 아닌지를 판명부터
# 그 섬들에 이름표(?)를 붙인다
# 그 다음에 연결을 해보자
