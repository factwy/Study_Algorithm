# Daily challenge (2023.06.20)
# 2090. K Radius Subarray Averages
# difficulty : Medium
# algorithm : Prefix Sum, Queue
# Runtime : 1735ms(40.53%), Memory : 31MB(99.85%)
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        queue = deque()
        prefix = 0
        nums_len = len(nums)

        for i in range(k):
            if i >= nums_len:
                break
            queue.append(nums[i])
            prefix += nums[i]

        for i in range(nums_len):
            if i+k < nums_len:
                queue.append(nums[i+k])
                prefix += nums[i+k]

            if i-k < 0 or i+k >= nums_len:
                nums[i] = -1
                continue

            nums[i] = prefix // (2*k + 1)
            prefix -= queue.popleft()
            
        return nums
