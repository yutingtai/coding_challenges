# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Input: target = 4, nums = [1,4,4]
# Output: 1

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


from typing import List


class Solution:
    def minSubArrayLen(self, target:int, nums: List[int]):
        left = 0
        current_sum = 0
        min_length = float("inf")
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float("inf") else 0
    
if __name__ == "__main__":
    s = Solution()
    length = s.minSubArrayLen(11, [1,1,1,1,1,1,1,1] )
    print(length)