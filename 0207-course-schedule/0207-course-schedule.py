from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph and indegree
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # Queue of courses with no prerequisites
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0

        while q:
            course = q.popleft()
            taken += 1
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return taken == numCourses
