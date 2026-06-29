class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
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

        """
        for i, num in enumerate(nums):
            if nums[i] == nums[num]:
                print(f"return at index {i}, num {num}")
                return num
            else:
                nums[i] = i
        """

        # arr = [3, 1, 3, 4, 2]
        # i=0, arr[0] == arr[3], 3 == 4? No -> [0,]
        # i=1, arr[1] == arr[1], -> yes -> Found 1
        # Problem! The algorithm doesn't work
        # Idea: Set index arr[arr[i]] as the value seen
        # You will later see: [1, 2, 3, 4, 5] type of array
        # But what's the condition under which the value is already seen?
        # [3, 1, 3, 4, 2]
        # i = 0, [3, 1, 3, 3, 2] # You lost the val 4
        # i = 1, [3, 1, 3, 3, 2]
        # i = 2, is arr[arr[i]] == arr[i] before setting it? if yes return that value?
        # -> at idx 2 we return 3 since the has been set
        """
        for i, num in enumerate(nums):
            if nums[num] == nums[i]:
                return num
            else:
                nums[num] = num
        failing badly:
        [1, 2, 3, 2, 2]
        i=0, arr[arr[0]] == arr[0], 2 == 1 ? No -> [1, 1, 3, 2, 2]
        i=1, arr[arr[1]] == arr[1], arr[1] == arr[1] -> yes
        """
        # Use negative marking
        # num between [1, n], each number corresponds to an idx in the array num-1
        # [1, 2, 3, 2, 2] -> positions (0, 1, 2, 3, 4)
        # When we see a number we go to corresponding position and flip the sign
        # if we visit a idx where the value is negative means we visited that number
        # idx = abs(num) - 1
        # nums[idx] < 0 -> return abs(num)
        # else nums[idx] *= -1

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            else:
                nums[idx] *= -1
