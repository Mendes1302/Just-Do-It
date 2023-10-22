from random import randint


def counter(number_list, n) -> int:
    if number_list == []: return 0
    number_list.pop(0)
    return 1 + counter(number_list, n+1)


def main() -> None:
    last_number = randint(3, 150)
    numbers_lists = [randint(0, last_number) for _ in range(last_number + 1)]

    size_list = len(numbers_lists)
    results = counter(numbers_lists[:], 0)
    print(f"Size List: {results}")
    print(f"[Size List] Check Values: {results == size_list}")



if __name__ == '__main__': main()