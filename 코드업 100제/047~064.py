# 1047 : [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기
a = int(input())
print(a << 1)

a = input()
print(a * 2)

# 1048 : [기초-비트시프트연산] 한 번에 2의 거듭제곱 배로 출력하기
a, b = map(int, input().split())
print(a << b)

a, b = map(int, input().split())
print(a * (2 ** b))

# 1049 : [기초-비교연산] 두 정수 입력받아 비교하기1
'''
두 정수(a, b)를 입력받아 a가 b보다 크면 1을, a가 b보다 작거나 같으면 0을 출력하는 프로그램을 작성해보자.
'''
a, b = map(int, input().split())
if a > b:
    print(1)
else: 
    print(0)

# 1050 : [기초-비교연산] 두 정수 입력받아 비교하기2
'''
두 정수(a, b)를 입력받아 a와 b가 같으면 1을, 같지 않으면 0을 출력하는 프로그램을 작성해보자.
'''
a, b = map(int, input().split())
if a == b:
    print(1)
else:
    print(0)

# 1051 : [기초-비교연산] 두 정수 입력받아 비교하기3
'''
두 정수(a, b)를 입력받아 b가 a보다 크거나 같으면 1을, 그렇지 않으면 0을 출력하는 프로그램을 작성해보자.
'''
a, b = map(int, input().split())
if b >= a:
    print(1)
else:
    print(0)

# 1052 : [기초-비교연산] 두 정수 입력받아 비교하기4
'''
두 정수(a, b)를 입력받아 a와 b가 서로 다르면 1을, 그렇지 않으면 0을 출력하는 프로그램을 작성해보자.
'''
a, b = map(int, input().split())
if a != b:
    print(1)
else:
    print(0)

# 1053 : [기초-논리연산] 참 거짓 바꾸기
a = int(input())
if a == 1:
    print(0)
else:
    print(1)

# 1054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기
a, b = map(int, input().split())
if a == 1 and b == 1:
    print(1)
else:
    print(0)

# 1055 : [기초-논리연산] 하나라도 참이면 참 출력하기
a, b = map(int, input().split())
if a ==1 or b == 1:
    print(1)
else:
    print(0)

# 1056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기
a, b = map(int, input().split())
if a != b:
    print(1)
else:
    print(0)

# 1057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기
a, b = map(int, input().split())
if a == b:
    print(1)
else:
    print(0)

# 1058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기
a, b = map(int, input().split())
if a == 0 and b == 0:
    print(1)
else:
    print(0)

# 1059 : [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기
a = int(input())
print(~a)

# 1060 : [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기
a, b = map(int, input().split())
print(a & b)

# 1061 : [기초-비트단위논리연산] 비트단위로 OR 하여 출력하기
a, b = map(int, input().split())
print(a | b)

# 1062 : [기초-비트단위논리연산] 비트단위로 XOR 하여 출력하기
a, b = map(int, input().split())
print(a ^ b)

# 1063 : [기초-삼항연산] 두 정수 입력받아 큰 수 출력하기
a, b = map(int, input().split())
print(a if a > b else b)

# 1064 : [기초-삼항연산] 정수 3개 입력받아 가장 작은 수 출력하기
a, b, c = map(int, input().split()) # 3, -1, 5
m = a if a < b else b
print(m if m < c else c)