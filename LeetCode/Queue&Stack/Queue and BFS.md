# Queue and BFS
Breadth-first search(BFS) is an algorithm to traverse or search in data structures like a tree or a graph
BFS find the shortest path, from a start node to a target node

### A Queue and BFS
- Similar to tree's level-order traversal, the nodes closer to the root node will be traversed earlier
- It is worth noting that the newly-added nodes will not be traversed immedialtely but will be processed in the next round
- The processing order of the nodes is the exact same order as how the were added to the queue

### A Number of Islands
```python
class Solution:
    def numIslands(self, grid: List[List[str]]):
        m, n = len(grid), len(grid[0])
        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            grid[x][y] = "2"
            
            dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        continue
                    if grid[nx][ny] != "1":
                        continue
                    grid[nx][ny] = "2"
                    check = True
                    queue.append((nx, ny))
        
        answer = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    bfs(x, y)
                    answer += 1
                    
        return answer
```

## A Open the Lock
```python
class Solution:
    def openLock(self, deadends: List[str], target: str):
        deadends = set(map(int, deadends))
        time = [-1] * 10000
        time[0] = 0
        
        def time_cnt(num, next_num):
            nonlocal time, deadends
            
            if time[next_num] == -1 or time[num] + 1 < time[next_num]:
                if next_num not in deadends:
                    time[next_num] = time[num] + 1
                    return True
            return False
        
        def bfs(target):
            nonlocal time
            
            queue = deque()
            queue.append(0)
            
            while queue:
                number = queue.popleft()
                if number == target:
                    continue
                
                multi = 1000
                while multi >= 1:
                    next_number = number + multi
                    if number // multi % 10 == 9:
                        next_number -= (multi * 10)                  
                    if time_cnt(number, next_number):
                        queue.append(next_number)
                            
                    next_number = number - multi
                    if number // multi % 10 == 0:
                        next_number += (multi * 10)  
                    if time_cnt(number, next_number):
                        queue.append(next_number)
                            
                    multi = multi // 10
            
            return time[target]
        
        answer = bfs(int(target))
        if 0 in deadends:
            answer = -1
            
        return answer
```
