def solution(s):
    flag = True
    for i in s:
        if i not in "1234567890":
            flag = False
            
    if flag and (len(s) == 4 or len(s) == 6):
        return True
    else:
        return False