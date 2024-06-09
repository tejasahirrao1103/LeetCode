"""
Que:
974. Subarray Sums Divisible by K
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
A subarray is a contiguous part of an array.

link: 
https://leetcode.com/problems/subarray-sums-divisible-by-k/

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
"""
#solution

class Solution(object):
    def subarraysDivByK(self, nums, k):
        remainder_count = {0: 1}
        total = 0
        count = 0
        for num in nums:
            total += num
            remainder = total % k
            if remainder < 0:
                remainder += k
            if remainder in remainder_count:
                count += remainder_count[remainder]
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
    
        return count
