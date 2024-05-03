def solution(n):
    answer = []
    for i in range(2, n+1):
        while n % i == 0:
            n = n // i
            if i not in answer:
                answer.append(i)
    return answer

n = 12

print(solution(n))