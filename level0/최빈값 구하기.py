def solution(array):
    check = []
    
    for i in set(array):
        check.append(array.count(i))
    if check.count(max(check)) == 1:
        return list(set(array))[check.index(max(check))]
    else:
        return -1

    

array = [1]
print(solution(array))