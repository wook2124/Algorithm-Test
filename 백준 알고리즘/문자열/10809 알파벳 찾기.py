# 10809번 : 알파벳 찾기
from string import ascii_lowercase
L = list(ascii_lowercase)

s = input()
for i in range(len(L)):
    print(s.find(L[i]), end = " ")