import pandas as pd
df = pd.read_csv('breadth_first_search_train.csv')
print(df['board'])
print(df['breadth_first_search'])
# split = df['board'].split(';')

def actions(state, action_taken, animal, house):
    # if animal there grab it
    # if house there, see if animal is in car
    if action_taken == 'd':
        new_state = [state[0] + 1, state[0] + 1, state[0] + 1, state[0] + 1,]
    elif action_taken == 'l':
        new_state = state + 1
    elif action_taken == 'r':
        new_state = state + 1
    elif action_taken == 'u':
        new_state = state + 1

def goal_test(state):
    if state == []:
        return 1
    return 0

def breadth_first_search(board):
    answer = ''
    # split board in to a list/matrix of rows and columns
    matrix_board = []
    row = []
    for j in range(len(board[1])):
        if ord(board[1][j]) != 59:
            row.append(board[1][j])
        else:
            matrix_board.append(row)
            row = []
    # get location of ^ for x and y
    x = 0
    y = 0
    in_car = []
    on_board = []
    # get animals on board
    for i in range(len(board[1])):
        if ord(board[1][i]) >= 97 or ord(board[1][i]) <= 122:
            on_board.append(board[1][i])
    node = [x, y, in_car, on_board]
    return answer

print(breadth_first_search(df['board']))
