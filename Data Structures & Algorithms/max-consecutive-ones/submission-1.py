class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r, cnt = (0, 0, 0)

        while r < len(nums):
            if nums[r] == 0:
                cnt = max(cnt, r - l)
                l = r + 1
            r += 1
        return max(cnt, r - l)
