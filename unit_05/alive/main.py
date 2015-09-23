#!/usr/bin/python

import itertools


def get_board(size, alive_cons):
    return [[1 if (i, j) in alive_cons else 0
             for j in xrange(size)]
            for i in xrange(size)]


def get_neighbors(con):
    x, y = con
    neighbors = [(x + i, y + j)
                 for i in xrange(-1, 2)
                 for j in xrange(-1, 2)
                 if not i == j == 0]
    return neighbors


def calculate_alive_neighbors(con, alive_cons):
    return len(filter(lambda x: x in alive_cons,
                      get_neighbors(con)))


def is_alive_con(con, alive_cons):
    alive_neighbors = calculate_alive_neighbors(con, alive_cons)
    if (alive_neighbors == 3 or
            (alive_neighbors == 2 and con in alive_cons)):
        return True
    return False


def new_step(alive_cons):
    board = itertools.chain(*map(get_neighbors, alive_cons))
    new_board = set([con
                     for con in board
                     if is_alive_con(con, alive_cons)])
    return list(new_board)


def is_correct_con(size, con):
    x, y = con
    return all(0 <= coord <= size - 1 for coord in [x, y])


def correct_cons(size, cons):
    return filter(lambda x: is_correct_con(size, x), cons)


def print_board(board):
    for line in board:
        print line
    print


def main():
    size = 6
    board = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3),(3,4)]
    print_board(get_board(size, board))
    for _ in xrange(10):
        board = correct_cons(size, new_step(board))
        print_board(get_board(size, board))


if __name__ == '__main__':
    main()