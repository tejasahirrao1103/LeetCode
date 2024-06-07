"""
Que:
846. Hand of Straights
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

link: https://leetcode.com/problems/hand-of-straights/description/?envType=daily-question&envId=2024-06-06

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
"""
#solution
from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        
        card_count = Counter(hand)
        start_cards = sorted(card_count)
        
        for card in start_cards:
            if card_count[card] > 0:
                count = card_count[card]
                # Try to create 'count' number of sequences starting with 'card'
                for i in range(count):
                    for j in range(card, card + groupSize):
                        if card_count[j] > 0:
                            card_count[j] -= 1
                        else:
                            return False
        return True
