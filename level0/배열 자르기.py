def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer

numbers = [1,2,3,4,5]

print(solution(numbers, 1,3))