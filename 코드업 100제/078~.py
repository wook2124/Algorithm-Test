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
