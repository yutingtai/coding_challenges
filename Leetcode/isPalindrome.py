class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string_list = [ch for ch in str(x)]
        if len(string_list) == 1:
            return True
        else:
            for i in range(len(string_list) // 2):
                if string_list[i] != string_list[-1 - i]:
                    return False
            return True





def main():
    s = Solution()
    # print(s.isPalindrome(x=0))
    print(s.isPalindrome(x=1000021))


if __name__ == '__main__':
    main()
