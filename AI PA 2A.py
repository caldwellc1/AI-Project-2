import pandas as pd
import collections


def a_star(problem):
    node = Node(problem.init)
    explored = set()
    frontier = collections.deque()
    frontier.append(node)
    dict = {tuple(node.state): path_cost(node)}
    answer = []
    count = 0
    while frontier:
        min_node = min(dict, key = dict.get)
        index_frontier = priority(frontier, min_node)
        node = list(frontier)[index_frontier]
        frontier.remove(node)
        del dict[tuple(node.state)]
        if problem.goal_test(node.state):
            print(count)
            return solution(node, answer)
        explored.add(tuple(node.state))
        for action in problem.actions(node.state):
            child = child_node(problem, node, action)
            count += 1
            if tuple(child.state) not in explored and tuple(child.state) not in dict:
                frontier.append(child)
                dict.update({tuple(child.state): path_cost(child)})
            elif child_higher_cost(frontier, child):
                frontier[get_index(frontier, child.state)] = child
    return answer


def path_cost(node):
    return node.path_cost + h(node.state)


def priority(frontier, min):
    for q in range(len(frontier)):
        if tuple(frontier[q].state) == min:
            return q
    return IndexError


def h(state):
    return len(state[2]) + 2 * len(state[3])


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
        matrix_board = []
        row = []
        for j in range(len(board)):
            if ord(board[j]) != 59:
                row.append(board[j])
            else:
                matrix_board.append(row)
                row = []
        x = 0
        y = 0
        for k in range(len(matrix_board)):
            row = matrix_board[k]
            for m in range(len(row)):
                if row[m] == '^':
                    x = k
                    y = m
        in_car = []
        on_board = []
        for i in range(len(board)):
            if 97 <= ord(board[i]) <= 122:
                on_board.append(board[i])
        self.init = [x, y, tuple(in_car), tuple(on_board)]
        self.board = matrix_board
        self.path_cost = 0

    def actions(self, state):
        move = []
        if self.board[state[0]+1][state[1]] != '.':
            move.append('d')
        if self.board[state[0]][state[1]-1] != '.':
            move.append('l')
        if self.board[state[0]][state[1]+1] != '.':
            move.append('r')
        if self.board[state[0]-1][state[1]] != '.':
            move.append('u')
        return move

    def result(self, state, action):
        new_state = state
        if action == 'd':
            for g in range(1, 3):
                move = self.board[state[0]+g][state[1]]
                if move != '.':
                    if 97 <= ord(move) <= 122:
                        if move not in state[2] and move in state[3]:
                            two = state[2] + tuple(move)
                            three = tuple([r for r in state[3] if r != move])
                            new_state = [state[0]+g, state[1], two, three]
                        else:
                            new_state = [state[0]+g, state[1], state[2], state[3]]
                    elif 65 <= ord(move) <= 90:
                        if move.lower() in state[2]:
                            two = tuple([t for t in state[2] if t != move.lower()])
                            new_state = [state[0]+g, state[1], two, state[3]]
                        else:
                            new_state = [state[0]+g, state[1], state[2], state[3]]
                    else:
                        new_state = [state[0]+g, state[1], state[2], state[3]]
                else:
                    break
        elif action == 'l':
            for g in range(1, 3):
                move = self.board[state[0]][state[1]-g]
                if move != '.':
                    if 97 <= ord(move) <= 122:
                        if move not in state[2] and move in state[3]:
                            two = state[2] + tuple(move)
                            three = tuple([r for r in state[3] if r != move])
                            new_state = [state[0], state[1]-g, two, three]
                        else:
                            new_state = [state[0], state[1]-g, state[2], state[3]]
                    elif 65 <= ord(move) <= 90:
                        if move.lower() in state[2]:
                            two = tuple([t for t in state[2] if t != move.lower()])
                            new_state = [state[0], state[1]-g, two, state[3]]
                        else:
                            new_state = [state[0], state[1]-g, state[2], state[3]]
                    else:
                        new_state = [state[0], state[1]-g, state[2], state[3]]
                else:
                    break
        elif action == 'r':
            for g in range(1, 3):
                move = self.board[state[0]][state[1]+g]
                if move != '.':
                    if 97 <= ord(move) <= 122:
                        if move not in state[2] and move in state[3]:
                            two = state[2] + tuple(move)
                            three = tuple([r for r in state[3] if r != move])
                            new_state = [state[0], state[1]+g, two, three]
                        else:
                            new_state = [state[0], state[1]+g, state[2], state[3]]
                    elif 65 <= ord(move) <= 90:
                        if move.lower() in state[2]:
                            two = tuple([t for t in state[2] if t != move.lower()])
                            new_state = [state[0], state[1]+g, two, state[3]]
                        else:
                            new_state = [state[0], state[1]+g, state[2], state[3]]
                    else:
                        new_state = [state[0], state[1]+g, state[2], state[3]]
                else:
                    break
        elif action == 'u':
            for g in range(1, 3):
                move = self.board[state[0]-g][state[1]]
                if move != '.':
                    if 97 <= ord(move) <= 122:
                        if move not in state[2] and move in state[3]:
                            two = state[2] + tuple(move)
                            three = tuple([r for r in state[3] if r != move])
                            new_state = [state[0]-g, state[1], two, three]
                        else:
                            new_state = [state[0]-g, state[1], state[2], state[3]]
                    elif 65 <= ord(move) <= 90:
                        if move.lower() in state[2]:
                            two = tuple([t for t in state[2] if t != move.lower()])
                            new_state = [state[0]-g, state[1], two, state[3]]
                        else:
                            new_state = [state[0]-g, state[1], state[2], state[3]]
                    else:
                        new_state = [state[0]-g, state[1], state[2], state[3]]
                else:
                    break
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
    df = pd.read_csv('test.csv')
    for u in range(33, 51):
        problem = Problem(df['board'][u])
        with open('answers2.txt', 'a') as fp:
            fp.write(str(a_star(problem)) + str(u) +"\n")

if __name__ == '__main__':
    main()
