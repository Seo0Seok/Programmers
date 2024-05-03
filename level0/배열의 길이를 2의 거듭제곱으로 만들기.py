def solution(arr):
    i = 0
    while(len(arr) != (2**i)):
        if len(arr) < (2**i):
            for _ in range(2**i - len(arr)):
                arr += [0]
            break
        else:
            i += 1
    return arr
        
        


arr = [1, 2, 3, 4, 5, 6]
arr2 = [58, 172, 746, 89]
print(solution(arr))
