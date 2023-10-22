from random import randint
from math import log2

def _guess_number(numbers_lists, system_choice) -> None:
    """
    A function to guess a number in a given list using binary search.
    
    Parameters:
        numbers_lists (list): The list of numbers to search in.
        system_choice (int): The number the system is trying to guess.
        
    Returns:
        None
    """
    size_list = len(numbers_lists)
    size_first_list = size_list
    bigO = log2(size_list)
    attempt = 0
    for i in range(round(bigO) + 1):
        size_list = len(numbers_lists)
        n = size_list // 2
        number = numbers_lists[n]
        print(f"\tAttempt: {i + 1}")
        print(f"\tNumber: {number}")
        
        if system_choice == number:
            attempt = i + 1
            print("\n\tFinished !!!!!!!!".upper())
            break
        elif system_choice > number:
            numbers_lists = numbers_lists[n:]
        elif system_choice < number:
            numbers_lists = numbers_lists[:n]
        print()
    
    print('\n\n')
    print(f"System Choice: {system_choice}")
    print(f"Size List: {size_first_list}")
    print(f"Number Attempt: {attempt}")
    print(f"Big O(log2 {size_first_list}) = {round(bigO)}")

def main() -> None:
    """
    The main function that generates a random number and performs binary search to guess it.
    
    Parameters:
        None
        
    Returns:
        None
    """
    last_number = randint(100, 4896884)
    system_choice = randint(0, last_number)
    numbers_lists = [n for n in range(last_number + 1)]
    _guess_number(numbers_lists, system_choice)

if __name__ == '__main__':
    main()
