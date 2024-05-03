def solution(str_list):
    answer = []
    for idx, i in enumerate(str_list):
        print(idx, i)
        if i == 'l':
            print('1')
            return str_list[:idx]
        elif i == 'r':
            print('2')
            return str_list[idx+1:]
        else:
            pass
    return answer

str_list = ["u", "u", "l", "r"]
str_list2 = ["u", "r", "l", "u"]
str_list3 = ["l"]

print(solution(str_list))
print(solution(str_list2))
print(solution(str_list3))