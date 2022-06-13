from math import inf
from typing import Dict, List


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


class MinHeap:
    def __init__(self) -> None:
        self.items = []

    def swim(self, i: int) -> None:
        while self.parent_index(i) >= 0 and self.parent(i) > self.items[i]:
            self.items[self.parent_index(
                i)], self.items[i] = self.items[i], self.parent(i)
            i = self.parent_index(i)

    def sink(self, i: int) -> None:
        while self.left_child_index(i) < self.size():
            j = self.left_child_index(i)
            if j + 1 < self.size() and self.left_child(i) > self.right_child(i):
                j += 1
            if self.items[i] <= self.items[j]:
                break
            self.items[j], self.items[i] = self.items[i], self.items[j]
            i = j

    def insert(self, val: int) -> None:
        self.items.append(val)
        self.swim(self.size() - 1)

    def del_min(self) -> int:
        self.items[0], self.items[-1] = self.items[-1], self.items[0]
        min_item = self.items.pop()
        self.sink(0)
        return min_item


class DijkstraHeap:
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
