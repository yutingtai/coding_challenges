# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".


# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


from collections import Counter
from typing import List
import unittest


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target_index = []
        p_count = Counter(p)
        for i in range(len(s) - len(p) + 1):
            temp_count = Counter(s[i:i+len(p)])
            if temp_count == p_count:
                target_index.append(i)
        return target_index
    
    def OptimizedfindAnagrams(self, s: str, p: str) -> List[int]:
        target_index = []
        if len(s) < len(p):
            return target_index
        
        p_count = Counter(p)
        window_count = Counter(s[:len(p)])

        if window_count == p_count:
            target_index.append(0)


        for i in range(len(p), len(s)):
            left_ch = s[i - len(p)]
            window_count[left_ch] -= 1
            if window_count[left_ch] == 0:
                del window_count[left_ch]
            
            right_ch = s[i]
            window_count[right_ch] += 1
            if window_count == p_count:
                target_index.append(i - len(p) + 1)

        return target_index
    


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
    
    def test1(self):
        s = "cbaebabacd"
        p = "abc"
        ans = self.s.findAnagrams(s=s, p=p)
        self.assertEqual(ans, [0,6])

    def test2(self):
        s = "abab"
        p = "ab"
        ans = self.s.findAnagrams(s=s, p=p)
        self.assertEqual(ans, [0,1,2])


    def test1_optimized(self):
        s = "cbaebabacd"
        p = "abc"
        ans = self.s.OptimizedfindAnagrams(s=s, p=p)
        self.assertEqual(ans, [0,6])   

    def test2_optimized(self):
        s = "abab"
        p = "ab"
        ans = self.s.OptimizedfindAnagrams(s=s, p=p)
        self.assertEqual(ans, [0,1,2])

if __name__ == "__main__":
    unittest.main()
            
        