class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyVal = prices[0]
        maxProfit = 0

        for i in prices:
            maxProfit = max(maxProfit, (i - buyVal))

            if i < buyVal:
                buyVal = i
        return maxProfit
