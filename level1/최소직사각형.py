def solution(sizes):
    left = []
    right = []

    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        left.append(sizes[i][0])
        right.append(sizes[i][1])
        
    return max(left) * max(right)