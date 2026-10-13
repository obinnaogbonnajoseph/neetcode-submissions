class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, res = 0, 0
        cur_set = set()
        for R in range(len(s)):
            while s[R] in cur_set:
                cur_set.remove(s[L])
                L += 1
            res = max(res, R - L + 1)
            cur_set.add(s[R])
        return res
