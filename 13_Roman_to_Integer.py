""" 
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

"""

# 方法一

""" 
只有 IV, IX, XL, XC, CD, CM 是特殊的值另外算， 算完把它替換成0，
其他就看它有幾個就乘幾個它的值。注意我們符號與對應的值用字典來儲存。
很難推廣
"""


class Solution:
    def romanToInt(self, s):
        Output = 0
        Special = dict(IV=4, IX=9, XL=40, XC=90, CD=400, CM=900)
        Origin = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

        for each in Special:
            Output += s.count(each)*Special[each]
            s = s.replace(each, '0')

        for each in Origin:
            Output += s.count(each)*Origin[each]
            
        return Output

p = Solution()
print(p.romanToInt('MCMXLIII'))

# 方法二

""" 
用掃描的方式，兩個兩個看。如果左邊比右邊大，就用加的。如果左邊比右邊小，就用減的。
容易推廣
"""

# class Solution:
#     def romanToInt(self, s):
#         values = {"I": 1,
#                   "V": 5,
#                   "X": 10,
#                   "L": 50,
#                   "C": 100,
#                   "D": 500,
#                   "M": 1000,}
#         num = 0
 
#         for i in range(len(s)-1):
#             if values[s[i]] >= values[s[i+1]]:
#                 num += values[s[i]]
#             if values[s[i]] < values[s[i+1]]:
#                 num -= values[s[i]]
#         num += values[s[-1]]

#         return num
# p = Solution()
# print(p.romanToInt('MCMXLIII'))
