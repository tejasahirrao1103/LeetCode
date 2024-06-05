"""
Que:
1002. Find Common Characters
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

link: https://leetcode.com/problems/find-common-characters/description/

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
"""
#solution
class Solution(object):
    def commonChars(self, words):
        char_count = {}

        for char in words[0]:
            char_count[char] = char_count.get(char, 0) + 1

        for word in words[1:]:
            temp_count = {}
            for char in word:
                temp_count[char] = temp_count.get(char, 0) + 1
            for char in char_count:
                char_count[char] = min(char_count[char], temp_count.get(char, 0))
        
        result = []
        for char, freq in char_count.items():
            result.extend([char] * freq)
        
        return result
