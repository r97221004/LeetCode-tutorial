"""
You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb
 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

# 方法一

"""
使用高中數學排列組合處理，速度勉強接受!
"""

# class Solution:
#     def climbStairs(self, n):
#         def fac(x):
#             if x == 0:
#                 return 1
#             val = 1
#             for i in range(2, x+1):
#                 val *= i
#             return val

#         gruopList = []
#         ans = 0
#         for i in range(n//2+1):
#             gruopList.append((n-2*i,i))
#         for i in gruopList:
#             ans += fac(i[0]+i[1])/(fac(i[0])*fac(i[1]))

#         return int(ans)

# p = Solution()
# n = 5
# print(p.climbStairs(n))  

# 方法二

"""
使用遞迴
"""

class Solution:
    def climbStairs(self, n):
        dp = [0] * (n+1)
        for i in range(n+1):         
            if i < 2: 
                dp[i] = 1
            else: 
                dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

p = Solution()
n = 5
print(p.climbStairs(n))  