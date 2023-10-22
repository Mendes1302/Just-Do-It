from random import randint

def _guess_number(array, system_choice) -> list:
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


def main()-> None:
    last_number = randint(0, 50)
    numbers_lists = [i for i in range(last_number + 1)]
    size_list = len(numbers_lists)
    system_choice = randint(0, last_number)
    number = _guess_number(numbers_lists[:], system_choice)

    print(f"List original: {numbers_lists}")
    print(f"Size List: {size_list}")
    print(f"System Choice: {system_choice}")
    print(f"Number:   {number}")


if __name__ == '__main__': main()