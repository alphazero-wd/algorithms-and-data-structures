from typing import List


class HeapSort:
    def __init__(self, nums: List[int]) -> None:
        self.nums = [None, *nums]

    def sink(self, i: int, n: int) -> None:
        while 2 * i < n:
            j = 2 * i
            if j + 1 < n and self.nums[j] < self.nums[j + 1]:
                j += 1
            if self.nums[i] >= self.nums[j]:
                break
            self.nums[j], self.nums[i] = self.nums[i], self.nums[j]
            i = j

    def heapsort(self):
        n = len(self.nums)
        for i in range(n // 2, 0, -1):
            self.sink(i, n)
        while n > 1:
            self.nums[1], self.nums[n - 1] = self.nums[n - 1], self.nums[1]
            n -= 1
            self.sink(1, n)

        return self.nums[1:]
