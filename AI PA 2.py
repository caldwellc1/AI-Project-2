
import pandas as pd
df = pd.read_csv('breadth_first_search_train.csv')
print(df['board'][0])
print(df['breadth_first_search'][0])
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


def start_state(board):
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
    return [x, y, in_car, on_board]


def breadth_first_search(board):
    answer = ''
    state = start_state(board)
    node = {}
    explored = {}
    frontier = [state]
    actions = ['d', 'l', 'r', 'u']
    while goal_test(state) == 0:
        if len(frontier) == 0:
            return 'Fail'
        if goal_test(state) == 1:
            return state
        explored.update(state)
        for action in actions:
            child = [board, state, action]
            if child[1] in explored == False or child[1] in frontier:
                frontier.append(child)
            elif child[1] in frontier:
                frontier[-1] = child
    return answer

print(breadth_first_search(df['board'][0]))

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
