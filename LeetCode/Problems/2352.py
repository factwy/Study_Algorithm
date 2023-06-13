# Daily challenge in 2023.06.13
# 2352. Equal Row and Column Pairs
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # brute force
        n = len(grid)
        cnt = 0
        for x in range(n):
            for y in range(n):
                row, col = [], []
                for i in range(n):
                    row.append(grid[x][i])
                    col.append(grid[i][y])
                if row == col:
                    cnt += 1
        return cnt

  # solve with brute force algorithm
  # need to solve with trie data structure
