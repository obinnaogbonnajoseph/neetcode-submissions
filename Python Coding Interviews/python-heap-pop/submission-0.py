from heapq import heappop
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    arr = []
    while len(heap) > 0:
        arr.append(heappop(heap))
    return arr

# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
