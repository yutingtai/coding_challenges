# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.__count_palindrome(s, i ,i)
            count += self.__count_palindrome(s, i, i+1) 
        return count

    def __count_palindrome(self, s:str, l:int, r:int) -> int:
        count = 0 
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
    

if __name__ == "__main__" :
    string = "aaa"
    s = Solution()
    c = s.countSubstrings(string)
    print(c)