from Graph import Graph

class UndirectedGraph(Graph):
  def __init__(self) -> None:
    super().__init__()

  def add_edge(self, u: int, v: int, w: int=0) -> None:
    if u not in self.adj_list: self.adj_list[u] = []
    if v not in self.adj_list: self.adj_list[v] = []
    self.adj_list[u].append([v, w])
    self.adj_list[v].append([u, w])