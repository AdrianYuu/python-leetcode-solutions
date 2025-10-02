class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = defaultdict(int)
        length = len(nums) + 1

        for num in nums:
            occurrences[num] += 1

        frequencies = [[] for _ in range(length)]

        for num, occur in occurrences.items():
            frequencies[occur].append(num)

        top_elements = []

        for i in range(length):
            nums = frequencies[length - i - 1]
            
            for num in nums:
                top_elements.append(num)

                if len(top_elements) == k:
                    return top_elements