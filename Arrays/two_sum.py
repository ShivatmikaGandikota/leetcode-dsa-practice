# Problem: Two Sum
# https://leetcode.com/problems/two-sum/
# Use a HashMap to store visited numbers and check if target(current) number exists.
def twoSum(nums, target):
    hashmap = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in hashmap:
            return [hashmap[diff], i]

        hashmap[nums[i]] = i
