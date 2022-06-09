from math import inf
from typing import Dict, List
from heapq import heappush, heappop

class Dijkstra:
  def __init__(self, s: int) -> None:
    self.Q = []
    self.dist = {}
    self.s = s

  # Time complexity: O(V^2 + E), O(Elog2(V)) if using a heap
  def dijkstra(self, adj_list: Dict[int, List[List[int]]]) -> Dict[int, int]:
    for v in adj_list.keys():
      self.dist[v] = inf
      heappush(self.Q, v)
    
    self.dist[self.s] = 0
    while len(self.Q) > 0:
      u = heappop(self.Q)

      for v, w in adj_list[u]:
        alt = self.dist[u] + w
        if alt <= self.dist[v]:
          self.dist[v] = alt