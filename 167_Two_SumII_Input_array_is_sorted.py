"""
Given an array of integers numbers that is already sorted in ascending order, find two numbers such 
that they add up to a specific target number. Return the indices of the two numbers (1-indexed) as an 
integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length. You may assume that each 
input would have exactly one solution and you may not use the same element twice.
"""

# 方法一

"""
跟第一題幾乎完全一模一樣阿。
"""

# 方法一

class Solution:
    def twoSum(self, numbers, target):
        dict1 = {}
        for i in range(len(numbers)):
            if target - numbers[i] not in dict1:
                dict1[numbers[i]] = i
            else:
                return [ dict1[target-numbers[i]]+1, i+1 ]

          

p = Solution()
numbers = [2,7,11,15] ; target = 9
print(p.twoSum(numbers, target))        