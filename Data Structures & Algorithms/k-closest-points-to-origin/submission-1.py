class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2

        def partition(l: int, r: int) -> int:
            left = l
            pivotdx = euclidean(points[r])
            for i in range(l, r):
                if euclidean(points[i]) < pivotdx:
                    points[left], points[i] = points[i], points[left]
                    left += 1
            points[r], points[left] = points[left], points[r]
            return left

        pivot = len(points)
        l = 0
        r = len(points) - 1

        while pivot != k:
            pivot = partition(l, r)
            if pivot < k:
                l = pivot + 1
            else:
                r = pivot - 1
        return points[:k]
