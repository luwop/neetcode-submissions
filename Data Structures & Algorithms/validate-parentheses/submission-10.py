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
            if c in parens:
                if st and st[-1] == parens[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)

        return len(st) == 0
        