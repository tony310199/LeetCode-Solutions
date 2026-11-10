class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minimum = prices [0] 
        for i in range(1,len(prices)):
            if prices[i] < minimum:
                minimum =  prices[i]
            if prices[i] - minimum > profit:
                profit = prices[i] - minimum

        return profit