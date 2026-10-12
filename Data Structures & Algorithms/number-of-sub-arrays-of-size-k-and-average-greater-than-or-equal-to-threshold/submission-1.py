class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res, cur_sum = (0, sum(arr[: k - 1]))
        for L in range(len(arr) - k + 1):
            cur_sum += arr[L + k - 1]
            if (cur_sum / k) >= threshold:
                res += 1
            cur_sum -= arr[L]
        return res
