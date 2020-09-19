# 8958번 : OX퀴즈
t = int(input())

for _ in range(t):
    ox = input()
    score = 0
    cnt = 0
    for i in range(len(ox)):
        if ox[i] == "O":
            cnt += 1
            score += cnt
        elif ox[i] == "X":
            cnt = 0
    print(score)