from random import randint


def _get_high_value(numbers_lists, high) -> int:
    if numbers_lists == []: return high
    value = numbers_lists.pop(0)
    if value > high:
        high = value
    return _get_high_value(numbers_lists, high)


def main() -> None:
    last_number = randint(3, 150)
    numbers_lists = [randint(0, last_number) for _ in range(last_number + 1)]
    
    high = _get_high_value(numbers_lists[:], 0)
    print(f"HIGH: {high}")
    print(f"[HIGH]      Check Values: {high == max(numbers_lists)}")



if __name__ == '__main__': main()