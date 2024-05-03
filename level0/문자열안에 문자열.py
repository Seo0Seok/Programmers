def solution(str1, str2):
    answer = 2
    a = len(str2)
    b = len(str1) - len(str2) + 1

    for i in range(0, b):
        if str1[i:a+i] == str2:
            print("str1=", str1[i:a+i])
            print("str2=", str2)
            answer = 1
    return answer

str1 = "AbcAbcA"
str2 = "Abc"
print(solution(str1, str2))

