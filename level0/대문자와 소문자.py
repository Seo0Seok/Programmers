def solution(my_string):
    answer = ''
    for i in my_string:
        if i.islower():
            i = i.upper()
            answer += i
        else:
            i = i.lower()
            answer += i
    return answer

my_string = "cccCCC"
my_string2 = "abCdEfghIJ"
print(solution(my_string2))