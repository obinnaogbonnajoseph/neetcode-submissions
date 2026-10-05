class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        num_sub_arrays, L, cur_avg_sum = (0, 0, 0)
        for R in range(len(arr)):
            cur_avg_sum += arr[R]
            if R - L + 1 == k:
                cur_avg = cur_avg_sum / k
                num_sub_arrays = num_sub_arrays + 1 if cur_avg >= threshold else num_sub_arrays
                cur_avg_sum -= arr[L]
                L += 1
        return num_sub_arrays
