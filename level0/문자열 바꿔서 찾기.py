def solution(myString, pat):
    answer = 0
    myString2 = ""
    for i in myString:
        if i == "A":
            i = "B"
        elif i == "B":
            i = "A"
        myString2 += i
    if pat in myString2:
        return 1
    else:
        return 0
    
myString = "ABAB"
pat = "ABAB"
print(solution(myString, pat))