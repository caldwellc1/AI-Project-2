import pandas as pd
# print(df['board'][0])
# print(df['breadth_first_search'][0])
# split = df['board'].split(';')


def breadth_first_search(problem):
    node = Node(problem.init)
    explored = set()
    frontier = [node]
    while frontier:
        node = frontier.pop(0)
        if problem.goal_test(node.state):
            return node #solution(node)
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = Node(problem, node, action)
            if child.state #not in explored or frontier:
                frontier.append(child) #frontier?
            elif child.state #in frontier higher cost:
                #replace frontier node with child
    return None


class Problem:
    def __init__(self, board):
        print(board)
        # split board in to a list/matrix of rows and columns
        matrix_board = []
        row = []
        for j in range(len(board)):
            if ord(board[j]) != 59:
                row.append(board[j])
            else:
                matrix_board.append(row)
                row = []
        # get location of ^ for x and y
        x = 0
        y = 0
        for k in range(len(matrix_board)):
            row = matrix_board[k]
            for m in range(len(row)):
                if row[m] == '^':
                    x = m
                    y = k
        in_car = []
        on_board = []
        # get animals on board
        for i in range(len(board)):
            if ord(board[i]) >= 97 and ord(board[i]) <= 122:
                on_board.append(board[i])
        self.init = [x, y, in_car, on_board]
        self.board = matrix_board
        self.path_cost = 0

    def actions(self, state):
        return ['d', 'l', 'r', 'u']


    def result(self, state, action):
        if action == 'd':
            #see if can move, if so move, see if pet there or house
        elif action == 'l':
            new_state = state + 1
        elif action == 'r':
            new_state = state + 1
        elif action == 'u':
            new_state = state + 1
        #return = new_state


    def goal_test(self, state):
        return len(state[2]) == 0 and len(state[3]) == 0


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost


def main():
    df = pd.read_csv('breadth_first_search_train.csv')
    problem = Problem(df['board'][0])
    print(breadth_first_search(problem))

if __name__ == '__main__':
    main()
