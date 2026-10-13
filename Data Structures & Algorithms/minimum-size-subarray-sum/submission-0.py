class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, cur_sum, res = (0, 0, float("inf"))
        for R in range(len(nums)):
            cur_sum += nums[R]
            while cur_sum >= target:
                res = min(res, R - L + 1)
                cur_sum -= nums[L]
                L += 1
        return 0 if res == float("inf") else res
