class TimeMap:

    def __init__(self):
        self.keyStore = defaultdict(list)  # key: list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result, values = "", self.keyStore.get(key)
        if values is None:
            return result
        left, right = 0, len(values) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][1] <= timestamp: # search right, timestamp > search_val
                result = values[mid][0]
                left = mid + 1
            else: # search left
                right = mid - 1
        return result
