def solution(num1, num2):
    answer = lambda num1, num2 : num1 / num2
    return int(answer(num1, num2) * 1000)

print(solution(3, 2))