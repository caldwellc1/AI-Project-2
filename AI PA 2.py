import pandas as pd


def breadth_first_search(problem):
    node = Node(problem.init)
    explored = set()
    frontier = [node]
    answer = []
    while frontier:
        node = frontier.pop(0)
        if problem.goal_test(node.state):
            return solution(node, answer)
        explored.add(tuple(node.state))
        for action in problem.actions(node.state):
            child = child_node(problem, node, action)
            if tuple(child.state) not in explored and child_not_in_frontier(frontier, tuple(child.state)):
                frontier.append(child)
            elif child_higher_cost(frontier, child):  # in frontier higher cost:
                print('hit')
                frontier[get_index(frontier, child.state)] = child
    return answer

def get_index(frontier, state):
    for a in range(len(frontier)):
        if frontier[a].state == state:
            return a
    return IndexError


def child_higher_cost(frontier, child):
    for a in range(len(frontier)):
        if frontier[a].state == tuple(child.state):
            if frontier[a].path_cost > child.path_cost:
                return True
            else:
                return False
    return False


def child_not_in_frontier(frontier, test):
    for a in range(len(frontier)):
        if frontier[a].state == test:
            return False
    return True


def solution(node, answer):
    if node.parent is None:
        return answer
    else:
        answer.insert(0, node.action)
        next_node = node.parent
        solution(next_node, answer)
    return answer


def child_node(problem, parent, action):
    return Node(problem.result(parent.state, action), parent, action, parent.path_cost + 1)


class Problem:
    def __init__(self, board):
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
            if 97 <= ord(board[i]) <= 122:
                on_board.append(board[i])
        self.init = [x, y, tuple(in_car), tuple(on_board)]
        self.board = matrix_board
        self.path_cost = 0

    def actions(self, state):
        return ['d', 'l', 'r', 'u']

    def result(self, state, action):
        new_state = state
        if action == 'd':
            move = self.board[state[0]+1][state[1]]
            if move != '.':
                if 97 <= ord(move) <= 122:
                    if move not in state[2] and move in state[3]:
                        two = state[2] + tuple(move)
                        three = tuple([r for r in state[3] if r != move])
                        new_state = [state[0]+1, state[1], two, three]
                    else:
                        new_state = [state[0]+1, state[1], state[2], state[3]]
                elif 65 <= ord(move) <= 90:
                    if move.lower() in state[2]:
                        two = tuple([t for t in state[2] if t != move.lower()])
                        new_state = [state[0]+1, state[1], two, state[3]]
                    else:
                        new_state = [state[0]+1, state[1], state[2], state[3]]
                else:
                    new_state = [state[0]+1, state[1], state[2], state[3]]
            # see if can move, if so move, see if pet there or house
        elif action == 'l':
            move = self.board[state[0]][state[1]-1]
            if move != '.':
                if 97 <= ord(move) <= 122:
                    if move not in state[2] and move in state[3]:
                        two = state[2] + tuple(move)
                        three = tuple([r for r in state[3] if r != move])
                        new_state = [state[0], state[1]-1, two, three]
                    else:
                        new_state = [state[0], state[1]-1, state[2], state[3]]
                elif 65 <= ord(move) <= 90:
                    if move.lower() in state[2]:
                        two = tuple([t for t in state[2] if t != move.lower()])
                        new_state = [state[0], state[1]-1, two, state[3]]
                    else:
                        new_state = [state[0], state[1]-1, state[2], state[3]]
                else:
                    new_state = [state[0], state[1]-1, state[2], state[3]]
        elif action == 'r':
            move = self.board[state[0]][state[1]+1]
            if move != '.':
                if 97 <= ord(move) <= 122:
                    if move not in state[2] and move in state[3]:
                        two = state[2] + tuple(move)
                        three = tuple([r for r in state[3] if r != move])
                        new_state = [state[0], state[1]+1, two, three]
                    else:
                        new_state = [state[0], state[1]+1, state[2], state[3]]
                elif 65 <= ord(move) <= 90:
                    if move.lower() in state[2]:
                        two = tuple([t for t in state[2] if t != move.lower()])
                        new_state = [state[0], state[1]+1, two, state[3]]
                    else:
                        new_state = [state[0], state[1]+1, state[2], state[3]]
                else:
                    new_state = [state[0], state[1]+1, state[2], state[3]]
        elif action == 'u':
            move = self.board[state[0]-1][state[1]]
            if move != '.':
                if 97 <= ord(move) <= 122:
                    if move not in state[2] and move in state[3]:
                        two = state[2] + tuple(move)
                        three = tuple([r for r in state[3] if r != move])
                        new_state = [state[0]-1, state[1], two, three]
                    else:
                        new_state = [state[0]-1, state[1], state[2], state[3]]
                elif 65 <= ord(move) <= 90:
                    if move.lower() in state[2]:
                        two = tuple([t for t in state[2] if t != move.lower()])
                        new_state = [state[0]-1, state[1], two, state[3]]
                    else:
                        new_state = [state[0]-1, state[1], state[2], state[3]]
                else:
                    new_state = [state[0]-1, state[1], state[2], state[3]]
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
