# 결국 1번 자르면 2개 2번 자르면 3개 3번 자르면 4개 ....
# 막대기를 자른 횟수 +1 이 남은 막대기의 개수임을 알 수 있다
stack = []
cnt = False
ans = 0

inp = list(input())
# 괄호를 모두 받음
for i in inp:
    if i == "(":  # 여는 괄호일 때
        stack.append(i)  # 스텍 ( 추가
        cnt = False  # false표시
    elif i == ")":  # 닫는 괄호일 때
        stack.pop()  # 여는 괄호를 제거
        if cnt == False:  # 만약 cnt가 False면 ()
            if len(stack) > 0:  # 스텍에 아직도 (가 남아 있을 때 즉, 막대일때
                ans += len(stack)  # 남아있는 (만큼 더해준다
        else:
            ans += 1  # 스텍이 남아있지 않다면 ans에 1을 더해준다
        cnt = True


print(ans)
