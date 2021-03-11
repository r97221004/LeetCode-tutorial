""" 
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

# 方法一

""" 
先用字串的sort屬性把字串長度最小的拉到第一個位子。兩個for迴圈就可以解決。第一個迴圈
是對第一個字串的每個字元，第二個迴圈是跑每個字串看看有沒有跟第一個字串的字元一樣。小心 runtime error。
"""


class Solution:
    def longestCommonPrefix(self, strs):
        Output = ''
        if not len(strs):
            return Output
        
        
        strs.sort(key=len)
       
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return Output
            else:
                Output += strs[0][i]   

        return Output


p = Solution()
strs = ['flac', 'flaee', 'flacce']
print(p.longestCommonPrefix(strs))

# 方法二

""" 
類似的作法，先用字串的sort屬性把字串長度最小的拉到第一個位子。兩個for迴圈就可以解決。
這個方法的第一個迴圈是讓字元從第一個字串的第一個字元跑到最後一個字元，第二個迴圈是看兩兩字元有沒有一樣。
"""
# class Solution:
#     def longestCommonPrefix(self, strs):
#             prefix = []
#             strs.sort(key=len)
#             if not strs: return ''
#             else:
#                 for i in range(len(strs[0])):
#                     if all(strs[c][i]==strs[c+1][i] for c in range(len(strs)-1)):
#                         prefix.append((strs[0][i]))
#                     else:
#                         break
#                 return ''.join(prefix)

# p = Solution()
# strs = ['flac', 'flaee', 'flacce']
# print(p.longestCommonPrefix(strs))


"""
all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
"""

"""
join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。語法: str.join(sequence)
"""


