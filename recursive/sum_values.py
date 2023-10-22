from random import randint


def soma(number_list) -> int:
    if len(number_list) == 0 : return 0
    value = number_list.pop(0)
    return value + soma(number_list)


def main() -> None:
    last_number = randint(3, 150)
    numbers_lists = [randint(0, last_number) for _ in range(last_number + 1)]

    sum_value = soma(numbers_lists[:])
    print(f"Sum: {sum_value}")
    print(f"[Sum]       Check Values: {sum_value == sum(numbers_lists)}")


if __name__ == '__main__': main()