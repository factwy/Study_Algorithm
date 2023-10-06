"""
Daily challenge in 2023.10.06
343. Integer Break
Difficulty : Medium
Algorithm : Dynamic Programming
Time complexity : O(N), Space complexity : O(N)
Runtime : 47 ms (17.49%), Memory : 16.18 MB (85.57%)
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1

        prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
        dp = [0] * (n+1)

        for p in prime:
            if p >= n:
                break
            dp[p] = p

        for x in range(2, n+1):
            dp[x] = max(dp[x], dp[x-1])
            for p in prime:  
                if p >= x:
                    break
                dp[x] = max(dp[x], p * dp[x-p])

        return dp[n]
