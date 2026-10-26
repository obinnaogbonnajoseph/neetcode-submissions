# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, pairs: List[Pair], strt: int, mid: int, end: int) -> None:
        L = pairs[strt : mid + 1]
        R = pairs[mid + 1 : end + 1]
        i, j, k = 0, 0, strt
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1

    def mergeSortFn(self, pairs: List[Pair], strt: int, end: int) -> List[Pair]:
        if end - strt + 1 <= 1:
            return pairs
        mid = (strt + end) // 2
        self.mergeSortFn(pairs, strt, mid)
        self.mergeSortFn(pairs, mid + 1, end)

        self.merge(pairs, strt, mid, end)
        return pairs

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        strt, end = 0, len(pairs)
        return self.mergeSortFn(pairs, strt, end)
