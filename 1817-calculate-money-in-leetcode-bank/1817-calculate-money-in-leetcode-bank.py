class Solution:
    def totalMoney(self, n: int) -> int:
        week = n // 7
        remainder = n % 7

        total = 0
        curr = 0

        for i in range(week):
            total += 28 + 7 * curr
            curr += 1

        for i in range(remainder):
            total += (i + 1) + curr

        return total