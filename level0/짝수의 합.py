def solution(n):
    list2 = []
    while True:
        
        if n <= 0:
            break
        if n % 2 == 0:
            list2.append(n)
        n -= 1

    answer = sum(list2)
    
    return answer

print(solution(5))