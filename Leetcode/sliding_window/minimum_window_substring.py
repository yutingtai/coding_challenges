# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_count = Counter(t)
        distinct_t_len = len(t_count)

        left = 0
        matched = 0
        window_count = Counter()
        ans =  float("inf"), 0 , 0

        for right in range(len(s)):
            window_count[s[right]] += 1

            if window_count[s[right]] == t_count[s[right]]:
                matched += 1
            
            while left <= right and matched == distinct_t_len:
                left_char = s[left]

                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                window_count[left_char] -= 1
                if window_count[left_char] < t_count[left_char]:
                    matched -=1

                left += 1


        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]



class Solu:
    def minWindow(self, s:str, t:str) -> str:
        if not s or not t:
            return ""
        
        t_count = Counter(t)
        distinct_t_len = len(t_count)
        left = 0
        matched = 0
        window_count = Counter()

        ans = float("inf"), 0 , 0 # min_length, left , right

        for right in range(len(s)):
            window_count[s[right]] += 1

            if window_count[s[right]] == t_count[s[right]]:
                matched += 1
            
            while left <= right and distinct_t_len == matched:
                if right - left + 1 < ans[0]:
                    ans = right - left + 1 , left , right
                
                left_ch = s[left]
                window_count[left_ch] -= 1
                if window_count[left_ch] < t_count[left_ch]:
                    matched -= 1
                left += 1
        return s[ans[1]:ans[2]+1] if ans[0] != float("inf") else ""

if __name__ == "__main__":
    s = Solution()
    ss = Solu()
    length = s.minWindow(s = "ADOBECODEBANC", t = "ABC")
    leng = ss.minWindow(s = "ADOBECODEBANC", t = "ABC")
    print(leng)

                

        
