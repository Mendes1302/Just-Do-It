from random import randint


def _get_high_value(numbers_lists, high) -> int:
    """
    Recursively finds the highest value in a list.

    Args:
    - numbers_lists (list): The list of numbers to find the highest value in.
    - high (int): The current highest value found in the list (default: 0).

    Returns:
    - int: The highest value in the list.
    """
    if numbers_lists == []:
        return high
    value = numbers_lists.pop(0)
    if value > high:
        high = value
    return _get_high_value(numbers_lists, high)


def main() -> None:
    """
    Main function to generate a random list of numbers and find the highest value.

    This function generates a random list of numbers, finds the highest value using the '_get_high_value' function,
    and checks if the result matches the actual highest value in the list.
    """
    last_number = randint(3, 150)
    numbers_lists = [randint(0, last_number) for _ in range(last_number + 1)]
    
    high = _get_high_value(numbers_lists[:], 0)
    print(f"HIGH: {high}")
    print(f"[HIGH]      Check Values: {high == max(numbers_lists)}")


if __name__ == '__main__':
    main()
