import pytest
from lab10 import multiply, divide, distance, quadratic, geometric_sum, word_count, find_substring, to_uppercase
#Сайланкин Дамир 107b
@pytest.fixture
def sample_text():
    with open("sample.txt", "r") as file:
        return file.read()

class TestMathFunctions:

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 6),
        (-2, 3, -6),
        (0, 5, 0),
        (7, -3, -21),
        (-4, -5, 20)
    ])
    def test_multiply(self, a, b, expected):
        assert multiply(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (6, 3, 2),
        (-6, 3, -2),
        (0, 5, 0),
        (7, -7, -1)
    ])
    def test_divide(self, a, b, expected):
        if b == 0:
            with pytest.raises(ValueError):
                divide(a, b)
        else:
            assert divide(a, b) == expected

    @pytest.mark.parametrize("x1, y1, x2, y2, expected", [
        (0, 0, 3, 4, 5),
        (1, 1, 1, 1, 0),
        (-1, -1, 2, 2, 4.242640687119285),
        (1, 2, 4, 6, 5),
        (0, 0, 0, 0, 0)
    ])
    def test_distance(self, x1, y1, x2, y2, expected):
        assert distance(x1, y1, x2, y2) == expected

    @pytest.mark.parametrize("a, b, c, expected", [
        (1, -3, 2, (2, 1)),
        (1, 2, 1, (-1, -1)),
        (1, 0, -4, (2, -2)),
        (1, -2, 5, None),
        (1, 4, 4, (-2, -2))
    ])
    def test_quadratic(self, a, b, c, expected):
        assert quadratic(a, b, c) == expected

    @pytest.mark.parametrize("a, r, n, expected", [
        (2, 3, 3, 26),
        (1, 2, 5, 31),
        (1, 1, 5, 5),
        (5, 0.5, 4, 9.375),
        (1, 0, 10, 1)
    ])
    def test_geometric_sum(self, a, r, n, expected):
        assert geometric_sum(a, r, n) == expected

class TestStringFunctions:

    @pytest.mark.parametrize("text, expected", [
        ("Lorem ipsum dolor sit amet", 5),
        ("Consectetur adipiscing elit", 3),
        ("Sed do eiusmod tempor incididunt", 5),
        ("Ut enim ad minim veniam", 5),
        ("Quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat", 12)
    ])
    def test_word_count(self, text, expected):
        assert word_count(text) == expected

    @pytest.mark.parametrize("text, substring, expected", [
        ("Lorem ipsum dolor sit amet", "ipsum", True),
        ("Consectetur adipiscing elit", "elit", True),
        ("Sed do eiusmod tempor incididunt", "nonexistent", False),
        ("Ut enim ad minim veniam", "veniam", True),
        ("Quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat", "laboris", True)
    ])
    def test_find_substring(self, text, substring, expected):
        assert find_substring(text, substring) == expected

    @pytest.mark.parametrize("text, expected", [
        ("Lorem ipsum dolor sit amet", "LOREM IPSUM DOLOR SIT AMET"),
        ("Consectetur adipiscing elit", "CONSECTETUR ADIPISCING ELIT"),
        ("Sed do eiusmod tempor incididunt", "SED DO EIUSMOD TEMPOR INCIDIDUNT"),
        ("Ut enim ad minim veniam", "UT ENIM AD MINIM VENIAM"),
        ("Quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat", "QUIS NOSTRUD EXERCITATION ULLAMCO LABORIS NISI UT ALIQUIP EX EA COMMODO CONSEQUAT")
    ])
    def test_to_uppercase(self, text, expected):
        assert to_uppercase(text) == expected

    @pytest.mark.parametrize("expected", [
        "ASD ASDASD"
    ])
    def test_to_uppercase_with_fixture(self, sample_text, expected):
        assert to_uppercase(sample_text.strip()) == expected
