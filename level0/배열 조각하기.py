def solution(arr, query):
    for idx, i in enumerate(query):
        if idx % 2 == 0:
            arr = arr[:i+1]
        else: 
            arr = arr[i:]
    return arr

arr = [0,1,2,3,4,5]
query = [4,1,2]

print(solution(arr, query))