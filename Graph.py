from typing import Dict, List

class Graph:
  def __init__(self) -> None:
    self.adj_list: Dict[int, List[List[int]]] = {}