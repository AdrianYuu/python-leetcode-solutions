class Solution:
    def totalMoney(self, n: int) -> int:
        week = 0
        day = 1
        total = 0

        for i in range(n):
            total += week + day
            day += 1

            if day == 8:
                day = 1
                week += 1

        return total