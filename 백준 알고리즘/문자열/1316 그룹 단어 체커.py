# 1316번 : 그룹 단어 체커
t = int(input())
group_word = 0

for _ in range(t):
    word = input()
    for i in range(len(word)):
        if i != len(word) - 1:
            if word[i] == word[i + 1]:
                pass
            elif word[i] in word[i + 1:]:
                break
        else:
            group_word += 1

print(group_word)