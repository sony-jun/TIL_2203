n = int(input())
m = int(input())
hubo = map(int, input().split())

li = []  # 리스트
num_li = []  # 인덱스 번호("현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제")

for i in hubo:
    if i in li:  # 리스트에 있다면
        a = li.index(i)  # 인덱스 번호를 찾음
        num_li[a] += 1  # 그 숫자를 더해줌(하나씩 추가됨)
    else:  # 리스트에 없다면
        if len(li) >= n:  # 만약 리스트 길이가 사진틀의 길이보다 크게 되면
            a = num_li.index(min(num_li))  # 넘버 리스트에 가장 작은 리스트 값을 찾아준다 (index)
            del li[a]  # 그 가장 작은 값을 리스트에서 삭제
            del num_li[a]  # 넘버리스트에서도 삭제
        li.append(i)  # 리스트에 넣어줌
        num_li.append(1)  # 리스트 번호를 넣어줌(딕서녀리 넣듯이 1추가)
li.sort()  # 크기순으로 정렬
print(*li)  # 출력
