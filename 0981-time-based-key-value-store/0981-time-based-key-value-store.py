class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        current = self.time_map[key]
        left = 0
        right = len(current) - 1
        result = ""

        while left <= right:
            mid = left + (right - left) // 2
            
            # current[mid][0] = timestamp
            # current[mid][1] = value
            if current[mid][0] <= timestamp:
                result = current[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)