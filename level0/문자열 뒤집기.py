def solution(my_string, s, e):
    if s > 0:
        answer = my_string[:s] + my_string[e:s-1:-1] + my_string[e+1:]
    else:
        answer = my_string[e::-1] + my_string[e+1:]
    return answer

my_string = "Stanley1yelnatS"
s = 0
e = 10

print(solution(my_string, s, e))

