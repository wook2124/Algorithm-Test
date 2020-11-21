def solution(card_numbers):
    answer = []
    for test_numbers in card_numbers:
        if len(test_numbers) > 16:
            test_numbers = test_numbers.replace('-', '')

        sum_1 = 0 
        for i in range(0, 2, len(test_numbers) - 1):
            i = int(i)
            i *= 2
            num = 0
            if i > 9:
                num = (i // 10) + (i % 10)
            sum_1 += num

        sum_2 = 0
        for i in range(1, 2, len(test_numbers) - 1):
            i = int(i)
            sum_2 += i
            
        if (sum_1 + sum_2) % 10 == 0:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer