def solution(game_board, table):
    answer = -1
    block = []
    space = []
    size = len(game_board)
    
    for i in range(size):
        for j in range(size):
            if game_board[i][j] == 1:
                game_board[i][j] = 0
            elif game_board[i][j] == 0:
                game_board[i][j] = 1
    
    for i in range(size):
        for j in range(size):
            if table[i][j] == 1:
                block.append(find_block(table,i, j))
            if game_board[i][j] == 1:
                space.append(find_block(game_board, i, j))

    return answer

# 블럭 뽑아내기 (bfs)
def find_block(table, x, y):
    d=[(-1, 0), (1, 0), (0, -1), (0, 1)]
    que = []

    que.append((x, y))
    table[x][y] = 0
    cnt = 0
    
    while cnt < len(que):
        x, y = que[cnt]
        cnt += 1
        for i in range(4) :
            nx = x + d[i][0]
            ny = y + d[i][1]

            if not (nx >= 0 and nx < len(table) and ny >= 0 and ny < len(table)):
                continue
            if table[nx][ny] == 1 :
                que.append((nx, ny))
                table[nx][ny] = 0
    return que