class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for entry in operations:
            if entry == '+':
                stack.append(stack[-1] + stack[-2])
            elif entry == 'D':
                stack.append(2 * stack[-1])
            elif entry == 'C':
                stack.pop()
            else:
                stack.append(int(entry))

        return sum(stack)