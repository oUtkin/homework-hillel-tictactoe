import random


# Функція для створення гральної дошки
def create_board():
    board = [['-' for i in range(3)] for j in range(3)]
    return board


# Функція для відображення гральної дошки
def display_board(board):
    print(board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('_' * 9)
    print(board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('_' * 9)
    print(board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])


# Функція для перевірки на перемогу
def check_win(board, player):
    # Перевірка по горизонталі
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Перевірка по вертикалі
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Перевірка по діагоналях
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


# Функція для ходу комп'ютера
def computer_move(board):
    # Спроба завершити гру (перемога комп'ютера)
    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                board[row][col] = 'O'
                if check_win(board, 'O'):
                    return

                board[row][col] = '-'

    # Спроба заблокувати гравця (перемога гравця)
    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                board[row][col] = 'X'
                if check_win(board, 'X'):
                    board[row][col] = 'O'
                    return

                board[row][col] = '-'

    # Хід комп'ютера (випадковий)
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == '-':
            board[row][col] = 'O'
            return


# Основна функція гри
def play_game():
    board = create_board()
    players = ['X', 'O']
    current_player = random.choice(players)

    while True:
        display_board(board)
        print('Наступний хід')

        if current_player == 'X':
            # Хід гравця
            while True:
                try:
                    row = int(input('Введіть номер рядка (1-3): '))-1
                    col = int(input('Введіть номер стовпця (1-3): '))-1
                    if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == '-':
                        board[row][col] = 'X'
                        break
                    else:
                        print('Комірка вже зайнята. Спробуйте ще раз.')
                except ValueError:
                    print('Некоректний хід. Спробуйте ще раз.')

        else:
            # Хід комп'ютера
            computer_move(board)

        if check_win(board, current_player):
            display_board(board)
            print(f'Гравець {current_player} переміг!')
            break

        if all(board[row][col] != '-' for row in range(3) for col in range(3)):
            display_board(board)
            print('Нічия!')
            break

        current_player = 'X' if current_player == 'O' else 'O'


# Запуск гри
play_game()
