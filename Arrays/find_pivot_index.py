#https://leetcode.com/problems/find-pivot-index/
#724. Find Pivot Index

class Solution:
    def pivotIndex(self, nums):

        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])

            if left == right:
                return i

        return -1
