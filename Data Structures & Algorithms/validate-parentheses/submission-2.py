class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_set = {"}": "{", ")": "(", "]": "["}
        for char in s:
            if char in hash_set:
                if not stack or stack.pop() != hash_set[char]:
                    return False
            else:
                stack.append(char)
        return not stack
