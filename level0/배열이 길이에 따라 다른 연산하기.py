def solution(arr, n):
    for i in range(len(arr)):
        if len(arr) % 2 == 0:
            if i % 2 == 1:
                arr[i] += n 
            
        elif len(arr) % 2 == 1:
            if i % 2 == 0:
                arr[i] += n 
            
    return arr

arr = [444, 555, 666, 777]
n = 100

print(solution(arr, n))