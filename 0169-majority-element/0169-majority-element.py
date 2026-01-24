class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occ = {}
        length = len(nums)

        for n in nums:
            if n in occ:
                occ[n] += 1
            else:
                occ[n] = 1
            
            if occ[n] > length / 2:
                return n