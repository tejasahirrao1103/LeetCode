"""
Que:
409. Longest Palindrome
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindromethat can be built with those letters. Letters are case sensitive, for example, "Aa" is not considered a palindrome.

link: https://leetcode.com/problems/longest-palindrome/description/

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
#Solution: 
class Solution(object):
    def longestPalindrome(self, s):
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        length = 0
        has_odd = False

        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                has_odd = True

        # Add an extra character in the middle if there's an odd count
        if has_odd:
            length += 1

        return length
