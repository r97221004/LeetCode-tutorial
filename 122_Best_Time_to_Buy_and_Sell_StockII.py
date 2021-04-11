"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy 
one and sell one share of the stock multiple times). Note: You may not engage in multiple transactions 
simultaneously (i.e., you must sell the stock before you buy again).
"""

# 方法一

"""
沒有想像中的難喔!只要把上升波段全都加起來而已。作法大家應該都大同小異。
"""

class Solution:
    def maxProfit(self, prices):
        profit  = 0
        for i in range(0,len(prices)-1):          
            if prices[i] < prices[i+1]:
                profit += (prices[i+1] - prices[i])
        
        return profit



p = Solution()
prices = [7,1,5,3,6,4]
print(p.maxProfit(prices))

