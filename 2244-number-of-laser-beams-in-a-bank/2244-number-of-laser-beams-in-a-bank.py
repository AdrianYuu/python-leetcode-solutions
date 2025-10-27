class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        prev = None

        for i in range(len(bank)):
            if not "1" in bank[i]:
                continue

            if prev is not None:
                total += bank[i].count("1") * bank[prev].count("1")

            prev = i

        return total