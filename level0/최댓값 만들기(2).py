def solution(numbers):
    answer = 0
    minus_cnt = 0
    numbers.sort()

    for i in numbers:
        if i < 0:
            minus_cnt += 1
    
    if minus_cnt <= 1:
        answer = numbers[-1] * numbers[-2]
    else:
        answer = max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
        
    return answer

numbers = [-30, -20, -10, 5, 5, 20, 5]

print(solution(numbers))