"""Test module for select_number.py"""

import pytest
from select_number import (
    get_divisible_numbers,
    get_valid_integer,
    main,
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


def test_get_divisible_numbers(capsys):
    """Tests the happy scenario where all conditions are satisfied."""
    get_divisible_numbers(1, 15)
    captured = capsys.readouterr()
    expected_output = "1 \n2 \n3 fizz\n4 \n5 buzz\n6 fizz\n7 \n8 \n9 fizz\n10 buzz\n11 \n12 fizz\n13 \n14 \n15 fizzbuzz\n"
    assert captured.out == expected_output


def test_main_happy_scenario(monkeypatch, capsys):
    """Tests happy scenario for main"""
    input_values = iter(["1", "7"])
    monkeypatch.setattr("builtins.input", lambda _: next(input_values))
    main()
    captured = capsys.readouterr()
    expected_output = "You have selected 1 and 7. Great choices!\n\n1 \n2 \n3 fizz\n4 \n5 buzz\n6 fizz\n7 \n"
    assert captured.out == expected_output


def test_main_greater_first_number_scenario(monkeypatch, capsys):
    """Tests scenario where first input number is greater than second."""
    input_values = iter(["7", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(input_values))
    main()
    captured = capsys.readouterr()
    expected_output = "The first number should be smaller than the second.\n"
    assert captured.out == expected_output
