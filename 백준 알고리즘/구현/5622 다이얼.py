# 5622번 : 다이얼
alphabet = input().lower()
dial = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
time = 0

for i in range(len(alphabet)):
    for j in dial:
        if alphabet[i] in j:
            time += dial.index(j) + 3

print(time)