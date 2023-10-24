# FizzBuzz Number Selector

A small Python script that takes two integers within the range of 1 to 100, loops through this range, and prints out the integers. Additionally, it adds 'fizz' if the integer is divisible by 3 and 'buzz' if divisible by 5.

Prerequisites
 
 - Python 3.x
 - Pip

 For installation instructions, check here: https://pip.pypa.io/en/stable/installation/

Installation
 
  - Clone the repository, as per github instructions.

 - Navigate to the project directory:
```
cd fizzbuzz
```

- Install project dependencies:
```
pip install -r requirements.txt
```
- Run the script:

```
python3 select_number.py
```

Usage

    When you run the script, it will prompt you to enter two integers. Make sure these integers are within the range of 1 to 100. The script will validate your input to ensure it's a valid integer and within the specified range.

    If the first input is less than the second input, it will print the selected range of numbers with 'fizz' and 'buzz' conditions. If the first input is greater or equal to the second input, you'll be prompted to enter valid inputs.

    The script will then loop through the selected range, printing each number and adding 'fizz' if it's divisible by 3 and 'buzz' if divisible by 5.

Tests

This project includes a set of tests to ensure its functionality. You can run the tests using the following command:

```
pytest test_select_number.py
```

The tests cover various scenarios, including valid and invalid input, as well as the correct generation of 'fizz' and 'buzz' for numbers in the specified range.

Contributing

If you want to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Make sure to follow the established coding style and conventions.
