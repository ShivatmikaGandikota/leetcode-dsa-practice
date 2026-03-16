#https://leetcode.com/problems/find-pivot-index/
#724. Find Pivot Index
#using Prefix Sum

class Solution:
    def pivotIndex(self, nums):
        prefix = [0]*len(nums)

        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]

        total = prefix[-1]

        for i in range(len(nums)):
            left = prefix[i-1] if i > 0 else 0
            right = total - prefix[i]

            if left == right:
                return i

        return -1
