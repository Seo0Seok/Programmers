def solution(a, b, c, d):
    answer = 0
    list2 = [a, b, c, d]
    temp = {a, b, c, d}

    if len(temp) == 1:
        p = list(temp)[0]
        x = list2.count(p)
    elif len(temp) == 2:
        p = list(temp)[0]
        q = list(temp)[1]
        x = list2.count(p)
        y = list2.count(q)
    else: 
        p = list(temp)[0]
        q = list(temp)[1]
        r = list(temp)[2]
        x = list2.count(p)
        y = list2.count(q)
        z = list2.count(r)

    if len(temp) == 1:
        answer = 1111 * p

    elif len(temp) == 2:
        if x == 3 or y == 3:    
            if x > y:
                answer = (10 * p + q) ** 2
            elif x < y:
                answer = (10 * q + p) ** 2

        elif x == 2 and y == 2:
            answer = (p + q) * abs(p - q)
    
    elif len(temp) == 3:
        if x == 2 and y == 1 and z == 1:
            answer = q * r
        elif x == 1 and y == 2 and z == 1:
            answer = p * r
        elif x == 1 and y == 1 and z == 2:
            answer = p * q
    
    else:
        answer = min(list2)

    return answer

# print(solution(2,2,2,2))
# print(solution(4,1,4,4))
# print(solution(6,3,3,6))
# print(solution(2,5,2,6))
# print(solution(6,4,2,5))
print(solution(1,2,2,3))
