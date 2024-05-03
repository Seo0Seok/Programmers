def solution(arr, idx):
    answer = 0
    for idx2, i in enumerate(arr):
        if idx2 >= idx and i == 1:
            return idx2
    return -1

arr = [1, 1, 1, 1, 0]
idx = 3

print(solution(arr,idx))