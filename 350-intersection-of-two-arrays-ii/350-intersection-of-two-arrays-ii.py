class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = list(set(nums1).intersection(nums2))
        result = []

        for n in intersection:
            intersection_num = min(nums1.count(n), nums2.count(n))
            for i in range(intersection_num):
                result.append(n)
        return result
                    
            