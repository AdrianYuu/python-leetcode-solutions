class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        # because by default it's a min heap
        # we use negation for each operation to make its a max heap
        heap = [-w for w in stones]

        heapq.heapify(heap)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, x - y)
        
        if len(heap) == 0:
            return 0
        
        return abs(heap[0])