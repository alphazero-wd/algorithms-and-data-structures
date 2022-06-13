from math import inf
from typing import Dict, List
from heapq import heappush, heappop


class Dijkstra:
    def __init__(self, s: int) -> None:
        self.Q = set()
        self.dist = {}
        self.s = s

    def extract_min(self):
        min_dst = inf
        min_dst_v = None
        for v in self.Q:
            if self.dist[v] < min_dst:
                min_dst = self.dist[v]
                min_dst_v = v
        return min_dst_v

    def dijkstra(self, adj_list: Dict[int, List[List[int]]]) -> Dict[int, int]:
        for v in adj_list.keys():
            self.dist[v] = inf
            self.Q.add(v)

        self.dist[self.s] = 0
        while len(self.Q) > 0:
            u = self.extract_min()
            self.Q.discard(u)

            for v, w in adj_list[u]:
                alt = self.dist[u] + w
                if alt <= self.dist[v]:
                    self.dist[v] = alt
