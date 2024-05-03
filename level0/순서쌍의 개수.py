def solution(n):
    list1 = []
    for i in range(1, n+1):
        if n % i == 0:
            list1.append(i)
    answer = len(list1)
    return answer

print(solution(100))