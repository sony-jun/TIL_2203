INC = 0
DEC = 1


# 2번째로 사용될 함수
def func_a(arr):
    length = len(arr)
    # 마킹된 리스트의 길이를 측정
    ret = [0 for _ in range(length)]
    # 마킹된 리스트의 길이와 동일한 return할 리스트 생성
    # 마킹된 리스트를 순회하면서 지그재그 배열 검열하여 ret 리스트에 저장
    ret[0] = 1
    # ret 리스트의 첫 번째 요소를 0으로 지정
    for i in range(1, length):
        # 첫 번째 요소를 제외한 리스트의 길이만큼 반복
        if arr[i] != arr[i - 1]:
            # 만약 마킹된 리스트의 요소(INC, DEC)가 서로 다르다면
            ret[i] = ret[i - 1] + 1
            # 지그재그 배열인 경우 길이를 기록
            # 첫 번째 요소가 1이기 때문에 다른 경우가 1번이면 2가 저장
            # 다른 경우가 2번이면 3이 저장
        else:
            ret[i] = 2
            # 마킹된 리스트가 없을 경우 2를 기록
    return ret
    # 마킹된 리스트(arr)의 길이를 저장한 ret 리스트를 반환


# 1번째로 사용될 함수
def func_b(arr):
    global INC, DEC
    # 전역 변수를 사용하기 위해 INC, DEC 선언
    length = len(arr)
    ret = [0 for _ in range(length)]
    # arr 리스트의 길이와 동일한 ret 리스트 생성
    ret[0] = -1
    # ret 리스트의 첫 번째 요소를 -1로 지정
    for i in range(1, length):
        # 첫 번째 요소를 제외한 리스트의 길이만큼 반복
        if arr[i] > arr[i - 1]:
            # 만약 현재 배열의 요소가 전 배열의 요소보다 크다면
            ret[i] = INC
        # INC 마킹
        elif arr[i] < arr[i - 1]:
            # 만약 현재 배열의 요소가 전 배열의 요소보다 작다면
            ret[i] = DEC
            # DEC 마킹
    return ret  # 마킹된 ret 리스트를 반환


# 01010101 식으로 마킹 될 것임.


# 3번째로 사용될 함수
def func_c(arr):
    # 인수로 지그재그 배열의 길이를 저장하고 있는 리스트를 전달받음
    ret = max(arr)
    # 전달받은 리스트 중 제일 큰 값을 ret에 저장
    if ret == 2:
        return 0
        # 만약 지그재그 배열의 최대 길이가 2라면 0 반환
        # 문제상에서 3 이상의 길이부터 인정한다고 기재되어있음.
    return ret
    # 아니라면 저장되어 있는 값 그대로 반환


def solution(S):
    check = func_b(S)
    dp = func_a(check)
    answer = func_c(dp)
    return answer


# # 2
# 위 #1 을 바탕으로 했을 때 2293번의 문제 핵심은 다음과 같다.

# '가치의 합이 k원이 되는 경우의 수'를 구하는 전체의 문제를, '가치의 합이 i (1 ≤ i ≤ k)원이 되는 경우의 수'를 구하는 부분 문제로 나눈다. 추가적으로 부분 문제를 더욱 세부적으로 나눌 것인데, '특정 동전을 썼을 때 가치의 합이 i원이 되는 경우의 수'를 구하는 부분 문제로 나눈다.
# 위에서 언급한 부분 문제들을 해결해나가며 메모이제이션을 할 것인데, 시간 제한이 0.5초이며 메모리 제한도 4MB밖에 되지 않기 때문에 하나의 리스트 안에서 덮어 씌우는 식으로 빠르게 해결해나가야 한다.
# 입출력 예시로 주어진 경우 말고도 다른 예시를 생각해보며 테스팅해봐야 한다.


# 라인 별 풀이
# (1) line 2

# 코인의 종류를 오름차순으로 정렬해야 할 줄 알았는데 정렬하지 않고 동작시켜도 문제가 없었다.


# (2) line 3

# 합이 i원이 되는 경우의 수를 구하기 위해 리스트 dp에 0을 k+1개 초기화한다. dp[1]은 합이 1원이 되는 경우의 수, dp[2]는 합이 2원이 되는 경우의 수,... , dp[k]는 합이 k원이 되는 경우의 수이다.


# (3) line 4

# dp[0]은 위 논리에 따라 '합이 0원이 되는 경우의 수'가 아니다. 이건 아래에 더 자세히 기술하겠다.


# (4) line 6

# 첫 번째 for문에서는 각 코인의 종류를 전부 순회한다. 입출력 예시의 경우, 1원 - 2원 - 5원 순으로 순회한다.


# (5) line 7

# dp를 순회하며 특정 가치를 가진 동전을 썼을 때 합이 j원이 되는 경우의 수가 있다면 리스트 dp에 기록하기 위한 for문이다. 만약 동전이 3원짜리라면 dp[1], dp[2]는 고려할 필요가 없으므로 dp[3]부터 순회한다.


# (6) line 8, 9

# 이건 코드를 실행하는 과정을 캡처한 후 설명하는 것이 더 편할 것 같다.


# 먼저 동전 1원일 때를 생각해보자 (i = 1). j는 i부터 시작하므로 가장 처음 나오는 j는 1이다. j - i는 1 - 1이므로 0과 같다. 조건문의 조건에 만족하므로 dp[1] = dp[1] + dp[0]이 된다. dp[1] = 0 + 1이 되는데, 이처럼 동전이 딱 하나만 쓰일 때 dp[0]에 할당해놓은 1을 이용한다. 이것이 line 4에서 설명하지 못한 부분이다. 계속 j가 늘어나도 조건문의 조건 'j - i >= 0'이 만족하므로 dp[j]에 dp[j] + dp[j-i] 값이 덮어 씌워진다.


# 문제는 2원짜리 동전부터다 (i = 2). j는 2부터 시작하며 j - i = 0이므로 조건문의 조건에 만족한다. 그에 따라 dp[2] = dp[2] + dp[0] = 1 + 1이 된다. 이것 또한 2원짜리 동전을 하나만 쓰는 경우를 추가하기 때문에 dp[0]에 할당된 1을 이용했다. dp[3]은 dp[3] + dp[1] 인데, 이 얘기는 '1원짜리 동전으로 3원의 합을 만든 경우의 수(1+1+1)' + '1원짜리 동전으로 1원의 합을 만든 경우에 2를 더해서 만든 경우의 수(1+2)'라는 것이다.


# 설명이 복잡해 보일 수 있는데, 이러한 과정을 5원짜리 동전까지 모두 마치면 다음과 같은 리스트가 완성된다. (눈이 너무 아파서 대충 했는데 오타가 있어도 이해해주시고 알고리즘의 흐름을 중점적으로 봐주셨으면 합니다.)


# (7) line 10

# 합이 k원이 되는 경우의 수를 의미하는 dp[k]를 출력한다.
