class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for n in list(set(nums)):
            if nums.count(n) > len(nums) // 2:
                return n
        