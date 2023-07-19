genres = input().split()
plays = map(int, input().split())
answer = []
music_play = dict()

# 장르별로 play 횟수
for k, v in zip(genres, plays):
    music_play[k] = music_play.get(k, 0) + int(v)

    # play 횟수 내림차순으로 정렬
play_list = sorted(music_play.items(), key=lambda x: x[1], reverse=True)

# 많이 재생된 장르 순으로 for문 돌리기
for l, cnt in play_list:
    arr = []
    # 재생횟수와 고유번호 넣어주기
    for idx, (g, p) in enumerate(zip(genres, plays)):
        if g == l:
            arr.append([p, idx])

        # 조건 2,3 을 고려한 정렬
    arr = sorted(arr, key=lambda x: (x[0], -x[1]), reverse=True)

    for i in range(min(len(arr), 2)):
        answer.append(arr[i][1])
print(answer)
