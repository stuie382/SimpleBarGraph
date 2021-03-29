import pytest

from simple_bar_chart.simple_bar import SimpleBar


@pytest.fixture
def uut():
    return SimpleBar()


class TestSimpleBar:

    def test_empty_input(self, uut):
        uut.analyise("")
        result = uut.format_output()
        assert result == ""

    def test_simple_input(self, uut):
        uut.analyise("p")
        result = uut.format_output()
        assert result == "p: p\n"

    def test_multiple_same_char_input(self, uut):
        uut.analyise("bmm")
        result = uut.format_output()
        assert result == "b: b\nm: m, m\n"

    def test_sentence(self, uut):
        uut.analyise("I like apples")
        result = uut.format_output()
        assert result == "i: i, i\nl: l, l\nk: k\ne: e, e\na: a\np: p, p\ns: s\n"
