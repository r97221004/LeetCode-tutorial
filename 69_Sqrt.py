"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only 
the integer part of the result is returned.
"""

# 方法一

"""
相當直接的想法，一個迴圈，只是時間相當浪費。
"""

# class Solution:
#     def mySqrt(self, x):
#         if not x:
#             return 0
#         for i in range(x+1):
#             if i*i == x:              
#                 return i
#             if i*i > x:
#                 return i-1

# p = Solution()
# x = 1
# print(p.mySqrt(x))  

# 方法二

"""
使用二分法 binary search，比上面的方法快很多， 但還是不理想，有更快的牛頓法可使用，
之後再來更新。
"""

class Solution:
    def mySqrt(self, x):
        left, right = 0, x/2 + 1
        while True:
            mid = int((left + right) / 2)  
            if mid**2 <= x and (mid+1)**2 > x:
                return mid
            elif (mid+1)**2 <= x:
                left = mid + 1
            else:
                right = mid
        
        
      

p = Solution()
x = 16
print(p.mySqrt(x)) 
  