def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:
            answer += my_string[i]    
    return answer

my_string = "apporoograpemmemprs"
indices = [1, 16, 6, 15, 0, 10, 11, 3]
print(solution(my_string, indices))