# Input: prices = [7,1,5,3,6,4]
# Output: 5

# Input: prices = [7,6,4,3,1]
# Output: 0


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > lowest_price:
                max_profit = max(max_profit, prices[i] - lowest_price)
            elif prices[i] < lowest_price:
                lowest_price = prices[i]
        return max_profit


if __name__ == "__main__":
    prices = [7, 6, 4, 3, 1]
    s = Solution()
    ans = s.maxProfit(prices)
    print(ans)
