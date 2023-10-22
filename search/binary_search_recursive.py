from random import randint


def _guess_number(array, system_choice) -> list:
    """
    Recursively attempts to guess a number chosen by the system from a sorted list.

    Args:
    - array (list): The sorted list of numbers to choose from.
    - system_choice (int): The number chosen by the system.

    Returns:
    - int: The guessed number if found, or None if not found.
    """
    size_list = len(array)
    n = size_list // 2
    number = array[n]
    if system_choice == number:
        return number
    elif system_choice > number:
        array = array[n:]
    elif system_choice < number:
        array = array[:n]
    return _guess_number(array, system_choice)


def main() -> None:
    """
    Main function to simulate a system choosing a number and attempting to guess it.

    This function generates a sorted list of numbers and a number chosen by the system.
    It then attempts to guess the system's chosen number using the '_guess_number' function.
    The function displays the original list, its size, the system's choice, and the guessed number.
    """
    last_number = randint(0, 50)
    numbers_lists = [i for i in range(last_number + 1)]
    size_list = len(numbers_lists)
    system_choice = randint(0, last_number)
    number = _guess_number(numbers_lists[:], system_choice)

    print(f"List original: {numbers_lists}")
    print(f"Size List: {size_list}")
    print(f"System Choice: {system_choice}")
    print(f"Number:   {number}")


if __name__ == '__main__':
    main()
