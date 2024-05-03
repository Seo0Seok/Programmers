num_list = [1,2,3,4,5]

# def solution(num_list):
#     answer = []
#     for i in range(len(num_list)):
#         answer.append(num_list[-(i+1)])
#     return answer

# def solution(num_list):
#     return num_list[::-1]

def solution(num_list):
    num_list.reverse()
    return num_list

print(solution(num_list))

