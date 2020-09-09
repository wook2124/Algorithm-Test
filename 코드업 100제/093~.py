# 1093 : [기초-1차원배열] 이상한 출석 번호 부르기1
# 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
# 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.
a = int(input())        # 정수 10이 입력됨
b = input().split()     # 두 번째 줄, 1 3 2 2 5 6 7 4 5 9 입력
ls = []

for i in range(24):
    ls.append(0)        # list마다 0을 23개 추가함
for i in range(a):      # 10이 입력되어 i = 0 ~ 9
    ls[int(b[i])] += 1  # int(b[0]) = ls[1] = 0에 해당 따라서 + 1 되어 1 입력
for i in range(1, 24):  # ls[1]부터 ls[23]까지 입력된 수를 한 칸 띄고 출력
    print(ls[i], end = " ")

# 1094 : [기초-1차원배열] 이상한 출석 번호 부르기2
# 번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
# n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.
a = int(input())
b = list(map(int, input().split()))

i = a - 1               # i = 10 - 1 = 9
while i >= 0:
    print(b[i], end = " ")
    i -= 1

a = int(input())
b = list(map(int, input().split()))

for i in reversed(b):   # reversed 함수는 list에서만 사용가능
    print(i, end = " ")

# 1095 : [기초-1차원배열] 이상한 출석 번호 부르기3
# 출석을 부른 번호 중에 가장 빠른 번호를 1개만 출력한다. (가장 작은 수 출력)
a = int(input())
b = list(map(int, input().split()))
print(min(b))
