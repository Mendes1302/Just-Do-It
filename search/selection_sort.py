from random import randint

def _get_low_value(numbers_lists):
    low = numbers_lists[0]
    index = 0
    for j in range(len(numbers_lists)):
        value = numbers_lists[j]
        if low >= value:
            low, index = value, j
    return index


def _get_high_value(numbers_lists):
    high = numbers_lists[0]
    index = 0
    for j in range(len(numbers_lists)):
        value = numbers_lists[j]
        if high <= value:
            high, index = value, j
    return index


def _sort_values_desc(numbers_lists, size_list) -> None:
    size_list = len(numbers_lists)
    high_list = []
    for _ in range(size_list):
        high = _get_high_value(numbers_lists)
        high_list.append(numbers_lists.pop(high))
    print(f"Values Sorted (high to low):\n{high_list}\n\n")


def _sort_values_asc(numbers_lists, size_list) -> None:
    low_list = []
    for _ in range(size_list):
        low = _get_low_value(numbers_lists)
        low_list.append(numbers_lists.pop(low))
    print(f"Values Sorted (low to high):\n{low_list}\n\n")

        
def main() -> None:
    last_number = randint(3, 150)
    numbers_lists = [randint(0, last_number) for _ in range(last_number + 1)]
    size_list = len(numbers_lists)

    _sort_values_asc(numbers_lists[:], size_list)
    _sort_values_desc(numbers_lists[:], size_list)

    print(f"Size List: {size_list}")
    print(f"Big O(n**2): {size_list**2}")


if __name__ == '__main__':
    main()
