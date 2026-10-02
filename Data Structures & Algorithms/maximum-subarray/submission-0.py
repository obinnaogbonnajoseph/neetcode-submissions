class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_n = nums[0]
        cur = 0
        for n in nums:
            cur = max(cur, 0) + n
            max_n = max(cur, max_n)
        return max_n
