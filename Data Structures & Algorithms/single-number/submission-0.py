class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR properties:
        # 1. a ^ a = 0
        # 2. a ^ 0 = a
        # Because of this all the numbers that appears twice will cancel 
        # each other out, the number that appears once will remain

        # alg:
        # 1. initialize res = 0
        # 2. iterate each num
        # 3. update res = res ^ num
        # 4. after processing res will remain with the single numb

        res = 0
        for num in nums:
            res = res ^ num
        return res