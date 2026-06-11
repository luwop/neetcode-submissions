class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for entry in operations:
            if entry.isnumeric():
                stack.append(int(entry))
            elif entry[0] == '-':
                stack.append(-1 * int(entry[1:]))
            else:
                if entry == '+':
                    stack.append(stack[-1] + stack[-2])
                elif entry == 'D':
                    stack.append(stack[-1] * 2)
                else:
                    stack.pop()

        return sum(stack)