def solution(num1, num2):
    answer = lambda *x:sum(x)
    return answer(num1, num2)

print(solution(15,5))