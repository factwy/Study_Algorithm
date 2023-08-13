# Daily challenge in 2023.08.13
# 2369. Check if There is a Valid Partition For The Array
# Difficulty : Medium
# Algorithm : Heap
# Time complexity : O(NlogN), Space complexity : O(N)
# Runtime : 868 ms (93.08%), Memory : 33.78 MB (47.69%)

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        size = len(nums)
        heap = []
        heapq.heappush(heap, 0)
        numbers = set([0])  # Using combination -> less duplication

        # Time complexity : (NlogN), Space complexity : O(N)
        while heap:
            i = heapq.heappop(heap)

            if i == size:
                return True

            if i < size-1 and (nums[i] == nums[i+1]) and i+2 not in numbers:
                heapq.heappush(heap, i+2)
                numbers.add(i+2)
            
            if i < size-2 and i+3 not in numbers:
                if nums[i] == nums[i+1] == nums[i+2]:
                    heapq.heappush(heap, i+3)
                    numbers.add(i+3)
                elif nums[i]+2 == nums[i+1]+1 == nums[i+2]:
                    heapq.heappush(heap, i+3)
                    numbers.add(i+3)

        return False
