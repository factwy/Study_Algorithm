# Daily challenge in 2023.07.22
# 688. Knight Probability in Chessboard
# Difficulty : Medium
# Algorithm : Dynamic Programming
# Time complexity : O(K*N^2), Space complexity : O(N^2)
# Runtime : 215 ms (82.08%), Memory : 16.50 MB (90.56%)
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dx = [2, 2, 1, 1, -1, -1, -2, -2]
        dy = [1, -1, 2, -2, 2, -2, 1, -1]

        # Space complexity : O(N^2)
        position = [[0]*n for _ in range(n)]
        position[row][column] = 1

        # Time complexity : O(K*N^2)
        for _ in range(k):
            next_position = [[0]*n for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    if position[x][y]:
                        for i in range(8):
                            nx, ny = x + dx[i], y + dy[i]
                            if 0 <= nx < n and 0 <= ny < n:
                                next_position[nx][ny] += position[x][y]

            position = next_position

        possible_way = 0
        for p in position:
            possible_way += sum(p)

        if possible_way:
            return possible_way / (8 ** k)
        else:
            return 0
