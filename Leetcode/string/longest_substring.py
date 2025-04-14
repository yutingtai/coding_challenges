# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.


# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.



import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_ch = set()
        length = float("-inf")
        left = 0
        for right in range(len(s)):
            while seen_ch and s[right] in seen_ch:
                seen_ch.remove(s[left])
                left += 1
            seen_ch.add(s[right])
            length = max(length, len(seen_ch))
        return int(length) if length != float("-inf") else 0
    
class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        s = "abcabcbb"
        ans = self.s.lengthOfLongestSubstring(s)
        self.assertEqual(3, ans)


    def test2(self):
        s = "bbbbb"
        ans = self.s.lengthOfLongestSubstring(s)
        self.assertEqual(1, ans)

    def test3(self):
        s = "pwwkew"
        ans = self.s.lengthOfLongestSubstring(s)
        self.assertEqual(3, ans)
    

if __name__ == "__main__":
    unittest.main()