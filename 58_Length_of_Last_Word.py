"""
Given a string s consists of some words separated by spaces, return the length of the 
last word in the string. If the last word does not exist, return 0.
A word is a maximal substring consisting of non-space characters only.
"""

# 方法一

"""
先將字串轉列表再reverse，用一次迴圈找第一個長度非0的數就是我們要的回傳值
"""

class Solution:
    def lengthOfLastWord(self, s):
        list1 = s.split(' ')
        list1.reverse()    
        for each in list1:
            if len(each) != 0:
                return len(each) 
        
        return 0
 

p = Solution()
s = "   ba " 
print(p.lengthOfLastWord(s))     


# 方法二

"""
注意! str.split() 預設用連續空格分割，與方法一比較一下。
"""

# class Solution:
#     def lengthOfLastWord(self, s):
#         s = s.split()
#         print(s)
#         if not s:
#             return 0
#         return len(s[-1])
     

# p = Solution()
# s = "   ba   aa     a" 
# print(p.lengthOfLastWord(s)) 