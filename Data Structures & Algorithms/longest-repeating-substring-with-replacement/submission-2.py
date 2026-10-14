class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, l, res, maxf = ({}, 0, 0, 0)

        for r in range(len(s)):
            char = s[r]
            count[char] = count.get(char, 0) + 1
            maxf = max(maxf, count[char])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
