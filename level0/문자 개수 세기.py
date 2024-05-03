def solution(my_string):
    answer = [0] * 52
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    alpha_list = list(alpha)

    for i in my_string:
        answer[alpha_list.index(i)] += 1
    return answer

my_string = "Programmers"

print(solution(my_string))