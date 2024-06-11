"""
Que: 
Relative Sort Array
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

link:https://leetcode.com/problems/relative-sort-array/description/

Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
"""

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # Create a dictionary to count the occurrences of each element in arr1
        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1
        
        # Append the elements in the order they appear in arr2
        result = []
        for num in arr2:
            result.extend([num] * count.pop(num))
        
        # Sort the remaining elements and append
        for num in sorted(count):
            result.extend([num] * count[num])
        
        return result
