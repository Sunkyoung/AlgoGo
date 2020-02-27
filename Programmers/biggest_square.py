def solution(board):
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] >= 1: # 0이 아닐 때만 값 업데이트 : 이게 테스트 통과의 관건!
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1]) + 1
    return max([num for row in board for num in row])**2 # list comprehension 사용 - 전체 배열의 최대값 구하기 ^2