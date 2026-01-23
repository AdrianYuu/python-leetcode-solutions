class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        main = len(nums1)
        second = len(nums2)
        first = len(nums1) - second

        while (first > 0) and (second > 0):
            if nums1[first - 1] >= nums2[second - 1]:
                nums1[main - 1] = nums1[first - 1]
                first -= 1
            else:
                nums1[main - 1] = nums2[second - 1]
                second -= 1
            main -= 1

        while first > 0:
            nums1[main - 1] = nums1[first - 1]
            first -= 1
            main -= 1
        
        while second > 0:
            nums1[main - 1] = nums2[second - 1]
            main -= 1
            second -= 1