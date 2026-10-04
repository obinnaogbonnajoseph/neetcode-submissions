from typing import List


def sort_words(words: List[str]) -> List[str]:
    sorted = words
    words.sort()
    return sorted


def sort_numbers(numbers: List[int]) -> List[int]:
    sorted_num = numbers
    sorted_num.sort()
    return sorted_num


def sort_decimals(numbers: List[float]) -> List[float]:
    sorted_dec = numbers
    sorted_dec.sort()
    return sorted_dec


# do not modify below this line
print(
    sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"])
)

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
