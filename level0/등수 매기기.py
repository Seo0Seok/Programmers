def solution(score):
    answer = []
    avg_list = []
    sort_list = []
    
    for i in score:
        avg_list.append(sum(i) / len(i))
    sort_list = sorted(avg_list, reverse=True)

    for j in range(len(avg_list)):
        answer.append(sort_list.index(avg_list[j]) + 1)    
    
    return answer
        
        
            



score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
print(solution(score))


