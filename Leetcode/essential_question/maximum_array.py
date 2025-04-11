# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


from typing import List
import unittest


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(current_sum, max_sum)

        return max_sum


class TestMaxSubArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.maxSubArray([1]), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.maxSubArray([5, 4, -1, 7, 8]), 23)

    def test_negative_numbers(self):
        self.assertEqual(self.solution.maxSubArray([-1, -2, -3, -4]), -1)

    def test_all_zeros(self):
        self.assertEqual(self.solution.maxSubArray([0, 0, 0, 0]), 0)

    def test_mixed(self):
        self.assertEqual(self.solution.maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3]), 7)


if __name__ == "__main__":
    unittest.main()
