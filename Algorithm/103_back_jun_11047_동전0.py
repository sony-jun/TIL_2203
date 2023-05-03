# 그리디 알고리즘(욕심쟁이 알고리즘, Greedy Algorithm)이란
# "매 선택에서 지금 이 순간 당장 최적인 답을 선택하여 적합한 결과를 도출하자"라는
# 모토를 가지는 알고리즘 설계 기법


N, K = map(int, input().split())
coin_lst = list()
for i in range(N):
    coin_lst.append(int(input()))

count = 0
for i in reversed(range(N)):
    count += K // coin_lst[i]  # 카운트 값에 K를 동전으로 나눈 몫을 더해줌
    K = K % coin_lst[i]  # K는 동전으로 나눈 나머지로 계속 반복

print(count)
