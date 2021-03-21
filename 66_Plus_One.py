"""
Given a non-empty array of decimal digits representing a non-negative integer, increment 
one to the integer. The digits are stored such that the most significant digit is at the 
head of the list, and each element in the array contains a single digit. You may assume 
the integer does not contain any leading zero, except the number 0 itself.
"""

# 方法一

"""
先把列表專成真正的一個整數後，加1，之後再轉回列表。
"""
class Solution:
    def plusOne(self, digits):
        value = 0
        digits.reverse()
        for i in range(len(digits)):
            value += digits[i]*10**(i)
        value += 1
        return [ int(i) for i in list(str(value))]


p = Solution()
digits = [1,2,9,9,9]
print(p.plusOne(digits))

# 方法二

"""
直接從列表改，重點是要注意進位的問題，跟列表要從尾巴讀回來。
"""

# class Solution:
#     def plusOne(self, digits):
#         for i in reversed(range(len(digits))):
#             if digits[i] == 9:
#                 digits[i] = 0
#             else:
#                 digits[i] += 1
#                 return digits
#         digits[0] =1
#         digits.append(0)
#         return digits

        
# p = Solution()
# digits = [1,2,9,9,9]
# print(p.plusOne(digits))