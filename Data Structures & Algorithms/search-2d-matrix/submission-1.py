class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLUMNS - 1

        while l <= r:
            m = (l + r) // 2
            row, column = m // COLUMNS, m % COLUMNS
            if target > matrix[row][column]:
                l = m + 1
            elif target < matrix[row][column]:
                r = m - 1
            else:
                return True
        return False
