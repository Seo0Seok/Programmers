def solution(s):
    num = list("0123456789")
    word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in word:
        if i in s:
            s = s.replace(i, num[word.index(i)])
    return int(s)

s = "123"
print(solution(s))

