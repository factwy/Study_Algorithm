"""
Daily challenge in 2023.10.13
746. Min Cost Climbing Stairs
Difficulty : Easy
Algorithm : Dynamic Programming
Time complexity : O(N), Space complexity : O(N)
Runtime : 62 ms (51.66%), Memory : 16.4 MB (52.53%)
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        
        for i, c in enumerate(cost):
            if i < 2:
                continue
            dp[i] = min(dp[i-1], dp[i-2]) + c

        return min(dp[-1], dp[-2])
