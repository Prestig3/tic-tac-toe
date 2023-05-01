def print_board(board):
    print('-------------')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
    print('-------------')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print('-------------')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    print('-------------')

def check_win(board, player):
    win_positions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    for pos in win_positions:
        if all([board[i] == player for i in pos]):
            return True
    return False

def check_tie(board):
    return all([pos != ' ' for pos in board])

def player_move(board):
    while True:
        try:
            pos = int(input("Введите позицию (1-9): "))
            if board[pos] != ' ':
                print("Позиция уже занята!")
                continue
            board[pos] = 'X'
            break
        except ValueError:
            print("Недопустимый ввод. Выберите позицию от 1-9.")
        except IndexError:
            print("Недопустимый ввод. Выберите позицию от 1-9.")

def computer_move(board):
    import random
    pos = random.randint(1, 9)
    while board[pos] != ' ':
        pos = random.randint(1, 9)
    board[pos] = 'O'

def play_game():
    board = [' ']*10
    print("Тик-Так!")
    print_board(board)
    while True:
        player_move(board)
        print_board(board)
        if check_win(board, 'X'):
            print("Ты выиграл!")
            break
        if check_tie(board):
            print("Ничья!")
            break
        computer_move(board)
        print_board(board)
        if check_win(board, 'O'):
            print("Компьютер победил!")
            break

play_game()