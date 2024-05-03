def solution(s):
    s = s.split(" ")
    for i in range(len(s)):
        if len(s[i]) > 0:
            s[i] = list(s[i])
            for j in range(len(s[i])):
                if j % 2 == 0:
                    s[i][j] = s[i][j].upper()
                else:
                    s[i][j] = s[i][j].lower()
        s[i] = ''.join(s[i])
    
    return ' '.join(s)

s = "   A   a    AaAaAaAaA     aAaAaAa     "
print(s)
print(solution(s))
