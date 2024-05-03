def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))

num_list = [-1, 2, 5, 6, 3]
print(solution(num_list))