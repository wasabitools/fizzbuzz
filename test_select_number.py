"""Test module for select_number.py"""

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


def test_get_valid_integer_invalid_input(monkeypatch, capsys):
    """Tests that a ValueError will be raised if a string is given."""
    value = monkeypatch.setattr("builtins.input", lambda _: "tt")
    get_valid_integer(value)
    captured = capsys.readouterr()
    assert "Please, enter a valid integer.\n" == captured.out


def test_get_valid_integer_invalid_input_float(monkeypatch, capsys):
    """Tests that a ValueError will be raised if a float is given."""
    value = monkeypatch.setattr("builtins.input", lambda _: "4.8")
    get_valid_integer(value)
    captured = capsys.readouterr()
    assert "Please, enter a valid integer.\n" == captured.out


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


def test_main_one_non_number_first_scenario(monkeypatch, capsys):
    """Tests scenario where one input is not a number."""
    input_values = iter(["b", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(input_values))
    main()
    captured = capsys.readouterr()
    expected_output = "Please, enter a valid integer.\nSomething is not right! Please check your answers.\n"
    assert captured.out == expected_output


def test_main_one_non_number_second_scenario(monkeypatch, capsys):
    """Tests scenario where one input is not a number."""
    input_values = iter(["4", "g"])
    monkeypatch.setattr("builtins.input", lambda _: next(input_values))
    main()
    captured = capsys.readouterr()
    expected_output = "Please, enter a valid integer.\nSomething is not right! Please check your answers.\n"
    assert captured.out == expected_output


def test_main_non_numbers_scenario(monkeypatch, capsys):
    """Tests scenario where no input is a number."""
    input_values = iter(["b", "c"])
    monkeypatch.setattr("builtins.input", lambda _: next(input_values))
    main()
    captured = capsys.readouterr()
    expected_output = "Please, enter a valid integer.\nPlease, enter a valid integer.\nSomething is not right! Please check your answers.\n"
    assert captured.out == expected_output


def test_main_out_of_range_numbers_scenario(monkeypatch, capsys):
    """Tests scenario where no input is a number."""
    input_values = iter(["0", "102"])
    monkeypatch.setattr("builtins.input", lambda _: next(input_values))
    main()
    captured = capsys.readouterr()
    expected_output = "Please, enter a number between 1 and 100.\nPlease, enter a number between 1 and 100.\nSomething is not right! Please check your answers.\n"
    assert captured.out == expected_output
