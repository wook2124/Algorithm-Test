# 4673번 : 셀프 넘버
natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):       # i = 850       
    for j in str(i):            # j = "8", "5", "0"
        i += int(j)             # 850 + 8 + 5+ 0, i = 863
    generated_num.add(i)        # 생성자가 있는 숫자들

self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i)

'''
natural_number_set = set(range(1, 1001))
generated_number_set = set()

for i in range(1, 1001):
    print('currnet i = ' + str(i))
    for j in str(i):
        print('currnet j = ' + str(j))
        i += int(j)
    print('**managed num = ' + str(i))
    generated_number_set.add(i)
    print()

print(generated_number_set)
print(natural_number_set)

self_numbers_set = natural_number_set - generated_number_set
print(sorted(self_numbers_set))
'''