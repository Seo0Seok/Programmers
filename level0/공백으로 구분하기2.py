def solution(my_string):
    my_string = my_string.split(' ')
    answer = []
    for i in my_string:
        if i != '':
            answer.append(i)
        
    return answer

my_string = "    programmers  "

print(solution(my_string))