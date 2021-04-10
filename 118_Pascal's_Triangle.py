"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

# 方法一

"""
用兩個迴圈解決，第一個迴圈決定列表數，第二個迴圈決定列表的內容
"""
class Solution:
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            result.append([])
            for j in range(0,i+1):
                if j in (0, i):
                    result[i].append(1)
                else:
                    result[i].append(result[i-1][j-1] + result[i-1][j])
        
        return result

p = Solution()
numRows = 5
print(p.generate(5))

# 方法二

"""
同樣的道理只是寫法稍微不同
"""

# class Solution:
#     def generate(self, numRows):
#         res = [[1]]
#         if numRows == 1:
#             return res
#         else:
#             for r in range(1, numRows):
#                 cur_row = [1]
#                 prev_row = res[-1]
#                 for i in range(1, r):
#                     cur_row.append(prev_row[i - 1] + prev_row[i])
#                 cur_row.append(1)
#                 res.append(cur_row)
#         return res
          

# p = Solution()
# numRows = 5
# print(p.generate(5))