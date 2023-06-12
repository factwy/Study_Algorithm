# Daily challenge in 2023.06.12
# 228. Summary Ranges
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        arr = []
        for num in nums:
            if not arr:
                arr.append([num])
            elif num-1 == arr[-1][0]:
                arr[-1] += [num]
            elif len(arr[-1]) > 1 and num-1 == arr[-1][1]:
                arr[-1][1] = num
            else:
                arr.append([num])
        answer = []
        for integer in arr:
            if len(integer) == 1:
                answer += [str(integer[0])]
            else:
                answer += [str(integer[0]) + "->" + str(integer[1])]
        return answer
