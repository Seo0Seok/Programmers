def solution(l, r):
    answer = [str(i) for i in range(l, r+1)]
    result = []
    cnt = 0

    for i in "12346789":
        for j in range(len(answer)):
            if i in answer[j]:
                answer[j] = "delete"

    for k in answer:
        if k != "delete":
            result.append(int(k))
    
    result.sort()

    if len(result) == 0:
        return [-1]
    
    return result
        
    

l = 3
r = 99999


print(solution(l, r))