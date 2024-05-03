def solution(lines):
    check = []
    check2 = []

    for i in lines:
        for j in range(min(i), max(i)+1):
            check.append(j)
        check2.append(check)
        check = []
    print(check2)
    # 교집합
    a = list(set(check2[0]) & set(check2[1]))
    b = list(set(check2[1]) & set(check2[2]))
    c = list(set(check2[0]) & set(check2[2]))

    a.sort()
    b.sort()
    c.sort()

    for z in [a, b, c]:
        if len(z) > 1:        
         check.append(z)
    print(check)
    if len(check) == 0:
        return 0
    elif len(check) == 1:
        return check[0][-1] - check[0][0]
    elif len(check) == 2:
        return abs(check[0][-1] - check[0][0]) + abs(check[1][-1] - check[1][0])
    elif len(check) == 3:    
        return max(map(max,check)) - min(map(min,check))
            
lines = [[0, 6], [0, 6], [2,4]]
print(solution(lines))