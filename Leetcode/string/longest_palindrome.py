# Input: s = "babad"
# Output: "bab"


# Input: s = "cbbd"
# Output: "bb"
import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        longest = 0
        for i in range(len(s)):
            odd = self.__longest_palindrom(s, i, i)
            even = self.__longest_palindrom(s, i, i + 1)
            if len(odd) > len(even) and longest < len(odd):
                ans = odd
                longest = len(odd)
            elif len(odd) < len(even) and longest < len(even):
                ans = even
                longest = len(even)
        return ans
    
    def __longest_palindrom(self, s: str, l: int, r: int) -> str:
        ans = ""
        longest = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            length = r - l + 1
            if length > longest:
                ans = s[l:r+1]
            l -= 1
            r += 1
        return ans
    

class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def testcase_1(self):
        s = "babad"
        ans = self.s.longestPalindrome(s)
        self.assertEqual(ans, "bab")

    def testcase_2(self):
        s = "cbbd"
        ans = self.s.longestPalindrome(s)
        self.assertEqual(ans, "bb")



if __name__ == "__main__":
    unittest.main()
        