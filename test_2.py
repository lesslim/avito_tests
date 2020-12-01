# -*- coding: utf-8 -*-
import pytest # type: ignore
from morse import decode


@pytest.mark.parametrize(
    "morse, expected",
    [
        ("....- ..---", "42"),
        ("..--..", "?"),
        ("-. ---", "NO"),
    ],
)
def test_decode(morse: str, expected: str):
    assert decode(morse) == expected
