def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 0:
        return [-1]
    return arr

arr = [10]
print(solution(arr))