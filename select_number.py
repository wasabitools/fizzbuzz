"""A small script which will find numbers divisible by 3 and 5"""


def get_valid_integer(num: int) -> int:
    """It accepts the user input and checks if it is of a valid integer.
    If the user exceeds the range or doesn't add a number an error will be thrown
    and the user will be asked to repeat the task with a number."""
    value = int(input(num))
    try:
        if int(value) in range(1, 101):
            return value
        else:
            print("Please, enter a number between 1 and 100.")
    except ValueError:
        print("Please, enter a valid integer.")


def get_divisible_numbers(start: int, end: int) -> None:
    """Print numbers from x to y with 'fizz' and 'buzz' conditions."""
    for i in range(start, end + 1):
        message = ""
        if i % 3 == 0:
            message += "fizz"
        if i % 5 == 0:
            message += "buzz"
        print(f"{i} {message}")


def main() -> None:
    """Main function to run the logic.
    Adds additional check in case the first input is greater than the second,
    then the range is invalid."""
    try:
        x = get_valid_integer("Please, enter a number from 1 to 100: ")
        y = get_valid_integer("Please, enter another number from 1 to 100: ")

        if x < y:
            print(f"You have selected {x} and {y}. Great choices!\n")
            get_divisible_numbers(x, y)
        else:
            print("The first number should be smaller than the second.")
    except Exception as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    main()
