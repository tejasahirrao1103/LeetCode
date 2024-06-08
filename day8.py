"""
Que:
523. Continuous Subarray Sum
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

link: https://leetcode.com/problems/continuous-subarray-sum/description/

A good subarray is a subarray where:
its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
  
Note that:
A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
"""
#solution: 
class Solution(object):
    def checkSubarraySum(self, nums, k):
        mod_dict = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            mod = total % k
        
            if mod in mod_dict:
                if i - mod_dict[mod] > 1:
                    return True
            else:
                mod_dict[mod] = i
    
        return False
        
