# NeetCode - Binary Search
# 875. Koko Eating Bananas
# Difficulty : Medium
# Algorithm : Binary search
# Time complexity : O(MlogN), Space complexity : O(1) - N : max(piles), M : len(piles)
# Runtime : 426 ms (85.53%), Memory : 17.89 MB (80.93%)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eating(self, k, piles, target):
            hour = 0
            for pile in piles:
                hour += (pile + k -1) // k
            if hour <= target:
                return True
            else:
                return False

        l, r = 1, max(piles)
        k = r
        while l <= r:
            mid = (l + r) // 2
            if eating(self, mid, piles, h):
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1

        return k
