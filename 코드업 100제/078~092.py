# 1078 : [기초-종합] 짝수 합 구하기
a = int(input())
n = 0
for i in range(1, a + 1):
    if i % 2 == 0:
        n += i
print(n)

# 1079 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기
a = input().split()
for i in a:
    print(i)
    if i == "q":
        break

# 1080 : [기초-종합] 언제까지 더해야 할까?
a = int(input())
n = 0
for i in range(a + 1):
    n += i
    if n >= a:
        print(i)
        break

# 1081 : [기초-종합] 주사위를 2개 던지면?
n, m = map(int, input().split())
for i in range(1, n + 1):
    for j in range (1, m + 1):
        print(i, j)

# 1082 : [기초-종합] 16진수 구구단?
a = str(input())
b = int(a, 16)
for i in range(1, 16):
    print("%s*%X=%X" %(a, i, b*i))

# 1083 : [기초-종합] 3 6 9 게임의 왕이 되자!
a = int(input())
for i in range(1, a + 1):
    if i % 3 != 0:
        print(i, end=" ")
    else:
        print("X", end=" ")

# 1084 : [기초-종합] 빛 섞어 색 만들기
r, g, b = map(int, input().split())
cnt = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            cnt += 1
            print(i, j, k)
print(cnt)

# 1085 : [기초-종합] 소리 파일 저장용량 계산하기
'''
h, b, c, s 가 공백을 두고 입력된다.
h는 48,000이하, b는 32이하(단, 8의배수), c는 5이하, s는 6,000이하의 자연수이다.
'''
h, b, c, s = map(int, input().split())
sum = h * b * c * s
result = sum / (8 * (2 ** 20))
print("%.1f MB" %result)

h, b, c, s = map(int, input().split())
print('%.1f MB' % (h * b * c * s / 1024 / 1024 / 8))

# 1086 : [기초-종합] 그림 파일 저장용량 계산하기
'''
w, h, b 가 공백을 두고 입력된다.
단, w, h는 모두 정수이고 1~1024 이다. b는 40이하의 4의 배수이다.
'''
w, h, b = map(int, input().split())
sum = w * h * b
result = sum / (8 * (2 ** 20))
print("%.2f MB" %result)

w, h, b = map(int, input().split())
print('%.2f MB' % (w * h * b / 1024 / 1024 / 8))

# 1087 : [기초-종합] 여기까지! 이제 그만~
a = int(input())
sum = 0
for i in range(1, a + 1):
    sum += i
    if sum >= a:
        print(sum)
        break

# 1088 : [기초-종합] 3의 배수는 통과?
a = int(input())
for i in range(1, a + 1):
    if i % 3 != 0:
        print(i, end=" ")
    else:
        continue

# 1089 : [기초-종합] 수 나열하기1
'''
시작 값(a), 등차의 값(d), 몇 번째 수 인지를 의미하는 정수(n)가 공백을 두고 입력된다.(모두 0 ~ 100)
'''
a, b, n = map(int, input().split())
for i in range(n - 1):
    a += b
print(a)

# 1090 : [기초-종합] 수 나열하기2
'''
시작 값(a), 등비의 값(r), 몇 번째 인지를 나타내는 정수(n)가 공백을 두고 입력된다.(모두 0 ~ 10)
'''
a, r, n = map(int, input().split())
for i in range(n - 1):
    a *= r
print(a)

# 1091 : [기초-종합] 수 나열하기3
'''
시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)가 공백을 두고 입력된다.(a, m, d는 -50 ~ +50, n은 10이하의 자연수)
'''
a, m, d, n = map(int, input().split())
for i in range(n - 1):
    a *= m
    a += d
print(a)

# 1092 : [기초-종합] 함께 문제 푸는 날
a, b, c = map(int, input().split())
day = 1
while day % a != 0 or day % b != 0 or day % c != 0:
    day += 1
print(day)