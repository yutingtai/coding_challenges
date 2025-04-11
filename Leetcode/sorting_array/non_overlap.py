# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


from typing import List


def only_overlap(a: List[int], b: List[int]) -> bool:
    return a[1] == b[0]


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        overlap_range = [intervals[0]]
        count = 0

        for i in range(1, len(intervals)):
            if not only_overlap(overlap_range[-1], intervals[i]):
                count += 1
            overlap_range.append(intervals[i])

        return count


if __name__ == "__main__":
    intervals = [[1, 2], [2, 3]]
    s = Solution()
    ans = s.eraseOverlapIntervals(intervals)
    print(ans)
