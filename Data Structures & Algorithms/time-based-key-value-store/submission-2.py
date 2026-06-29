class TimeMap:

    def __init__(self):
        self.time = []
        self.dictionary = []


    def set(self, key: str, value: str, timestamp: int) -> None:
        # each call of timestamp has strictly increasing 
        # time
        self.time.append(timestamp)
        self.dictionary.append({})
        self.dictionary[-1][key] = value
        print(f"setting {key, self.dictionary[-1][key]}")
        

    def get(self, key: str, timestamp: int) -> str:
        def binary_search(low, high, target):
            if low > high:
                return low
            mid = low + (high - low) // 2

            if self.time[mid] <= target and self.time[mid+1] > target:
                return mid
            elif self.time[mid] > target: # search left
                return binary_search(low, mid-1, target)
            else:
                return binary_search(mid+1, high, target)
        for t in self.time:
            print(f"calling get at time {t} and key {key}")
        idx = binary_search(0, len(self.time)-2, timestamp)
        print(idx)

        while idx >= 0:
            if idx == 0 and timestamp < self.time[0]:
                return ""
            result = self.dictionary[idx].get(key)
            print(f"result {result} at timestamp: {timestamp}, idx: {idx}")
            if result: 
                return result
            
            idx -= 1

        return ""