"""
Given an integer x, return true if x is palindrome integer. An integer is 
a palindrome when it reads the same backward as forward. For example, 121 is 
palindrome while 123 is not.
"""

# 方法一

"""
把整數轉成字串, 再用字串的index來處理即可
"""

# class Solution:
#     def isPalindrome(self, x):
#         x = str(x)
#         x_reverse = x[::-1]
#         if x == x_reverse and -2**31 <= int(x_reverse)  and int(x_reverse) <= 2**31 -1:
#             return True
#         else:
#             return False

# p = Solution()
# print(p.isPalindrome(123321))

# 方法二

"""
一模一樣的想法, 只是寫得更簡潔
"""

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

p = Solution()
print(p.isPalindrome(123321))