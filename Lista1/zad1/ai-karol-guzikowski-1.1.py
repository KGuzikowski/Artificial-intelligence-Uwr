from collections import deque
import tabulate

figures = ('K', 'W', 'k')


def pos_to_char(x, y, z):
    return [chr(x[0] + 96) + str(x[1]), chr(y[0] + 96) + str(y[1]), chr(z[0] + 96) + str(z[1])]


def pos2d(s):
    """
        s - position on the board, for example 'a3' or 'h8'
    """
    column = ord(s[0]) - ord('a')
    row = ord(s[1]) - ord('1')
    return column, row


def print_board(wk, wt, bk):
    """
        wk - position of the white king
        wt - position of the white tower
        bk - position of the black king
    """
    board = [[' ' for i in range(8)] for j in range(8)]
    c, r = pos2d(wk)
    board[r][c] = figures[0]

    c, r = pos2d(wt)
    board[r][c] = figures[1]

    c, r = pos2d(bk)
    board[r][c] = figures[2]

    board = [ ([chr(j + 49)] + board[j]) for j in range(8)] + [[' '] + [chr(j + 97) for j in range(8)]]

    print((tabulate.tabulate(board)))
    print()


class State:
    def __init__(self, move, w_k, w_r, b_k, act):
        self.move = move
        self.white_king = w_k
        self.white_rook = w_r
        self.black_king = b_k
        self.moves_no = act


# vectors
dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]


def pos_to_cords(pos):
    return(ord(pos[0]) - 96, int(pos[1]))


ALL_STATES = set()


def can_move(x, y, state, who):
    # GO BLACK
    if state.move == 'black':
        st = ('black_king', state.white_king, state.white_rook, (x, y))
        if st in ALL_STATES:
            return False

        ALL_STATES.add(st)

        rook_x = state.white_rook[0]
        rook_y = state.white_rook[1]

        if x == rook_x or y == rook_y:
            return False

        for i in range(8):
            w_king_x = state.white_king[0] + dx[i]
            w_king_y = state.white_king[1] + dy[i]
            if x == w_king_x and y == w_king_y:
                return False

        return (1 <= x <= 8) and (1 <= y <= 8)

    if state.move == 'white':

        if who == 'white_rook':
            st = ('white_rook', state.white_king, (x, y), state.black_king)
            if st in ALL_STATES:
                return False

            ALL_STATES.add(st)

            return (1 <= x <= 8) and (1 <= y <= 8)

        if who == 'white_king':
            st = ('white_king', (x, y), state.white_rook, state.black_king)
            if st in ALL_STATES:
                return False

            ALL_STATES.add(st)

            for i in range(8):
                b_king_x = state.black_king[0] + dx[i]
                b_king_y = state.black_king[1] + dy[i]

                if x == b_king_x and y == b_king_y:
                    return False

            if x == state.white_rook[0] and y == state.white_rook[1]:
                return False

            return (1 <= x <= 8) and (1 <= y <= 8)


def check_mate(state):
    b_k, w_k, w_r = state.black_king, state.white_king, state.white_rook

    if b_k[0] == 1 and w_k[0] == 3 and b_k[1] == w_k[1] and w_r[0] == 1 and abs(b_k[1] - w_r[1]) > 1:
        return True

    if b_k[0] == 8 and w_k[0] == 6 and b_k[1] == w_k[1] and w_r[0] == 8 and abs(b_k[1] - w_r[1]) > 1:
        return True

    if b_k[1] == 1 and w_k[1] == 3 and b_k[0] == w_k[0] and w_r[1] == 1 and abs(b_k[0] - w_r[0]) > 1:
        return True

    if b_k[1] == 8 and w_k[1] == 6 and b_k[0] == w_k[0] and w_r[1] == 8 and abs(b_k[0] - w_r[0]) > 1:
        return True

    return False


