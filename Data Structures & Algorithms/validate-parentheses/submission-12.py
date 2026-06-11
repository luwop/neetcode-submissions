class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        
        st = []

        for char in s:
            if char in hashmap:
                if st and st[-1] == hashmap[char]:
                    st.pop()
                    continue
                else:
                    return False

            st.append(char)

        return len(st) == 0
            