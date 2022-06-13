from typing import List, Optional


class Heap:
    def __init__(self) -> None:
        self.items: List[int] = []

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

    def peek(self) -> Optional[int]:
        if not self.is_empty():
            return self.items[0]
