#https://leetcode.com/problems/intersection-of-two-arrays/
# Problem: Intersection of Two Arrays
#Converting nums1 to a set and check each element of nums2.
# If element exists in nums1 set, add it to result set.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        s=set()
        for i in nums2:
            if i in set1:
                s.add(i)
        return list(s)
