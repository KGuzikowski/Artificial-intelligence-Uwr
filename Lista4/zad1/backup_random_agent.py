import random

#0 -free, 1 - black, 2 - white
size = 8
board = [[0 for i in range(size)] for j in range(size)]
board[size//2 - 1][size//2 - 1] = 2
board[size//2][size//2] = 2
board[size//2 - 1][size//2] = 1
board[size//2][size//2 - 1] = 1
free = size**2 - 4
turn = 1
first = 1
def find_neighbours(move, board):
    x = move[0]
    y = move[1]
    neighbours = []
    for i in range(3):
        for j in range(3):
            a = i - 1
            b = j - 1 
            if (x + a) < size and (x + a >= 0) and (y + b < size) and (y + b >= 0):
                neighbours.append([x+a, y+b])
    return neighbours



def make_move(move, board):
    x = move[0]
    y = move[1]
    neighbours = find_neighbours(move, board)
    changed = False
    for neighbour in neighbours:
        nx = neighbour[0]
        ny = neighbour[1]
        if board[nx][ny] == 2 - (turn + 1)%2:
            new_x = nx
            new_y = ny
            last_color = 2 - (turn + 1)%2
            visited = [[new_x, new_y]]
            while (new_x + nx - x) < size and (new_x + nx - x>= 0) and (new_y + ny - y >= 0) and (new_y + ny - y >= 0) and last_color == 2 - (turn + 1)%2 and not changed:
                new_x += nx - x
                new_y += ny - y
                last_color = board[new_x][new_y]
                visited.append([new_x, new_y])
                if board[new_x][new_y] == turn:
                    for node in visited:
                        board[x][y] = turn
                        board[node[0]][node[1]] = turn
                        changed = True
    return changed
    



def random_bot(board, turn):
    pos_moves = []
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                neighbours = find_neighbours([i,j], board)
                neighbours = list(filter(lambda x: board[x[0]][x[1]] == 2 - (turn + 1)%2, neighbours))
                if find_neighbours([i,j], board) != []:
                    copy = [[]for k in range(size)]
                    for k in range(size):
                        for l in range(size):
                            copy[k].append(board[k][l])
                    if make_move([i,j], copy):
                        pos_moves.append([i,j])

    return random.choice(pos_moves)

                    
    



def print_board():
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                print(". ", end="")
            elif board[i][j] == 1:
                print("○ ", end="")
            else:
                print("● ", end="")
        print(" ")





while True:
    print_board()
    print("turn:", turn)
    if turn == 1:
        move = input().split(" ")
    else:
        move = random_bot(board, turn)

    move[0] = int(move[0])
    move[1] = int(move[1])
    make_move(move, board)
    turn = 2 - (turn + 1)%2
    
