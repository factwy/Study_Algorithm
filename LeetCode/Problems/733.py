# explore <Queue & Stack> - Conclusion
# 733. Flood Fill
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        m, n = len(image), len(image[0])
        visited = set([])

        def dfs(x, y):
            nonlocal n, m, image, color
            visited.add((x, y))

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if (nx, ny) in visited:
                    continue
                if image[x][y] == image[nx][ny]:
                    dfs(nx, ny)
            image[x][y] = color

        dfs(sr, sc)
        return image
