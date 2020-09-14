# 11720번 : 숫자의 합
n = int(input())    # 5
a = list(input())   # [5, 4, 3, 2, 1]
sum = 0

for i in a:         # i = 5, 4, 3, 2, 1
    sum += int(i)

print(sum)