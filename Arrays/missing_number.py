#https://leetcode.com/problems/missing-number/
#268. Missing Number
#Approach: 
#1. Calculate sum of elements in the array.
#2. Calculate expected sum using formula n*(n+1)//2.
#3. Subtract array sum from expected sum.
#4. The result is the missing number.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        os=sum(nums)
        n=len(nums)
        ns=n*(n+1)//2
        return ns-os
        
