# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


from collections import defaultdict
import unittest


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ch_count = defaultdict(int)
        max_length = 0
        max_count = 0

        for right in range(len(s)):
            ch_count[s[right]] += 1
            max_count = max(max_count, ch_count[s[right]])

            if (right - left + 1) - max_count > k:
                ch_count[s[left]] -= 1
                left += 1
            
            max_length = max(right - left + 1, max_length)
        return max_length


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        s = "ABAB"
        k = 2
        self.assertEqual(self.s.characterReplacement(s=s, k=k), 4)

    def test2(self):
        s = "AABABBA"
        k = 1 
        self.assertEqual(self.s.characterReplacement(s=s, k=k), 4)


if __name__ == "__main__":
    unittest.main()
            
            