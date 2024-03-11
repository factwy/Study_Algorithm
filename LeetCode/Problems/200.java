/*
200. Number of Islands
Difficulty : Medium
Algorithm : Linked List, Queue
Time complexity : O(N^2), Space complexity : O(N^2)
Runtime : 5 ms (32.15), Memory : 48.36 MB (99.06%)
*/

import java.util.*;

class Solution {
    char[][] graph;

    public int numIslands(char[][] grid) {
        int cnt = 0;

        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++) {
                if(grid[i][j] == '0')
                    continue;
                bfs(grid, i, j);
                cnt++;
            }
        }

        return cnt;
    }

    public void bfs(char[][] graph, int x, int y) {
        Queue<int[]> q = new LinkedList();

        int[] dx = {0, -1, 0, 1};
        int[] dy = {-1, 0, 1, 0};
        int m = graph.length, n = graph[0].length;
        
        graph[x][y] = '0';
        q.offer(new int[]{x, y});

        while(q.isEmpty() != true) {
            int[] val = q.poll();
            x = val[0];
            y = val[1];

            for(int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(nx < 0 || nx >= m || ny < 0 || ny >= n)
                    continue;
                if(graph[nx][ny] == '0')
                    continue;

                graph[nx][ny] = '0';
                q.offer(new int[]{nx, ny});
            }
        }
    }
}
