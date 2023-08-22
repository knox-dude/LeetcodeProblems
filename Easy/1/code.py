class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = dict()
        for idx, val in enumerate(nums):
            if val in needed:
                return needed[val], idx
            needed[target-val] = idx
