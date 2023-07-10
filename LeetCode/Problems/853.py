# NeetCode - Stack
# 853. Car Fleet
# Difficulty : Medium
# Algorithm : Stack
# Time complexity : O(NlogN), Space complexity : O(N)
# Runtime : 897 ms (80.54%), Memory : 39.2 MB (29.65%)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = [(p, s) for p, s in zip(position, speed)]
        car.sort(key = lambda x : x[0], reverse = True)
        
        stack = []
        for p, s in car:
            t = (target - p) / s
            if stack:
                if t > stack[-1]:
                    stack.append(t)
            else:
                stack.append(t)

        return len(stack)
# reference Neetcode
