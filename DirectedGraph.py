from typing import Dict, List
from Graph import Graph


class DirectedGraph(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.rev_adj_list: Dict[int, List[List[int]]] = {}

    def add_edge(self, u: int, v: int, w: int = 0):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append([v, w])

    def transpose(self):
        for u in self.adj_list.keys():
            self.rev_adj_list[u] = []

        for u in self.adj_list.keys():
            for v, w in self.adj_list[u]:
                self.rev_adj_list[v].append([u, w])
