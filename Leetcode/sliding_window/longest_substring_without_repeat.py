# Given a string s, find the length of the longest substring without duplicate characters.
#
# s = "abcabcbb"
# outpu: 3
# a: abc
#
# s = "pwwkew"
# output : 3
# a: wke



def find_sentence_indices(paragraph: str, sentence: str):
    start_index = paragraph.find(sentence)
    if start_index == -1:
        return -1, -1  # Sentence not found

    end_index = start_index + len(sentence) - 1
    return start_index, end_index


paragraph = ""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_pointer, end_pointer = 0, 0
        max_len = 0
        seen_ch = set()
        for end_pointer in range(len(s)):
            while s[end_pointer] in seen_ch:
                seen_ch.remove(s[start_pointer])
                start_pointer += 1
            seen_ch.add(s[end_pointer])
            max_len = max(max_len, end_pointer-start_pointer+1)

        return max_len
            










class S:
    def ans(self, s):
        left = 0
        max_length = 0
        seen_ch = set()
        for right in range(len(s)):
            while s[right] in seen_ch:
                seen_ch.remove(s[left])
                left += 1
            seen_ch.add(s[right])
            max_length = max(max_length, right- left + 1)
        return max_length











class Solu:
    def ans(self, s):
        left = 0
        seen_ch = set()
        max_length = 0
        for right in range(len(s)):
            while s[right] in seen_ch:
                seen_ch.remove(s[left])
                left += 1
            seen_ch.add(s[right])
            max_length = max(max_length, right-left +1)
        return max_length

















if __name__ == "__main__":
    solution = Solution()
    ss = S()
    sss = Solu()
    strings = ["abcabcbb", "pwwkew", ""]

    for s in strings:
        length = solution.lengthOfLongestSubstring(s)
        _length = ss.ans(s)
        __length = sss.ans(s)
        print(length)
        print(_length)
        print(__length)

    
    
    