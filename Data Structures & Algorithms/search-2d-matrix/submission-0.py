class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr: List[int], l: int, r: int) -> bool:
            while l <= r:
                mid = (l + r) // 2

                if target < arr[mid]:
                    r = mid - 1
                elif target > arr[mid]:
                    l = mid + 1
                else:
                    return True
            return False

        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            row_m = matrix[m]

            if row_m[0] == target or row_m[-1] == target:
                return True

            if row_m[0] < target and row_m[-1] > target:
                # perform binary search on row_m
                return binary_search(row_m, 0, len(row_m) - 1)

            if target < row_m[0]:
                r = m - 1
            else:
                l = m + 1
        return False
