from queue import Queue
from typing import List, Dict, Set


class GraphSearch:
    def dfs(self, adj_list: Dict[int, List[List[int]]], u: int, visited: Set = set()) -> None:
        print(u, end=" ")
        visited.add(u)
        for neighbor in adj_list[u]:
            if neighbor not in visited:
                self.dfs(adj_list, neighbor, visited)

    def bfs(self, adj_list: Dict[int, List[List[int]]], s: int) -> None:
        visited = set()
        queue = Queue()
        queue.put(s)
        visited.add(s)
        while not queue.empty():
            u = queue.get()
            print(u, end=' ')
            for neighbor in adj_list[u]:
                if neighbor not in visited:
                    queue.put(neighbor)
                    visited.add(neighbor)
