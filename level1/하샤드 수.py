def solution(x):
    check = 0
    
    for i in str(x):
        check += int(i)
        
    if x % check == 0:
        return True
    
    return False