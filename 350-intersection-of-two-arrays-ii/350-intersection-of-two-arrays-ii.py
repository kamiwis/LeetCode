class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        shorter_array = []
        longer_array = []
        result = []
        if len(nums1) <= len(nums2):
            shorter_array = nums1
            longer_array = nums2
        if len(nums1) > len(nums2):
            shorter_array = nums2
            longer_array = nums1
        for n in set(shorter_array):
            if n in longer_array:
                intersection_num = min(nums1.count(n), nums2.count(n))
                for i in range(intersection_num):
                    result.append(n)
        return result
                    
            