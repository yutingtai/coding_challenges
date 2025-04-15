# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["tan", "nat"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]


from collections import Counter, defaultdict
from typing import List
import unittest


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_count = defaultdict(list)
        for _str in strs:
            _str_count = frozenset(Counter(_str))
            group_count[_str_count].append(_str)

        return list(group_count.values())
    


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        ans = self.s.groupAnagrams(strs)

        expected_groups = [["bat"],["tan","nat"],["eat","tea", "ate"]]
        
        for expected in expected_groups:
            self.assertIn(expected, ans)

        # Also make sure lengths match
        self.assertEqual(len(expected_groups), len(ans))
            
    def test2(self):
        strs = [""]
        self.assertEqual(self.s.groupAnagrams(strs), [[""]])

    def test3(self):
        strs = ["a"]
        self.assertEqual(self.s.groupAnagrams(strs), [["a"]])



if __name__ == "__main__":
    unittest.main()