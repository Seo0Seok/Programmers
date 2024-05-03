def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex not in i:
            answer += i
    return answer

str_list = ["abc", "bbc", "cbc"]
ex = "c"
print(solution(str_list, ex))