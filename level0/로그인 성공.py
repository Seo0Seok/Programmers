def solution(id_pw, db):
    a = 0
    b = 0
    c = 0
    
    for i in range(len(db)):
        if id_pw[0] == db[i][0] and id_pw[1] == db[i][1]:
            a += 1
        elif id_pw[0] == db[i][0] and id_pw[1] != db[i][1]:
            b += 1
        elif id_pw[0] != db[i][0]:
            c += 1
    
    if a:
        return "login"
    elif b:
        return "wrong pw"
    elif c:
        return "fail"