def do_check_mate(akt_state, pre_white, pre_black, beg_state, debug):
    answer = akt_state.moves_no
    winning_moves = []
    if debug:
        while akt_state != beg_state:
            winning_moves.append((akt_state.white_king, akt_state.white_rook, akt_state.black_king, akt_state.moves_no))

            akt_state = pre_white[(akt_state.white_king, akt_state.white_rook, akt_state.black_king, akt_state.moves_no)]

    winning_moves.reverse()
    for w in winning_moves:
        print('Move number: ', w[3])
        chess_board = pos_to_char(w[0], w[1], w[2])
        print_board(chess_board[0], chess_board[1], chess_board[2])
    print('We did check mate in ', answer, ' moves!')
    for _ in range(50):
        print('_', end='')
    print('\n\n\n\n')
    

def find_mate_pos(w_k, w_rook, b_k, first, debug):
    ALL_STATES.clear()
    pre_black, pre_white = {}, {}
    w_k, b_k, w_rook = pos_to_cords(w_k), pos_to_cords(b_k), pos_to_cords(w_rook)
    beg_state = 0
    Q = deque()

    if first == 'white':
        beg_state = State('white', w_k, w_rook, b_k, 0)
        Q.append(beg_state)
    else:
        beg_state = State('black', w_k, w_rook, b_k, 0)
        Q.append(beg_state)

    total = 0
    while len(Q) > 0:
        total += 1
        akt_state = Q.popleft()

        if check_mate(akt_state):
            do_check_mate(akt_state, pre_white, pre_black, beg_state, debug)
            return

        if akt_state.move == 'black':
            for i in range(8):
                new_x = akt_state.black_king[0] + dx[i]
                new_y = akt_state.black_king[1] + dy[i]

                if can_move(new_x, new_y, akt_state, 'black_king'):
                    Q.append(State('white', akt_state.white_king, akt_state.white_rook, (new_x, new_y), akt_state.moves_no + 1))
                    pre_white[(akt_state.white_king, akt_state.white_rook, (new_x, new_y), akt_state.moves_no + 1)] = akt_state

        if akt_state.move == 'white':
            for i in range(8):
                new_x = akt_state.white_king[0] + dx[i]
                new_y = akt_state.white_king[1] + dy[i]

                if can_move(new_x, new_y, akt_state, 'white_king'):
                    Q.append(State('black', (new_x, new_y), akt_state.white_rook, akt_state.black_king, akt_state.moves_no + 1))
                    pre_white[((new_x, new_y), akt_state.white_rook, akt_state.black_king, akt_state.moves_no + 1)] = akt_state

            rook_x, rook_y = akt_state.white_rook[0], akt_state.white_rook[1]

            low, high = 1, 8
            if akt_state.white_king[0] == rook_x:
                if akt_state.white_king[1] > rook_y:
                    high = akt_state.white_king[1] - 1
                else:
                    low = akt_state.white_king[1] + 1

            for i in range(low, high + 1):
                if i == rook_x:
                    continue
                if can_move(i, rook_y, akt_state, 'white_rook'):
                    Q.append(State('black', akt_state.white_king, (i, rook_y), akt_state.black_king, akt_state.moves_no + 1))
                    pre_white[(akt_state.white_king, (i, rook_y), akt_state.black_king, akt_state.moves_no + 1)] = akt_state

            left, right = 1, 8
            if akt_state.white_king[1] == rook_y:
                if akt_state.white_king[1] > rook_x:
                    right = akt_state.white_king[0] - 1
                else:
                    left = akt_state.white_king[0] + 1

            for i in range(left, right + 1):
                if i == rook_y:
                    continue
                if can_move(rook_x, i, akt_state, 'white_rook'):
                    Q.append(State('black', akt_state.white_king, (rook_x, i), akt_state.black_king, akt_state.moves_no + 1))
                    pre_white[(akt_state.white_king, (rook_x, i), akt_state.black_king, akt_state.moves_no + 1)] = akt_state

    print('We considered ', total, ' situations!')


INPUT = []
with open('zad1_input.txt') as f:
    for line in f:
        INPUT.append(line.strip())

debug = True


def solve(board):
    for data in board:
        print('Starting position: ', data)
        print_board(data.split()[1], data.split()[2], data.split()[3])
        board = data.split()
        first_move = board[0]
        w_king = board[1]
        w_rook = board[2]
        b_king = board[3]

        find_mate_pos(w_king, w_rook, b_king, first_move, debug)


solve(INPUT)