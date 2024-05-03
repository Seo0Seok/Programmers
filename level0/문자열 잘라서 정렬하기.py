def solution(myString):
    answer = []
    myString = myString.split('x')

    for i in myString:
        if i == '':
            pass
        else:
            answer.append(i)
    
    answer.sort()
    return answer

myString1 = "axbxcxdx"
myString2 = "dxccxbbbxaaaa"
myString3 = "xxaxbxcxx"

print(solution(myString3))