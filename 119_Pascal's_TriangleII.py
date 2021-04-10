"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

# 方法一

"""
跟118題幾乎完全一模一樣，兩個迴圈搞定。
"""

class Solution:
    def getRow(self, rowIndex):
        result = []
        for i in range(0, rowIndex+1):
            result.append([])
            for j in range(0, i+1):
                if j in [0, i]:
                    result[i].append(1)
                else:
                    result[i].append(result[i-1][j-1] + result[i-1][j])
        
        return result[-1]

p =Solution()        
rowIndex = 3
print(p.getRow(3))

# 方法二

"""
跟118幾乎一模一樣，可參考。
"""










