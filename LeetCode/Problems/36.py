# NeetCode - Arrays & Hashing
# 36. Valid Sudoku
# Difficulty : Medium
# Algorithm : Array
# Time complexity : O(N), Space Complexity : O(N)
# Runtime : 113 ms (78.90%), Memory : 16.1 MB (98.74%)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set([]) for _ in range(9)]
        col = [set([]) for _ in range(9)]
        box = [set([]) for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                    
                if num in row[i]:
                    return False
                else:
                    row[i].add(num)

                if num in col[j]:
                    return False
                else:
                    col[j].add(num)

                box_index = (i//3*3) + (j//3)
                if num in box[box_index]:
                    return False
                else:
                    box[box_index].add(num)

        return True
