"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], 
then return 0. Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

# 方法一

"""
先分成大於等於0跟小於0來操作, 轉成字串再轉成列表用列表屬性來達成目標, 再把他轉回整數, 最後
要檢查有沒有超出範圍
"""

# class Solution:
#     def reverse(self, x):      
#         if x >= 0: 
#             New_Str = ''
#             list1 = list(str(x))
#             list1.reverse()
#             for each in list1:
#                 New_Str += each
#             x_reverse = int(New_Str)

#         else:
#             New_Str = '-'
#             list1 = list(str(x))
#             list1.pop(0)
#             list1.reverse()
#             for each in list1:
#                 New_Str += each
#             x_reverse = int(New_Str)

#         if -2**31 <= x_reverse <= 2**31 -1:
#             return x_reverse
#         else:
#             return 0

# p = Solution()
# print(p.reverse(-123000))

# 方法二

"""
直接轉換到字串再轉回整數, 精簡多了!!
"""

class Solution:
    def reverse(self, x):
        # convert to string, reverse, convert to int?
        x = str(x)
        x = x[::-1]
        if '-' in x:
            x = x.strip('-')
            x = -1*int(x)
        else:
            x = int(x)
        if x >= (-2)**31 and x <= (2**31) - 1:
            return x
        else:
            return 0

p = Solution()
print(p.reverse(-123000))

