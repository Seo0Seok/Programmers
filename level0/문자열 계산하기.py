def solution(my_string):
    answer = ""
    listt = []
    k = 0
    result = 0
    my_string = my_string.split()
    for i in my_string[1:]:
        answer += i
    for j in range(len(answer) // 2):
        listt.append(int(answer[k:2+k]))
        k += 2
    return int(my_string[0]) + sum(listt)

my_string = "3 + 4 - 7"
# my_string = my_string.replace(' - ', ' + -').split(' + ')
my_string = my_string.replace(' ', '')
print(my_string)
# print(solution(my_string))