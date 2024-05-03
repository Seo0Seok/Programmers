from math import prod

def solution(num_list):
    answer = 1
    if len(num_list) >= 11:
        return sum(num_list)
    elif len(num_list) <= 10:
        # for i in num_list:
        #     answer *= i
        # return answer
        return prod(num_list)

num_list = [2,3,4,5]
print(solution(num_list))