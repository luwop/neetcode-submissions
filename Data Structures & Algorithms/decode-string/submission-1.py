class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        counts = []
        n = 0
        for ch in s:
            if ch.isdigit():
                n = n * 10 + int(ch) 
            elif ch == '[':
                counts.append(n)
                stack.append(ch)
                n = 0
            elif ch == ']':
                tmp = []
                while stack and stack[-1] != '[':
                    tmp.append(stack.pop())

                stack.pop()
                mul = counts.pop()
                stack.append(mul * ''.join(tmp[::-1]))
            else:
                stack.append(ch)

        
        return ''.join(stack)

