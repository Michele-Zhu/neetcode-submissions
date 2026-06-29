class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Slow and fast pointer solution
        # [1, 3, 4, 2, 2]
        # nums[0] points at idx 1 -> 3
        # nums[1] points at idx 3 -> 2
        # nums[2] points at idx 4 -> 2
        # nums[3] points at idx 2 -> 3
        # nums[4] points at idx 2 -> 3
        # we have multiple pointers at idx 2
        # we also guarantee that idx 0 is never poited

        # find cycle, i.e. intersection between fast & slow pointers
        slow, fast = 0, 0
        while True: # equivalent of do while cycle
            slow = nums[slow]
            fast = nums[nums[fast]] # double jump
            if slow == fast:
                break
        #print(slow, fast)
        # now we find the cycle starting point
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        #print(slow, slow2)
        return slow