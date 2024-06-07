"""
Que:
648. Replace Words
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative.
For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".Given a dictionary consisting of many roots and a sentence consisting of words 
separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root 
that has the shortest length.Return the sentence after the replacement.

link: https://leetcode.com/problems/replace-words/

Example 1:
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

"""

#solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        def insert(root, word):
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True
        
        def find_root(root, word):
            node = root
            root_form = ""
            for char in word:
                if char not in node.children or node.is_end_of_word:
                    break
                node = node.children[char]
                root_form += char
            return root_form if node.is_end_of_word else word
        
        root = TrieNode()
        for word in dictionary:
            insert(root, word)

        words = sentence.split()
        for i in range(len(words)):
            words[i] = find_root(root, words[i])
    
        return ' '.join(words)
