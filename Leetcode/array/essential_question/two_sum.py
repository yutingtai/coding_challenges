# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Input: nums = [3,3], target = 6
# Output: [0,1]


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in num_index:
                return [num_index[remain], i]

            else:
                num_index[num] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    ans = s.twoSum(nums=nums, target=target)
    print(ans)
