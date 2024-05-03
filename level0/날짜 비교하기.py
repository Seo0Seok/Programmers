def solution(date1, date2):
    answer = 0
    for i in range(len(date1)):
        date1[i] = str(date1[i])
        date2[i] = str(date2[i])

    date1 = ''.join(date1)
    date2 = ''.join(date2)
    
    if int(date2) > int(date1):
        answer = 1

    return answer

date1 = [1024, 10, 24]
date2 = [1024, 10, 24]

print(date1 < date2)
# print(solution(date1, date2))