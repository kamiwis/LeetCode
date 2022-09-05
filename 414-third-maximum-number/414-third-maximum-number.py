class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(list(set(nums))) < 3:
            return max(nums)
        for i in range(2):
            max_num = max(nums)
            while max_num in nums:
                nums.remove(max_num)
        return max(nums)
                
            
        