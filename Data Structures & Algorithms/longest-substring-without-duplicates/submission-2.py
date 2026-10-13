class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, res = 0, 0
        pos = {}
        for R in range(len(s)):
            char = s[R]
            if char in pos:
                L = max(pos[char] + 1, L)
            pos[char] = R
            res = max(res, R - L + 1)
        return res
