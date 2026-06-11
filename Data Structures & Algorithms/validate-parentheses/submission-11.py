class Solution:
    def isValid(self, s: str) -> bool:

        st = []
        parens = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for c in s:
            print(st)
            if not c in parens:
                st.append(c)
            elif st and st[-1] == parens[c]:
                st.pop()
            else:
                return False

        return len(st) == 0
        