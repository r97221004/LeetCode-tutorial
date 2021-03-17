"""
Implement strStr(). Return the index of the first occurrence of needle in haystack, or 
-1 if needle is not part of haystack.
"""

# 方法一

"""
python 的字串已經有內建的方法 index, 輕鬆解決。
"""

class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1

p =Solution()
haystack = "hello" ; needle = "ll"
print(p.strStr(haystack, needle))

# 方法二

"""
跟上面一樣的方法，只是換個方式寫，來個例外處理。
"""

# class Solution:
#     def strStr(self, haystack, needle):
#         if needle == "":
#            return 0
#         try:
#            return haystack.index(needle)
#         except ValueError:
#            return -1

# p =Solution()
# haystack = "hello" ; needle = "ll"
# print(p.strStr(haystack, needle))
