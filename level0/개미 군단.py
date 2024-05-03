def solution(hp):
    
    a1 = hp // 5 
    a2 = hp % 5

    b1 = a2 // 3
    b2 = a2 % 3

    c1 = b2 // 1

    return a1 + b1 + c1

hp = 999
print(solution(hp))