"""
Given two binary strings a and b, return their sum as a binary string.
"""

# 方法一

"""
先把二進位轉成十進位，加完之後再轉回二進位。 小心一下兩個函數的參數跟返回值是字串還是整數。
"""
class Solution:
    def addBinary(self, a, b):       
        def ToDecimal(x):
            Total = 0
            toList = list(str(x))
            toList.reverse()
            toList = [int(each) for each in toList]
            for i in range(len(toList)):
                Total += toList[i]*2**(i)
            return Total
        
        def ToBinary(x):
            if x//2 ==0:
                return str(x%2)
            else:
                return ToBinary(x//2) + str(x%2)
             

        return ToBinary(ToDecimal(a) + ToDecimal(b))

p =Solution()
a = "1010" ; b = "1011"
print(p.addBinary(a,b))

# 方法二

"""
跟我們在算十進位相加一樣，記得carry位，也就是要不要進位。
carry  10100   
    a   1010
    b   1011
"""
# class Solution:
#     def addBinary(self, a, b):
#         result, carry, val = '', 0, 0
#         for i in range(max(len(a), len(b))):
#             if i < len(a):
#                 val += int(a[-i-1])
#             if i < len(b):
#                 val += int(b[-i-1])
#             val += carry 
#             result = str(val%2) + result
#             carry, val = val//2, 0

#         if carry:
#             result = '1' + result
#         return result



# p =Solution()
# a = "1010" ; b = "1011"
# print(p.addBinary(a,b))