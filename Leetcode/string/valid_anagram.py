# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false

# anagram: same freqency for the same letter


import unittest
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)
        for ch, number in s_count.items():
            if ch not in t_count or t_count[ch] != number:
                return False
        return True
        




class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(self.s.isAnagram(s=s, t=t))

    def test2(self):
        s = "rat"
        t = "cat"
        self.assertFalse(self.s.isAnagram(s=s, t=t))
        

if __name__ == "__main__":
    unittest.main()