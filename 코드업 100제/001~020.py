# https://codeup.kr/problemset.php?search=%EA%B8%B0%EC%B4%88100%EC%A0%9C

# 1001 : [기초-출력] 출력하기01
print("Hello")

# 1002 : [기초-출력] 출력하기02
print("Hello World")

# 1003 : [기초-출력] 출력하기03
print("Hello\nWorld")

# 1004 : [기초-출력] 출력하기04
print("'Hello'")

# 1005 : [기초-출력] 출력하기05
print("\"Hello World\"")

# 1006 : [기초-출력] 출력하기06
print("\"!@#$%^&*()\"")

# 1007 : [기초-출력] 출력하기07
print("\"C:\Download\hello.cpp\"")

# 1008 : [기초-출력] 출력하기08
print("\u250C\u252C\u2510\n\u251C\u253C\u2524\n\u2514\u2534\u2518")

# 1010 : [기초-입출력] 정수 1개 입력받아 그대로 출력하기
a = int(input())
print(a)

# 1011 : [기초-입출력] 문자 1개 입력받아 그대로 출력하기
a = str(input())
print(a)

# 1012 : [기초-입출력] 실수 1개 입력받아 그대로 출력하기
a = float(input())
print(a)

# 1013 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기
a= input()
print(a)

# 1014 : [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기
a, b = input().split()
print(b, a)

# 1015 : [기초-입출력] 실수 입력받아 둘째 자리까지 출력하기
a = float(input())
print('%.2f' %a)

# 1017 : [기초-입출력] 정수 1개 입력받아 3번 출력하기
a = int(input())
print(a, a, a)

# 1018 : [기초-입출력] 시간 입력받아 그대로 출력하기
h, m = map(int, input().split(':'))
print('%d:%d' %(h, m))

t = input()
print(t)

# 1019 : [기초-입출력] 연월일 입력받아 그대로 출력하기
y, m, d = map(int, input().split('.'))
print('%04d.%02d.%02d' %(y, m, d))

# 1020 : [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기
a, b = input().split('-')
print(a + b)