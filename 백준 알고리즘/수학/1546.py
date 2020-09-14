# 1546번 : 평균
n = int(input())                            # n = 3
score = list(map(float, input().split()))   # score = [40.0, 80.0, 60.0]

max = 0
for i in range(n):
    if max < score[i]:
        max = score[i]

for i in range(n):
    score[i] = (score[i] / max) * 100       # score 초기화
                                            # score = [50.0, 100.0, 75.0]
sum = 0
for i in range(n):
    sum += score[i]                         # sum = 225.0

print(sum / n)