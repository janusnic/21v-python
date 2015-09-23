import main


def test_get_board():
    alive_cons = [(1, 1),
                  (2, 2),
                  (3, 1),
                  (3, 3),
                  (4, 0)]
    board = [[0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 1, 0, 1, 0],
             [1, 0, 0, 0, 0]]
    assert main.get_board(5, alive_cons) == board


class TestGetNeighbors(object):
    def test_zero_positive(self):
        con = (0, 2)
        neighbors = [(-1, 1),
                     (-1, 2),
                     (-1, 3),
                     (0, 1),
                     (0, 3),
                     (1, 1),
                     (1, 2),
                     (1, 3)]
        assert main.get_neighbors(con) == neighbors

    def test_zero_zero(self):
        con = (0, 0)
        neighbors = [(-1, -1),
                     (-1, 0),
                     (-1, 1),
                     (0, -1),
                     (0, 1),
                     (1, -1),
                     (1, 0),
                     (1, 1)]
        assert set(main.get_neighbors(con)) == set(neighbors)

    def test_positive_result(self):
        con = (5, 5)
        neighbors = [(4, 4),
                     (4, 5),
                     (4, 6),
                     (5, 4),
                     (5, 6),
                     (6, 4),
                     (6, 5),
                     (6, 6)]
        assert set(main.get_neighbors(con)) == set(neighbors)


def test_calculate_alive_neighbors():
    con = (0, 2)

    alive_cons = [(0, 0),
                  (1, 1),
                  (1, 2),
                  (2, 4),
                  (3, 5),
                  (0, 3)]
    assert main.calculate_alive_neighbors(con, alive_cons) == 3


class TestIsAliveCon(object):
    def test_new_con(self):
        alive_cons = [(1, 1),
                      (2, 0),
                      (2, 2)]
        con = (2, 1)
        assert main.is_alive_con(con, alive_cons) is True

    def test_alive_con_alive_3_neighbors(self):
        alive_cons = [(1, 1),
                      (2, 0),
                      (2, 1),
                      (2, 2)]
        con = (2, 1)
        assert main.is_alive_con(con, alive_cons) is True

    def test_alive_con_alive_2_neighbors(self):
        alive_cons = [(1, 1),
                      (2, 0),
                      (2, 1)]
        con = (2, 1)
        assert main.is_alive_con(con, alive_cons) is True

    def tests_dead_con_few_neighbor(self):
        alive_cons = [(1, 1),
                      (2, 0)]
        con = (2, 1)
        assert main.is_alive_con(con, alive_cons) is False

    def test_alive_con_few_neighbors(self):
        alive_cons = [(1, 1),
                      (2, 1)]
        con = (2, 1)
        assert main.is_alive_con(con, alive_cons) is False

    def test_many_neighbors(self):
        alive_cons = [(1, 0),
                      (1, 1),
                      (2, 0),
                      (3, 1)]
        con = (2, 1)
        assert main.is_alive_con(con, alive_cons) is False


class TestIsCorrectCon(object):
    def test_zero_zero(self):
        assert main.is_correct_con(5, (0, 0)) is True

    def test_zero_positive(self):
        assert main.is_correct_con(5, (0, 4)) is True
        assert main.is_correct_con(5, (4, 0)) is True

    def test_zero_negative(self):
        assert main.is_correct_con(5, (0, -1)) is False
        assert main.is_correct_con(5, (-1, 0)) is False

    def test_negative(self):
        assert main.is_correct_con(5, (-1, -6)) is False
        assert main.is_correct_con(5, (-6, -1)) is False
        assert main.is_correct_con(5, (-6, -6)) is False
        assert main.is_correct_con(5, (-1, -1)) is False

    def test_posirive(self):
        assert main.is_correct_con(5, (1, 1)) is True

    def test_over_size(self):
        assert main.is_correct_con(5, (1, 5)) is False
        assert main.is_correct_con(5, (5, 1)) is False
        assert main.is_correct_con(5, (1, 6)) is False
        assert main.is_correct_con(5, (6, 6)) is False

    def test_negative_over_size(self):
        assert main.is_correct_con(5, (-6, 6)) is False
        assert main.is_correct_con(5, (6, -6)) is False
        assert main.is_correct_con(5, (-1, 6)) is False
        assert main.is_correct_con(5, (-1, 6)) is False


def test_correct_cons():
    cons = [(1, 1),
            (-1, 2),
            (1, -1),
            (1, 10)]
    assert main.correct_cons(5, cons) == [(1, 1)]


class TestNewStep(object):
    def test_glader(self):
        alive_cons = [(1, 2),
                      (2, 3),
                      (3, 1),
                      (3, 2),
                      (3, 3)]
        new_alive_cons = [(2, 1),
                          (2, 3),
                          (3, 2),
                          (3, 3),
                          (4, 2)]
        assert set(main.new_step(alive_cons)) == set(new_alive_cons)

    def test_flasher(self):
        alive_cons = [(0, 1),
                      (1, 1),
                      (2, 1)]
        new_alive_cons = [(1, 0),
                          (1, 1),
                          (1, 2)]
        assert set(main.new_step(alive_cons)) == set(new_alive_cons)