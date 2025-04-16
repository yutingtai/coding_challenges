# Input: ransomNote = "a", magazine = "b"
# Output: false

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Input: ransomNote = "aa", magazine = "aab"
# Output: true


from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)

        for ch, number in r_count.items():
            if m_count[ch] < number:
                return False
        return True