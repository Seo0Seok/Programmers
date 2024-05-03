def solution(my_string):
    num = ["0","1","2","3","4","5","6","7","8","9"]
    answer = 0

    for i in range(len(num)):
        a = my_string.count(num[i])
        b = a * int(num[i])
            
        answer += b
    
    return answer


       
my_string = "aAb1B2cC34oOp")
print(solution(my_string))
