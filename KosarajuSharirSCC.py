from typing import Dict, List
from TopologicalSort import TopologicalSort

class KosarajuSharirSCC:
  def __init__(self) -> None:
    self.visited = set()
    self.count = 0

  # Time complexity: O(V + E)
  def count_scc(self, adj_list: Dict[int, List[List[int]]], rev_adj_list: Dict[int, List[List[int]]]):
    self.reverse_post = TopologicalSort().topological_order(rev_adj_list)
    for v in self.reverse_post:
      if v not in self.visited: 
        self.dfs(adj_list, v)
        self.count += 1
    return self.count
  
  def dfs(self, adj_list: Dict[int, List[List[int]]], u: int):
    self.visited.add(u)
    for v, _ in adj_list[u]:
      if v not in self.visited:
        self.dfs(adj_list, v)