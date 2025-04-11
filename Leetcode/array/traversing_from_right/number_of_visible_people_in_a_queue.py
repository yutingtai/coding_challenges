# Input: heights = [10,6,8,5,11,9]
# Output: [3,1,2,1,1,0]


# Input: heights = [5,1,2,3,10]
# Output: [4,1,1,1,0]

from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)
        n = len(heights) - 1 

        stack = []

        for i in range(n, -1, -1):
            count = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1
            if stack:
                count += 1
            
            ans[i] = count
            stack.append(heights[i])
            
        return ans
    

if __name__ == "__main__":
    s = Solution()
    ans = s.canSeePersonsCount([10,6,8,5,11,9])
    print(ans)