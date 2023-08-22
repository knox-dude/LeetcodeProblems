class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lowest, mid = 2**31, 2**31
        highest = -1
        for num in nums:
            if num > lowest and num > mid:
                return True
            if num > lowest and num < mid:
                mid = num
            if num < lowest:
                lowest = num
        return False
        
