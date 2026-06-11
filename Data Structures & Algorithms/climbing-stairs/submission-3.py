class Solution:
    def climbStairs(self, n: int) -> int:
        """
        dp(i) = number of ways to reach the ith step
        dp(i) = dp(i - 1) + dp(i - 2)
        BC: if i == 0 return 1, i < 0 return 0
        """
        cache = {}
        def memo(i):
            if i == 0:
                return 1
            if i < 0:
                return 0

            if i in cache:
                return cache[i]

            cache[i] = memo(i - 1) + memo(i - 2)
            return cache[i]

        return memo(n)
        


        