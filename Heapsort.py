from typing import List


class HeapSort:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums

    def sink(self, i: int, n: int) -> None:
        while 2 * i + 1 < n:
            j = 2 * i + 1
            if j + 1 < n and self.nums[j] < self.nums[j + 1]:
                j += 1
            if self.nums[i] >= self.nums[j]:
                break
            self.nums[j], self.nums[i] = self.nums[i], self.nums[j]
            i = j

    def heapsort(self):
        n = len(self.nums)
        for i in range((n - 1) // 2, -1, -1):
            self.sink(i, n)
        while n > 0:
            self.nums[0], self.nums[n - 1] = self.nums[n - 1], self.nums[0]
            n -= 1
            self.sink(0, n)

        return self.nums
