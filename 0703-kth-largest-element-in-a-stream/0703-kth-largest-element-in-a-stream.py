class KthLargest:
    # use min heap with K largest number
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

        # heapify the list
        heapq.heapify(self.heap)

        # only take K largest number
        # so we pop untill the size is only K
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)