def test_area(rectangle):
    result = rectangle.area()
    expected = 10 * 20
    assert result == expected


def test_perimeter(rectangle):
    result = rectangle.perimeter()
    expected = 2 * (10 + 20)
    assert result == expected


def test_not_equal(rectangle, other_rectangle):
    assert rectangle != other_rectangle
