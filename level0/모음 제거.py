def solution(my_string):
    delete = ['a', 'e', 'i', 'o', 'u']
    for str in my_string:
        for delete2 in delete:
            if str == delete2:
                my_string = my_string.replace(delete2,"")
                
    return my_string

my_string = "nice to meet you"
my_string = "bus"

print(solution(my_string))