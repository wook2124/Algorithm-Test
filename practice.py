import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
li = []

for _ in range(n):
    li.append(list(map(int, input().split())))

print(n)
print(li)