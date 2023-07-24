# Daily challenge in 2023.07.24
# 50. Pow(x, n)
# Difficulty : Medium
# Algorithm : Recursion
# Time complexity : O(logN), Space complexity : O(logN)
# Runtime : 53 ms (18.45%), Memory : 16.35 MB (41.10%)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1.0
        elif n == 1:
            return x

        if n < 0:
            return self.myPow(1/x, -n)
        elif n % 2 == 0:
            return self.myPow(x*x, n//2)
        else:
            return x * self.myPow(x*x, n//2)
