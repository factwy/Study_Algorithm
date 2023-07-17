# NeetCode - Sliding Window
# 121. Best Time to Buy and Sell Stock
# Difficulty : Easy
# Algorithm : Sliding Window
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 1081 ms (17.98%), Memory : 27.44 MB (23.68%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy, sell = 0, 0
        while sell < len(prices):
            res = max(res, prices[sell]-prices[buy])
            if prices[buy] <= prices[sell]:
                sell += 1
            else:
                buy += 1

        return res
