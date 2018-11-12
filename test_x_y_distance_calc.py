from x_y_distance_calc import x_y_distance_calc


def test_5x6():
    assert x_y_distance_calc(0, 0, 5, 6) == 7.81


def test_0x100():
    assert x_y_distance_calc(0, 0, 0, 100) == 100


def test_1x100():
    assert x_y_distance_calc(0, 0, 1, 100) == 100


def test_passing_zero():
    assert x_y_distance_calc(-2, -6, 3, 0) == 7.81
