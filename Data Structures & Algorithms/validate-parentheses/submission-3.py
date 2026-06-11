class Solution:
    def isValid(self, s: str) -> bool:

        valid = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        
        stack = []

        for ch in s:
            if ch not in valid:
                stack.append(ch)
            elif stack and valid[ch] == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0