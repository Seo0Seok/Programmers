def solution(num_list, n):
    answer = []
    i = 0
    for _ in range(len(num_list)//n):
        answer.append(num_list[i:n+i])
        i += n
    return answer
num_list = [100, 95, 2, 4, 5, 6, 18, 33, 948]
n = 3

# # answer = [[0] * n] * len(num_list)
# answer = []
# answer.append(num_list[:2])


print(solution(num_list, n))