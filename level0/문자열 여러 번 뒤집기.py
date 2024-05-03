def solution(my_string, queries):
    for (a, b) in queries:
        my_string = my_string[:a] + my_string[a:b+1][::-1] + my_string[b+1:]
    return my_string

my_string = "rermgorpsam"
queries = [[2, 3], [0, 7], [5, 9], [6, 10]]

print(solution(my_string, queries))