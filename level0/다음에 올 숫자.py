def solution(common):
    check1 = []
    check2 = []

    for i in range(1, 3):
        check1.append(common[i] - common[i-1])

    if len(set(check1)) == 1:
        return common[-1] + check1[0]
    else:
        for i in range(1, 3):
            check2.append(common[i] // common[i-1])
        return common[-1] * check2[0]
    

    # return answer

common = [-1, 2, -4]
print(solution(common))