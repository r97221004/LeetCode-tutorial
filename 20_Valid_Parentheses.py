"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine 
if the input string is valid. An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
"""

# 方法一

"""
先定義什麼是合法的形式，然後再用遞迴的方式把原先的表達式簡化。兩兩字元掃，由左自右，把 (), {},[]
都消滅成""， 一直重複同樣的事，等到刪到不能再刪， 長度固定了，裡面還不是Valid_forms，就是錯的了。
"""

class Solution:
    def isValid(self, s):
        valid_forms = ['()', '[]', '{}', '']

        if s in valid_forms:
            return True
        leng = len(s)
        s = s.replace('()','')
        s = s.replace('[]','')
        s = s.replace('{}','')
        if len(s) == leng:
            return False
        else:
            return self.isValid(s)

p = Solution()
s = '{{}[][[[]]]}'
print(p.isValid(s))

# 方法二

"""
跟上面的方法有點類似，只是這個方法是由左自右掃，蒐集開口向右的括弧，一配到對就消滅掉，一配到對就消滅掉，等到刪到不能再刪，
裡面還有東西在就是錯的了。
"""

# class Solution:
#     def isValid(self, s):
#             a=[]
#             d={ ')':'(' , ']':'[' , '}':'{' }
#             b='([{'
#             for i in s:
#                 if i in b:
#                     a.append(i)
#                 else:
#                     if a and a[-1]==d[i]:
#                         a.pop()
#                     else:
#                         return False
#             if a:
#                 return False
#             return True

# p = Solution()
# s = '{{}[][[[]]]}'
# print(p.isValid(s))










