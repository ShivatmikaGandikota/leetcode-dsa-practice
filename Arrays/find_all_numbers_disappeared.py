#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
#448. Find All Numbers Disappeared in an Array
# Approach:
# Convert array to set and check numbers from 1 to n.
# If a number is not in the set, add it to the result list.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        s=set(nums)
        for i in range(1,n+1):
            if i not in s:
                ans.append(i)
        return ans
