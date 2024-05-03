def solution(my_string, letter):
    answer = my_string.replace(letter, "")
    return answer

my_string = "abcdef"
letter = "f"
print(solution(my_string, letter))