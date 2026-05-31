from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            q = deque(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                        if heights[nr][nc] >= heights[r][c]:
                            visited.add((nr,nc))
                            q.append((nr,nc))
            return visited

        pacific = bfs([(0,c) for c in range(cols)] + [(r,0) for r in range(rows)])
        atlantic = bfs([(rows-1,c) for c in range(cols)] + [(r,cols-1) for r in range(rows)])

        return list(pacific & atlantic)
