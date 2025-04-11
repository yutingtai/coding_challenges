# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]

#        *
#  a     |-------|
#  b           |----|

#   |----|
#        |---|
#
#        


from typing import List


def overlap(a: List[int], b:List[int]) -> bool:
    return a[1] >= b[0] and b[1] > a[0]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        checked = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if overlap(checked[-1], intervals[i]):
                new_interval = [min(checked[-1][0],intervals[i][0]), max(checked[-1][1],intervals[i][1])]
                checked[-1] = new_interval
            else:
                checked.append(intervals[i])
        
        return checked



if __name__ == "__main__":
    intervals = [[1,4],[4,5]]
    s = Solution()
    ans = s.merge(intervals)
    print(ans)