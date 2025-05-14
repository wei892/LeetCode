class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxP = 0

        while right < len(prices)-1:
            print(left, right)
            if prices[right] < prices[left]:
                left = right
                right += 1
            profit = prices[right] - prices[left]
            maxP = max(maxP, profit)
            right += 1
        
        return maxP