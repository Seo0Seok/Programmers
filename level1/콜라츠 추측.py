def solution(num):
    answer = 0
    while True:
        if num == 1:
            break
        elif answer > 500:
            return -1
        
        if num % 2 == 0:
            num //= 2
            answer += 1
        else: 
            num = (num * 3) + 1
            answer += 1
    
    return answer