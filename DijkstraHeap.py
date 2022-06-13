from math import inf
from typing import Dict, List, Tuple


class MinHeap:
    def __init__(self) -> None:
        self.items: List[Tuple[int]] = []

    def parent_index(self, i):
        return (i - 1) // 2

    def left_child_index(self, i):
        return 2 * i + 1

    def right_child_index(self, i):
        return 2 * i + 2

    def parent(self, i):
        return self.items[self.parent_index(i)]

    def left_child(self, i):
        return self.items[self.left_child_index(i)]

    def right_child(self, i):
        return self.items[self.right_child_index(i)]

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return self.size() <= 0

    def swim(self, i: int) -> None:
        while self.parent_index(i) >= 0 and self.parent(i)[1] > self.items[i][1]:
            self.items[self.parent_index(
                i)], self.items[i] = self.items[i], self.parent(i)
            i = self.parent_index(i)

    def sink(self, i: int) -> None:
        while self.left_child_index(i) < self.size():
            j = self.left_child_index(i)
            if j + 1 < self.size() and self.left_child(i)[1] > self.right_child(i)[1]:
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
    def __init__(self, s: int, adjList: Dict[int, List[List[int]]]) -> None:
        self.pq = MinHeap()
        self.dist = {}
        self.s = s
        self.adj_list = adjList

    def extract_min(self):
        return self.pq.del_min()

    def dijkstra(self, ) -> Dict[int, int]:
        for v in self.adj_list.keys():
            self.dist[v] = inf
            self.pq.insert((v, self.dist[v]))

        self.dist[self.s] = 0
        while not self.pq.is_empty():
            u, _ = self.pq.del_min()

            for v, w in self.adj_list[u]:
                alt = self.dist[u] + w
                if alt <= self.dist[v]:
                    self.dist[v] = alt
        return self.dist
