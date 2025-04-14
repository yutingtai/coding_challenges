# Input: s = "A man, a plan, a canal: Panama"
# Output: true

# Input: s = "race a car"
# Output: false

# Input: s = " "
# Output: true


import re
import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        half_n = len(clean_s) // 2
        for i in range(half_n):
            if clean_s[i] != clean_s[len(clean_s) -1 -i]:
                return False
        return True
    

class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(self.s.isPalindrome(s))

    def test2(self):
        s = "race a car"
        self.assertFalse(self.s.isPalindrome(s))

    def test3(self):
        s = " "
        self.assertTrue(self.s.isPalindrome(s))


if __name__ == "__main__":
    unittest.main()