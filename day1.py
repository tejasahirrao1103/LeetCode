"""
que:
link: https://leetcode.com/problems/score-of-a-string/?envType=daily-question&envId=2024-06-01
3110. Score of a String

You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
Return the score of s.

Example 1:
Input: s = "hello"
Output: 13

Explanation:
The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.
"""

#solution

class Solution(object):
    def scoreOfString(self, s):
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i - 1]))
        return score
