from typing import Dict, List
class TopologicalSort:
  def __init__(self) -> None:
    self.reverse_post = []
    self.visited = set()
  
  # Time complexity: O(V + E)
  def topological_order(self, adj_list: Dict[int, List[List[int]]]) -> List[int]:
    for v in adj_list.keys():
      if v not in self.visited: 
        self.dfs(adj_list, v)
    return self.reverse_post[::-1]
  
  def dfs(self, adj_list: Dict[int, List[List[int]]], u: int) -> None:
    self.visited.add(u)
    for v, _ in adj_list[u]:
      if v not in self.visited:
        self.dfs(adj_list, v)
    self.reverse_post.append(u)