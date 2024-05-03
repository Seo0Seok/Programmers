def solution(arr):
    for i in range(len(arr)):    
        if len(arr[i]) > len(arr):
            for _ in range(len(arr[i]) - len(arr)):
                arr.append([0] * len(arr[i]))
            return arr
        elif len(arr[0]) < len(arr):
            for _ in range(len(arr) - len(arr[0])):
                for k in range(len(arr)):
                    arr[k].append(0)    
            return arr    
        else:
            return arr   
    

arr1 = [[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]
arr2 = [[57, 192, 534, 2], [9, 345, 192, 999]]
arr3 = [[1, 2], [3, 4]]
arr4 = [[1, 1], [1, 1], [1, 1], [1, 1]]

print(solution(arr1))
print(solution(arr2))
print(solution(arr3))
print(solution(arr4))