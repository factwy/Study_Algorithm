# Daily challenge in 2023.06.23
# 1027. Longest Arithmetic Subsequence
# difficulty : Medium
# algorithm : dynamic programming
# Runtime : 3749 ms (30.14%), Memory : 36.6 MB (60.83%)
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dif = []
        for _ in range(1001):
            dif.append({})

        nums_len = len(nums)
        for i in range(nums_len):
            for j in range(i+1, nums_len):
                if i not in dif[nums[j] - nums[i] + 500]:
                    dif[nums[j] - nums[i] + 500][i] = j

        answer = 1
        for i in range(1001):
            if not dif[i]:
                continue
            
            dic_list = sorted(list(dif[i].keys()))
            for index in range(len(dic_list)):
                now, size = dic_list[index], 1
                while now in dif[i].keys():
                    next_index = dif[i][now]
                    now, size = dif[i][now], size+1
                answer = max(answer, size)

        return answer
