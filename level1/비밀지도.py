def solution(n, arr1, arr2):
    answer = []
    
    for x, y in zip(arr1, arr2):
        z = format((x | y), 'b').zfill(n)
        answer.append(z.replace('1', '#').replace('0', ' '))
    
    return answer

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))

# print(type(int(bin(9))))