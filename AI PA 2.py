import pandas as pd

def breadth_first_search(problem):
    node = Node(problem.init)
    explored = set()
    frontier = [node]
    answer = []
    while frontier:
        node = frontier.pop(0)
        if problem.goal_test(node.state):
            return solution(node, answer) #solution(node)
        explored.add(tuple(node.state))
        for action in problem.actions(node.state):
            child = child_node(problem, node, action)
            if tuple(child.state) in explored or child_in_frontier(frontier, child.state): #not in explored or frontier:
                frontier.append(child)
            elif child_higher_cost(frontier, child): #in frontier higher cost:
                frontier[get_index(frontier, child.state)] = child#replace frontier node with child
    return answer

def get_index(frontier, state):
    for a in range(len(frontier)):
        if frontier[a].state == state:
            return a
    return IndexError

def child_higher_cost(frontier, child):
    for a in range(len(frontier)):
        if frontier[a].state == child.state:
            if frontier[a].path_cost > child.path_cost:
                return True
            else:
                return False
    return False

def child_in_frontier(frontier, test):
    for a in range(len(frontier)):
        if frontier[a].state == test:
            return False
    return True

def solution(node, answer):
    if node.parent is None:
        answer.insert(0, node.action)
        return answer
    else:
        answer.insert(0, node.acion)
        next_node = node.parent
        solution(next_node, answer)

def child_node(problem, parent, action):
    return Node(problem.result(parent.state, action), parent, action, parent.path_cost + 1)

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
        in_car = set()
        on_board = set()
        # get animals on board
        for i in range(len(board)):
            if 97 <= ord(board[i]) <= 122:
                on_board.add(board[i])
        self.init = [x, y, in_car, on_board]
        self.board = matrix_board
        self.path_cost = 0

    def actions(self, state):
        return ['d', 'l', 'r', 'u']

    def result(self, state, action):
        new_state = state
        if action == 'd':
            move = self.board[state[0]][state[1]+1]
            if move != '.':
                if 97 <= ord(move) <= 122:
                    if move not in state[2] and move in state[3]:
                        state[2].add(move)
                        state[3].remove(move)
                        new_state = [state[0], state[1]+1, state[2], state[3]]
                elif 65 <= ord(move) <= 90:
                    if move.lower in state[2]:
                        state[2].remove(move)
                        new_state = [state[0], state[1]+1, state[2], state[3]]
                else:
                    new_state = [state[0], state[1]+1, state[2], state[3]]
            #see if can move, if so move, see if pet there or house
        elif action == 'l':
            move = self.board[state[0]-1][state[1]]
            if move != '.':
                if 97 <= ord(move) <= 122:
                    if move not in state[2] and move in state[3]:
                        state[2].add(move)
                        state[3].remove(move)
                        new_state = [state[0]-1, state[1], state[2], state[3]]
                elif 65 <= ord(move) <= 90:
                    if move.lower in state[2]:
                        state[2].remove(move)
                        new_state = [state[0]-1, state[1], state[2], state[3]]
                else:
                    new_state = [state[0]-1, state[1], state[2], state[3]]
        elif action == 'r':
            move = self.board[state[0]+1][state[1]]
            if move != '.':
                if 97 <= ord(move) <= 122:
                    if move not in state[2] and move in state[3]:
                        state[2].add(move)
                        state[3].remove(move)
                        new_state = [state[0]+1, state[1], state[2], state[3]]
                elif 65 <= ord(move) <= 90:
                    if move.lower in state[2]:
                        state[2].remove(move)
                        new_state = [state[0]+1, state[1], state[2], state[3]]
                else:
                    new_state = [state[0]+1, state[1], state[2], state[3]]
        elif action == 'u':
            move = self.board[state[0]][state[1]-1]
            if move != '.':
                if 97 <= ord(move) <= 122:
                    if move not in state[2] and move in state[3]:
                        state[2].add(move)
                        state[3].remove(move)
                        new_state = [state[0], state[1]-1, state[2], state[3]]
                elif 65 <= ord(move) <= 90:
                    if move.lower in state[2]:
                        state[2].remove(move)
                        new_state = [state[0], state[1]-1, state[2], state[3]]
                else:
                    new_state = [state[0], state[1]-1, state[2], state[3]]
        return new_state

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
