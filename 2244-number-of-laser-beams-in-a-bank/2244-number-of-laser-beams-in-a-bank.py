class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0

        def calc_laser(s):
            laser = 0
            for c in s:
                if c == '1':
                    laser += 1
            return laser

        prev = None

        for i in range(len(bank)):
            if not "1" in bank[i]:
                continue

            if prev is not None:
                total += calc_laser(bank[i]) * calc_laser(bank[prev])

            prev = i

        return total