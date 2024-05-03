def solution(arr):
    cnt = 0
    flag = True
    
    while flag:
        temp = arr.copy()
        for idx, i in enumerate(arr):
            if i >= 50 and i % 2 == 0:
                arr[idx] = arr[idx] // 2
            elif i < 50 and i % 2 == 1:
                arr[idx] = arr[idx] * 2 + 1
        cnt += 1

        if temp == arr:
            flag = False
            return cnt - 1
        
arr = [1,2,3,100,99,98]

print(solution(arr))