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
n, m = map(int, input().split(" "))
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
r, g, b = map(int, input().split(" "))
cnt = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            cnt += 1
            print(i, j, k)
print(cnt)

# 1085 : [기초-종합] 소리 파일 저장용량 계산하기
# h, b, c, s 가 공백을 두고 입력된다.
# h는 48,000이하, b는 32이하(단, 8의배수), c는 5이하, s는 6,000이하의 자연수이다.
h, b, c, s = map(int, input().split(" "))
sum = h * b * c * s
result = sum / (8 * (2 ** 20))
print("%0.1f MB" %result)

h, b, c, s = map(int, input().split(" "))
print('%0.1f MB' % (h * b * c * s / 1024 / 1024 / 8))
