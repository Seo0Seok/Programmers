def solution(my_string):
    answer = 0
    for i in my_string:
        if i not in "1234567890":
            my_string = my_string.replace(i, " ")
    
    for j in my_string.split():
        answer += int(j)

    return answer

my_string = "1a2b3c4d123Z"
print(solution(my_string))