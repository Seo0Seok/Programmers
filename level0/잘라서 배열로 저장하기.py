def solution(my_str, n):
    answer = []
    k = 0
    
    if len(my_str) % n == 0:
        for i in range(int(len(my_str) // n)):
            answer.append(my_str[k:n+k])
            k += n
    else:
        for i in range(len(my_str) // n + 1):
            answer.append(my_str[k:n+k])
            k += n
    return answer

my_str = "abc1Addfggg4556b"
n = 6

my_str2 = "abcdef123"
n2 = 3

print(solution(my_str2, n2))