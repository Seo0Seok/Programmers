def solution(num_list):
    answer = 0
    idx = 0
    fin = -1
    for i in num_list:
        
        if i < 0:
            fin = idx
            break
        idx += 1
        
    return fin

num_list = [12, 4, 15, 46, 38, -2, 15]
print(solution(num_list))