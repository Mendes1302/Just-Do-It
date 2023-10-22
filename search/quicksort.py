from random import randint
from math import log2

def quicksort(array, size_list) -> list:
    if size_list  < 2: return array
    index = randint(0, len(array)-1)
    pivo = array.pop(index)
    lows = [v for v in array if v <= pivo]
    high = [v for v in array if v > pivo]
    return quicksort(lows, len(lows)) + [pivo] + quicksort(high, len(high))


def main()-> None:
    last_number = randint(3, 25)
    numbers_lists = [randint(0, last_number) for _ in range(last_number + 1)]
    size_list = len(numbers_lists)
    bigO = size_list*log2(size_list)
    sorted_list = quicksort(numbers_lists[:], size_list)
    print(f"List original: {numbers_lists}")
    print(f"List sorted:   {sorted_list}")
    print(f"Big O({size_list} log2 {size_list}) = {round(bigO)}")


if __name__ == '__main__': main()