# NeetCode - Sliding Window
# 239. Sliding Window Maximum
# Difficulty : Hard
# Algorithm : Sliding Window, Monotonic Queue
# Time complexity : O(N), Space complexity : O(K)
# Runtime : 1586 ms (97.35%), Memory : 33.18 MB (40.67%)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_queue = deque()    # index
        res = []

        for i in range(k-1):
            if mono_queue:
                while mono_queue and nums[mono_queue[-1]] < nums[i]:
                    mono_queue.pop()
            mono_queue.append(i)


        # Time complexity : O(N), Space complexity : O(K)
        for i in range(k-1, len(nums)):
            if mono_queue:
                while mono_queue and nums[mono_queue[-1]] < nums[i]:
                    mono_queue.pop()
            mono_queue.append(i)

            res.append(nums[mono_queue[0]])
            
            while mono_queue and mono_queue[0] <= i - (k-1):
                mono_queue.popleft()

        return res
# Heap            - (Runtime : 2701 ms, Memory : 41.4 MB)
# Monotonic Queue - (Runtime : 1586 ms, Memory : 33.18 MB)
