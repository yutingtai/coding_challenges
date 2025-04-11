# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Input: temperatures = [30,60,90]
# Output: [1,1,0]



from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_index = []
        ans = [0 for _ in range(len(temperatures))]

        for i, t in enumerate(temperatures):
            while stack_index and temperatures[stack_index[-1]] < t:
                prev_index = stack_index.pop()
                ans[prev_index] = i - prev_index
            stack_index.append(i)
        return ans
    

class Solu:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        temp_i_stack = []
        
        for i,temp in enumerate(temperatures):
            while temp_i_stack and temp > temperatures[temp_i_stack[-1]]:
                prev_i = temp_i_stack.pop()
                ans[prev_i] = i - prev_i
            temp_i_stack.append(i)

        return ans
    


if __name__ == "__main__":
    temperatures =  [30,40,50,60]
    s = Solution()
    ss = Solu()
    ans = s.dailyTemperatures(temperatures)
    _ans = ss.dailyTemperatures(temperatures)
    print(ans)
    print(_ans)