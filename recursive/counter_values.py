from random import randint


def counter(number_list, n) -> int:
    """
    Recursively counts the number of elements in a list.

    Args:
    - number_list (list): The list of numbers to count.
    - n (int): A parameter used in the recursive counting (default: 0).

    Returns:
    - int: The total count of elements in the list.
    """
    if number_list == []:
        return 0
    number_list.pop(0)
    return 1 + counter(number_list, n + 1)


def main() -> None:
    """
    Main function to generate a random list of numbers and count its size.

    This function generates a random list of numbers, counts its size using the 'counter' function,
    and checks if the result matches the actual size of the list.
    """
    last_number = randint(3, 150)
    numbers_lists = [randint(0, last_number) for _ in range(last_number + 1)]

    size_list = len(numbers_lists)
    results = counter(numbers_lists[:], 0)
    print(f"Size List: {results}")
    print(f"[Size List] Check Values: {results == size_list}")


if __name__ == '__main__':
    main()
