def solution(board):
    answer = 0
    new_board = [[0] * len(board) for i in range(len(board))]

    if len(board) == 1:
        if board[0][0] == 1:
            return 0
        else :
            return 1
            
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                if i-1 < 0:
                    if j-1 < 0:
                        new_board[i][j] = new_board[i][j+1] = 2
                        new_board[i+1][j] = new_board[i+1][j+1] = 2
                    elif j+1 > len(board)-1:
                        new_board[i][j-1] = new_board[i][j] = 2
                        new_board[i+1][j-1] = new_board[i+1][j] = 2
                    else:
                        new_board[i][j-1] = new_board[i][j] = new_board[i][j+1] = 2
                        new_board[i+1][j-1] = new_board[i+1][j] = new_board[i+1][j+1] = 2
                   
                elif i+1 > len(board)-1:
                    if j-1 < 0:
                        new_board[i-1][j] = new_board[i-1][j+1] = 2
                        new_board[i][j] = new_board[i][j+1] = 2
                    elif j+1 > len(board)-1:
                        new_board[i-1][j-1] = new_board[i-1][j] = 2
                        new_board[i][j-1] = new_board[i][j] = 2
                    else:
                        new_board[i-1][j-1] = new_board[i-1][j] = new_board[i-1][j+1] = 2
                        new_board[i][j-1] = new_board[i][j] = new_board[i][j+1] = 2
                    
                elif j-1 < 0:
                    if i-1 < 0:
                        new_board[i][j] = new_board[i][j+1] = 2
                        new_board[i+1][j] = new_board[i+1][j+1] = 2
                    elif i+1 > len(board)-1:
                        new_board[i-1][j] = new_board[i-1][j+1] = 2
                        new_board[i][j] = new_board[i][j+1] = 2
                    else:
                        new_board[i-1][j] = new_board[i-1][j+1] = 2
                        new_board[i][j] = new_board[i][j+1] = 2
                        new_board[i+1][j] = new_board[i+1][j+1] = 2

                elif j+1 > len(board)-1:
                    if i-1 <0:
                        new_board[i][j-1] = new_board[i][j] = 2
                        new_board[i+1][j-1] = new_board[i+1][j] = 2
                    elif i+1 > len(board)-1:
                        new_board[i-1][j-1] = new_board[i-1][j] = 2
                        new_board[i][j-1] = new_board[i][j] = 2
                    else:
                        new_board[i-1][j-1] = new_board[i-1][j] = 2
                        new_board[i][j-1] = new_board[i][j] = 2
                        new_board[i+1][j-1] = new_board[i+1][j] = 2

                else:
                    new_board[i-1][j-1] = new_board[i-1][j] = new_board[i-1][j+1] = 2
                    new_board[i][j-1] = new_board[i][j] = new_board[i][j+1] = 2
                    new_board[i+1][j-1] = new_board[i+1][j] = new_board[i+1][j+1] = 2
                
    for i in range(len(new_board)):
        for j in range(len(new_board[i])):
            if new_board[i][j] == 0:
                answer += 1
    return answer


board = [[0]]

print(solution(board))
