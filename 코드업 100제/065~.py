# 1065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기
a, b, c = map(int, input().split(" "))
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

# 1066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기
a, b, c = map(int, input().split(" "))
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
# 평가 기준
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