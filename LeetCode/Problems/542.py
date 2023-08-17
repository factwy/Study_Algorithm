# Daily challenge in 2023.08.17
# 542. 01 Matrix
# Difficulty : Medium
# Algorithm : BFS
# Time complexity : O(N*M), Space complexity : O(N*M)
# Runtime : 538 ms (84.00%), Memory : 20.27 MB (33.30%)

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        graph = [[0] * n for _ in range(m)]
        arr = []
        dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

        for a in range(m):
            for b in range(n):
                if not mat[a][b]:
                    arr.append((a, b, 0))

        queue = deque(arr)
        while queue:
            x, y, num = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue

                if mat[nx][ny]:
                    if graph[nx][ny] == 0 or graph[nx][ny] > num + 1:
                        graph[nx][ny] = num + 1
                        queue.append((nx, ny, num+1))

        return graph
