def solution(n):
    answer = 0
    check = []
    while n != 0:
        if n % 3 == 0:
            check.append(0)
        else:
            check.append(n%3)
        n //= 3 
        
    for i in range(len(check)):
        answer += check[i] * (3 ** (len(check) - 1 - i))

    return answer

n = 125
print(solution(n))