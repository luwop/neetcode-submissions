class Solution:
    def climbStairs(self, n: int) -> int:
        # State: dp(i) = # ways to climb to the ith step.

        # Function: dp(i) = dp(i - 1) + dp(i - 2)
        # List: dp[i] = dp[i - 1] + dp[i - 2]
        # Base Case: if i == 1 return 1 or if i == 2 return 2
        dp  = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(dp)):
            print(dp)
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]