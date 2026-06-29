class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use hashmap/array to store the numbers seen during traversal
        # the cost is O(n) in time and O(n) in space
        # 1. Traverse the array and use a boolean array to store the seen value
        # 2. True if seen, False if unseen
        # 3. If seen then return the value
        #
        # Can we do better than this solution?
        # -> no condition that numbers are ordered
        # -> Can we use the array itself to check conditions?
        # [1, 2, 3, 2, 2,], len(arr) = 5, n = 4, 1 <= arr[i] <= n
        # Properties of the array:
        # [1, n] range, the array contains n+1 integers, exactly one repeated integer in the array

        #  len(arr) = n + 1, 1<= arr[i] <= n, i in [0, n-1]
        # [0] -> mark the element encountered with it's index
        # [0, 1, 2,], now arr[3] = 2 check if arr[arr[3]] == arr[3]
        # and you should be golden
        # Why this solution should be valid? 
        # Example:
        # arr = [1, 2, 3, 3, 4], len(arr) = 5, n = 4
        # arr = [0, 1, 2, ], arr[3] == 3, arr[arr[3]] = 3 == arr[3] ?? yes

        # arr = [1, 2, 3, 4, 5, 2, 6], len(arr) = 7, n = 6
        # arr = [0, 1, 2, 3, 4, ],  arr[2] == arr[i] ?? yes

        # arr = [6, 3, 4, 5, 2, 1, 2]
        # arr = [0, 1, 2, 3, 4, 5, ], arr[2] == arr[i], 2 == 2 yes
        # i=0, arr[i] == arr[arr[i]]? No -> [0, ...]
        # i=1, arr[1] == arr[3]? 1 == 5? No -> [0, 1, ...]
        # i=2, arr[2] == arr[4], 4 == 2 ? No -> [0, 1, 2]
        # i=3, arr[3] == arr[5], 5 == 1 ? No -> [0, 1, 2, 3]
        # i=4, arr[4] == arr[2], 2 == 2? Yes -> Found 2
        seen = set()
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
            