# 10814번 : 나이순 정렬
n = int(input())

ls = []
for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    ls.append((age, name))

# sort_ls = sorted(ls) 

print(sort_ls)