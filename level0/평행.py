def solution(dots):
    check = []
  
    for i in range(len(dots)):
        for j in range(i+1, len(dots)):
            print(i,j)
            check.append([(dots[i][0] - dots[j][0]), (dots[i][1] - dots[j][1])])

    for k in range(len(dots)-1):
        if [check[k][0] / check[len(check)-1-k][0]] == [check[k][1] / check[len(check)-1-k][1]]:
            return 1
    return 0

dots =  [[3, 5], [4, 1], [2, 4], [5, 10]]
print(solution(dots))