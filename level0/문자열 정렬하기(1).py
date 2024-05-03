def solution(my_string):
    answer = []
    for i in my_string:
        if i.isnumeric():
            answer.append(int(i))
            
    return sorted(answer)

my_string = "p2o4i8gj2"
print(solution(my_string))