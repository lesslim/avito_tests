import pytest  # type: ignore
from one_hot_encoder import fit_transform  # type: ignore


def test_list():
    """Аргумент функции - список."""
    assert fit_transform(["a", "b", "c"]) == [
        ("a", [0, 0, 1]),
        ("b", [0, 1, 0]),
        ("c", [1, 0, 0]),
    ]


def test_str():
    """Аргумент функции - строки."""
    assert fit_transform("a", "b", "c") == [
        ("a", [0, 0, 1]),
        ("b", [0, 1, 0]),
        ("c", [1, 0, 0]),
    ]


def test_empty_list():
    """Аргумент функции - пустой список."""
    assert fit_transform([]) == []


def test_bad_input():
    """Аргумент функции невалидный - числа."""
    with pytest.raises(TypeError):
        fit_transform(1, 2)


def test_empty_input():
    """Функция без аргумента."""
    with pytest.raises(TypeError):
        assert fit_transform()


def test_not_in():
    """В результате нет значения."""
    assert (1, [0, 2]) != fit_transform([1, 2, 1])
