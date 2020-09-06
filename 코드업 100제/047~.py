# 1047 : [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기
a = input()
print(a * 2)

a = int(input())
print(a << 1)

# 1048 : [기초-비트시프트연산] 한 번에 2의 거듭제곱 배로 출력하기
a, b = map(int, input().split(" "))
print(a * (2 ** b))

a, b = map(int, input().split(" "))
print(a << b)