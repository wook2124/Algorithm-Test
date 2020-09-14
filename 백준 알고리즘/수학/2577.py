# 2577번 : 숫자의 개수
a = int(input())                # 150
b = int(input())                # 266
c = int(input())                # 427
result = list(str(a * b * c))   # [1, 7, 0, 3, 7, 3, 0, 0]

for i in range(10):             # i = 0 ~ 9
    print(result.count(str(i))) # i를 문자열(str)로 바꿔서 몇 개 있는지 count함