import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the option is only from 0 to max(piles) for the speed
        left = 1
        right = max(piles)
        k = 0

        # calculate if using k speed, the time needed in hours
        # to finish is how much
        def calc(speed):
            sum = 0

            for p in piles:
                sum += math.ceil(p / speed)

            return sum

        while left <= right:
            mid = left + (right - left) // 2 # speed

            # hour needed to eat all the banana
            # with the speed of mid
            hour = calc(mid)

            # try lowering the speed because we want the
            # smallest k possible
            if hour <= h:
                right = mid - 1
                k = mid
            # if the current speed is too slow, we increase the speed
            elif hour > h:
                left = mid + 1

        return k