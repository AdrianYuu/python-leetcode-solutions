class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        result = [0] * length
        stack = []

        #75, 71, 76

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                i, t = stack.pop()
                result[i] = index - i

            stack.append((index, temperature))

        return result 