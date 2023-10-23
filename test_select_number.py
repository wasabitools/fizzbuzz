"""Test module for select_number.py"""

import pytest
from select_number import (
    get_valid_integer,
)


def test_get_valid_integer_in_range(monkeypatch):
    """Tests happy case where an integer is given"""
    value = monkeypatch.setattr("builtins.input", lambda _: "3")
    result = get_valid_integer(value)
    assert result == 3


def test_get_valid_integer_out_of_range(monkeypatch, capsys):
    """Tests that if an out of range integer is given the appropriate
    print statement will be printed."""
    value = monkeypatch.setattr("builtins.input", lambda _: "0")
    get_valid_integer(value)
    captured = capsys.readouterr()
    assert "Please, enter a number between 1 and 100.\n" == captured.out


def test_get_valid_integer_invalid_input(monkeypatch):
    """Tests that a ValueError will be raised if a string is given."""
    value = monkeypatch.setattr("builtins.input", lambda _: "tt")
    with pytest.raises(ValueError):
        get_valid_integer(value)


def test_get_valid_integer_invalid_input_float(monkeypatch):
    """Tests that a ValueError will be raised if a float is given."""
    value = monkeypatch.setattr("builtins.input", lambda _: "4.8")
    with pytest.raises(ValueError):
        get_valid_integer(value)


def test_get_valid_integer_invalid_input_none(monkeypatch):
    """Tests that a TypeError will be raised if nothing is given."""
    value = monkeypatch.setattr("builtins.input", lambda _: None)
    with pytest.raises(TypeError):
        get_valid_integer(value)