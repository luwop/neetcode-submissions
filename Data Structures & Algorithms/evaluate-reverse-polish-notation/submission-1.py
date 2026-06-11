class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for ch in tokens:
            print(stack)
            if ch in ('-', '+', '/', '*'):
                print(ch)
                rop = stack.pop()
                lop = stack.pop()
                if ch == '+':
                    print(f"{lop} + {rop}")
                    stack.append(lop + rop)
                if ch == '-':
                    print(f"{lop}  {rop}")
                    stack.append(lop - rop)
                if ch == '*':
                    print(f"{lop} + {rop}")
                    stack.append(lop * rop)
                if ch == '/':
                    print(f"{lop} + {rop}")
                    stack.append(int(lop / rop))  
            else:
                stack.append(int(ch))

        return stack[-1]            
