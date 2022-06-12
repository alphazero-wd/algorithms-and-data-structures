from Heap import Heap


class MinHeap(Heap):
    def __init__(self) -> None:
        super().__init__()

    def swim(self, i: int) -> None:
        while self.parent_index(i) > 0 and self.items[i // 2] > self.items[i]:
            self.items[i // 2], self.items[i] = self.items[i], self.parent(i)
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
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        min_item = self.items.pop()
        self.sink(1)
        return min_item
