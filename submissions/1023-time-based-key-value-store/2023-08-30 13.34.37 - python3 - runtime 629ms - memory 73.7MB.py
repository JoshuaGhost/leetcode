class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        p = bisect.bisect_right(self.cache[key], timestamp, key = lambda x: x[1]) - 1
        if len(self.cache[key]) == 0 or self.cache[key][p][1] > timestamp:
            return ''
        return self.cache[key][p][0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)