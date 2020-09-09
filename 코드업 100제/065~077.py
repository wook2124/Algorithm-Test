# 1065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기
a, b, c = map(int, input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

# 1066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기
a, b, c = map(int, input().split())
if a % 2 == 0:
    print("even")
else:
    print("odd")
if b % 2 == 0:
    print("even")
else:
    print("odd")
if c % 2 == 0:
    print("even")
else:
    print("odd")

# 1067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분석하기
# 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.
a = int(input())
if a < 0:
    print("minus")
else:
    print("plus")
if a % 2 == 0:
    print("even")
else:
    print("odd")

# 1068 : [기초-조건/선택실행구조] 정수 1개 입력받아 평가 출력하기
# 점수 범위 : 평가
# 90 ~ 100 : A
# 70 ~   89 : B
# 40 ~   69 : C
#  0 ~   39 : D
a = int(input())
if a >= 90:
    print("A")
elif a >= 70:
    print("B")
elif a >= 40:
    print("C")
else:
    print("D")

# 1069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기
# 평가 : 내용
# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?
a = input()
if a == "A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a =="D":
    print("slowly~")
else:
    print("what?")

# 1070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기
# 월 : 계절 이름
# 12, 1, 2 : winter
#  3, 4, 5 : spring
#  6, 7, 8 : summer
#  9, 10, 11 : fall
a = int(input())
if a in(12, 1, 2):
    print("winter")
elif a in(3, 4, 5):
    print("spring")
elif a in(6, 7, 8):
    print("summer")
else:
    print("fall")

# 1071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기1
a = input().split()
num = list(map(int, a))
for i in num:
    if i == 0:
        break
    else:
        print(i)

a = list(map(int, input().split()))
for i in a:
    if i == 0:
        exit()
    else: 
        print(i)

# 1072 : [기초-반복실행구조] 정수 입력받아 계속 출력하기
n = int(input())
a = list(map(int, input().split()))
for i in a:
    print(i)

# 1073 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기2
a = input().split()
num = list(map(int, a))
for i in num:
    if i == 0:
        break
    else:
        print(i)

# 1074 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1
a = int(input())
for i in range(a):
    print(a - i)

# 1075 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2
a = int(input())
for i in range(a):
    print(a - i - 1)

# 1076 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기
f = ord(input())  # f문자를 102 아스키 코드로 바꿔줌
a = 97            # a문자는 97 아스키 코드 
while(f + 1 > a): # 103 > 97, 즉 97(a) 98(b) 99(c) 100(d) 101(e) 102(f)까지 출력
    print(chr(a), end=" ") # end=" "로 출력값마다 공백주기
    a += 1

# 1077 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기
a = int(input())
n = 0
while(a + 1 != n):
    print(n)
    n += 1