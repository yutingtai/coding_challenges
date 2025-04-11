# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# Input: nums = [2,0,1]
# Output: [0,1,2]



from collections import defaultdict
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 1
        blue = 2
        count = defaultdict(int)
        for color in nums:
            count[color] += 1

        for i in range(len(nums)):
            if count[red] > 0:
                nums[i] = red
                count[red] -= 1
            elif count[white] > 0:
                nums[i] = white
                count[white] -= 1
            elif count[blue] > 0 :
                nums[i] = blue
                count[blue] -= 1
        

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    s = Solution()
    s.sortColors(nums)
    print(nums)


            
        