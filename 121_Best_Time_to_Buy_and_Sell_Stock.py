"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different 
day in the future to sell that stock. Return the maximum profit you can achieve from this 
transaction. If you cannot achieve any profit, return 0.
"""

# 方法一

"""
由左刷到右，遇到跌的更新fix，遇到漲的且漲得更多，更新返回值。
"""

# class Solution:
#     def maxProfit(self, prices):
#         fix = prices[0]
#         res = 0
#         for i  in range(1, len(prices)):
#             if prices[i] <= fix:
#                 fix = prices[i]
#             elif prices[i] - fix > res:
#                 res = prices[i] - fix

#         return res

# p = Solution()
# prices = [7,1,5,3,6,4]
# print(p.maxProfit(prices))


# 方法二

"""
由左刷到右，每次都及時更新 min_price 和 max_profit

"""

class Solution:
    def maxProfit(self, prices):
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min( min_price, price)
            max_profit = max(max_profit, price - min_price)
    
        return max_profit

p = Solution()
prices = [7,1,5,3,6,4]
print(p.maxProfit(prices))