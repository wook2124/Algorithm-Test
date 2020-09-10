# 1093 : [기초-1차원배열] 이상한 출석 번호 부르기1
# 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
# 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.
a = int(input())             # 정수 10이 입력됨
b = input().split()          # 두 번째 줄, 1 3 2 2 5 6 7 4 5 9 입력
ls = []

for i in range(24):
    ls.append(0)             # list에 0을 23개 추가함
for i in range(a):           # a = 10이 입력되어 i = 0 ~ 9
    ls[int(b[i])] += 1       # int(b[0]) = ls[1] = 0에 해당 따라서 + 1 되어 1 입력
for i in range(1, 24):       # ls[1]부터 ls[23]까지 입력된 수를 한 칸 띄고 출력
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


# 1096 : [기초-2차원배열] 바둑판에 흰 돌 놓기
# 바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력된다.
# 둘째 줄 부터 n+1 번째 줄까지 힌 돌을 놓을 좌표(x, y)가 n줄 입력된다.
# n은 10이하의 자연수이고 x, y 좌표는 1 ~ 19 까지이며, 같은 좌표는 입력되지 않는다.
# 흰 돌이 올려진 바둑판의 상황을 출력하고 흰 돌이 있는 위치는 1, 없는 곳은 0으로 출력한다.

# 바둑판 준비 1
m = [
    [0] * 19                        # [] * 19 = 가로로 19개
    for i in range(19)              # range(19) = 세로로 19개
]                                   # 0 ~ 18로 19개의 0이 가로, 세로로 생김

# 바둑판 입력 1
n = int(input())                    # n = 5를 입력받음
for i in range(n):                  # i = 0 ~ 4
    x, y = map(int, input().split())# x, y는 각각 1 1, 2 2, 3 3, 4 4, 5 5 입력받음
    m[x - 1][y - 1] = 1             # m[0][0], ...,  m[4][4]에 1이 찍힘 (m은 0부터 입력됨)

# 바둑판 출력 1
for i in range(19):                 # i = 0 ~ 18
    for j in range(19):             # j = 0 ~ 18
        print(m[i][j], end = " ")   # m[0][0]부터 m[18][18]까지 한 칸 띄고 출력
    print()                         # m[0][18]출력 후 줄 바꾼 뒤 j for문 벗어나고 다시 m[1][0]출력


# 바둑판 준비 2
m = []                        # list 생성
for i in range(20):           # i = 0 ~ 19
    m.append([])              # [ ]안에 []를 생성함 = [[]]
    for j in range(20):       # j = 0 ~ 19 (i가 0일때 20번, 1일때 20번)
        m[i].append(0)        # i = 0, j = 0인 경우 = [[0]]
                              # i = 0, j = 1인 경우 = [[0, 0]] 이런식으로 0이 추가됨  
                                 # i = 1, j = 19가 되면 = [[0, ..., 0]], [[0, ..., 0]]

# 바둑판 입력 2
n = int(input())              # n = 5를 입력받음
for i in range(n):            # i = 0 ~ 4
    x, y = map(int, input().split())    # x, y는 각각 1 1, 2 2, 3 3, 4 4, 5 5 입력받음
    m[x][y] = 1               # m[1][1], ..., m[5][5]에 1이 찍힘

# 바둑판 출력 2
for i in range(1, 20):           # i = 1 ~ 19     
    for j in range(1, 20):       # j = 1 ~ 19
        print(m[i][j], end=" ")  # m[1][1]부터 m[19][19]까지 한 칸 띄고 출력
    print()                      # m[1][19]출력 후 줄 바꾼 뒤 j for문 벗어나고 다시 m[2][1]출력


# 1097 : [기초-2차원배열] 바둑알 십자 뒤집기
# 바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
# 십자 뒤집기 횟수(n)가 입력된다.
# 십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.

# 바둑판 준비
board = [
    [0] * 20                        # [] * 20 = 가로로 20개
    for j in range(20)              # range(20) = 세로로 20개
]

# 바둑판 입력
for i in range(0, 19):              # i = 0 ~ 18
    n = input().split()             # 0 0 .. 1 0 1 0 .. 0 0
    board[i] = list(map(int, n))
    #print()

# 입력 반복
repeat = int(input())               # repaet = 2
for i in range(0, repeat):          # i = 0 ~ 1
    temp = input().split()          # temp = 10 10, 12 12
    point = list(map(int, temp))    # 10과 12를 list로 묶음, [10, 12]
    x = point[0]-1                  # x = point[0] - 1 = 9
    y = point[1]-1                  # y = point[1] - 1 = 11

    # 가로(width)
    for j in range(0, 19):          # j = 0 ~ 18
        if board[x][j] == 0:        # board[9][0] == 0이면
            board[x][j] = 1         # board[9][0] = 1로 바꿔줌
        else:
            board[x][j] = 0         # 아닌경우 그대로 0

    # 세로(cols)
    for k in range(0, 19):
        if board[k][y] == 0:
            board[k][y] = 1
        else:
            board[k][y] = 0

# 바둑판 출력
for i in range(0, 19):
    for j in range(0, 19):
        print(board[i][j], end = " ")
    print()
