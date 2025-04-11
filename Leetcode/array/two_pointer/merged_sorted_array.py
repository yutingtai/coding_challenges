# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]


# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]


# Input: nums1 = [4, 5], m = 2, nums2 = [1, 2], n = 2
# Output: [1]

# [1, 2, 3]  [2, 3]





from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            elif nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1




if __name__ == "__main__":
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2, 5, 8]
    n = 3
    s.merge(nums1, m, nums2 ,n )
            
    print(nums1)
            