class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = defaultdict(int)

        for num in nums:
            occurrences[num] += 1

        sorted_occurrences = sorted(occurrences, key=lambda num: occurrences[num], reverse=True)

        top_elements = []

        for i in range(k):
            top_elements.append(sorted_occurrences[i])

        return top_elements