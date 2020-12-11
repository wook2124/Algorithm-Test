# 10039번 : 평균 점수
ans = []
for i in range(5):
    ans.append(int(input()))

result = []
for i in ans:
    if i < 40:
        result.append(40)
    else:
        result.append(i)

avg = sum(result) / len(result)

print(int(avg))