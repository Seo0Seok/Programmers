def solution(my_string, overwrite_string, s):
    
    a = list(my_string[0:s]) + list(overwrite_string) + list(my_string[s + len(overwrite_string):])
    my_string = ''.join(a)
    return my_string

my_string = "Program29b8UYP"
overwrite_string = "merS123"
s = 7

print(solution(my_string, overwrite_string, s))