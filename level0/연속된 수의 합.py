def solution(num, total):
    answer = []
    a = 0
    
    for i in range(num):
        a += i
    
    first = (total - a) // num

    for i in range(num):
        answer.append(first+i)
    
    return answer


num = 5
total = 5

print(solution(num, total))