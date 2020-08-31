# 1021 : [기초-입출력] 단어 1개 입력받아 그대로 출력하기
a = input()
print(a)

# 1022 : [기초-입출력] 문장 1개 입력받아 그대로 출력하기
a = input()
print(a)

# 1023 : [기초-입출력] 실수 1개 입력받아 부분별로 출력하기
a, b = map(int, input().split('.'))
print('%d\n%d' %(a, b))

a, b = input().split('.')
print(a + "\n" + b)

# 1024 : [기초-입출력] 단어 1개 입력받아 나누어 출력하기
a = input()
for i in range(len(a)) :
    print("'" + a[i] + "'")

a = input()
for i in a :
    print("'" + i + "'")

# 1025 : [기초-입출력] 정수 1개 입력받아 나누어 출력하기
a = input()
for i in range(len(a)):
    x = int(a[i])
    n = (len(a)-i-1)
    print([x*(10**n)])   

a, b, c, d, e = map(int, input())
print('[%d0000]\n[%d000]\n[%d00]\n[%d0]\n[%d]' %(a, b, c, d, e))

# 1026 : [기초-입출력] 시분초 입력받아 분만 출력하기
a, b, c = map(int, input().split(':'))
print(b)

# 1027 : [기초-입출력] 년월일 입력받아 형식 바꿔 출력하기
y, m, d = map(str, input().split("."))
print(d + "-" + m + "-" + y)

y, m, d = map(int, input().split('.'))
print('%02d-%02d-%04d' %(d, m, y))

# 1028 : [기초-데이터형] 정수 1개 입력받아 그대로 출력하기2
a = input()
print(a)

# 1029 : [기초-데이터형] 실수 1개 입력받아 그대로 출력하기2
a = float(input())
print('%.11f' %a)

# 1030 : [기초-데이터형] 정수 1개 입력받아 그대로 출력하기3
a = input()
print(a)

# 1031 : [기초-출력변환] 10진 정수 1개 입력받아 8진수로 출력하기
a = int(input())
print('%o' %a)

# 1032 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기1
a = int(input())
print('%x' %a)

# 1033 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기2
a = int(input())
print('%X' %a)

# 1034 : [기초-출력변환] 8진 정수 1개 입력받아 10진수로 출력하기
a = int(input(), 8)
print('%d' %a)

# 1035 : [기초-출력변환] 16진 정수 1개 입력받아 8진수로 출력하기
a = int(input(), 16)
print('%o' %a)

# 1036 : [기초-출력변환] 영문자 1개 입력받아 10진수로 출력하기
a = input()
print(ord(a))