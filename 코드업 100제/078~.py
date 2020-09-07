# 1078 : [기초-종합] 짝수 합 구하기
a = int(input())
n = 0
for i in range(1, a + 1):
    if i % 2 == 0:
        n += i
print(n)