class Solution:
    def climbStairs(self, n: int) -> int:
        # State: dp(i) = # ways to climb to the ith step.

        # Reccurence: dp(i) = dp(i - 1) + dp(i - 2)

        # Base Case: if i == 1 return 1 or if i == 2 return 2
        cache = {}
        def dp(i):
            if i <= 2:
                return i
            if i in cache:
                return cache[i]
            ans = dp(i - 1) + dp(i - 2)
            cache[i] = ans
            return ans

        return dp(n)