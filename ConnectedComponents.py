from typing import Dict, List
class ConnectedComponent:
  def __init__(self) -> None:
    self.count = 0
    self.visited = set()
  
  # Time complexity: O(V + E)
  # Space complexity: O(V + E)
  def count_cc(self, adj_list: Dict[int, List[List[int]]]) -> int:
    for v in adj_list.keys():
      if v not in self.visited:
        self.dfs(adj_list, v)
        self.count += 1
    return self.count

  def dfs(self, adj_list: Dict[int, List[List[int]]], v: int) -> None:
    self.visited.add(v)
    for neighbor in adj_list[v]:
      if neighbor not in self.visited:
        self.dfs(adj_list, neighbor)

