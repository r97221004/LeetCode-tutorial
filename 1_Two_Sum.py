"""
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target. You may assume that each input would have exactly one 
solution, and you may not use the same element twice. You can return the answer in any order.
"""

# 方法一

"""
使用兩個 for 迴圈，參考範例一，當 i 等於2時， 看看剩下的有沒有等於 7。等 i 等於7時，看
看剩下的有沒有等於2，依此類推，找到就可回傳值。
"""

class Solution:
    def twoSum(self, nums, target):      
        for i in range(0, len(nums)) :
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

p = Solution()
print(p.twoSum([1, 2, 3, 4], 7))



# 方法二

"""
跟方法一的順序剛好顛倒。方法一是往後搜尋，這個方法是往前搜尋，比如第一個數是2，先
存在字典裡，再找第二個數是7，回頭看看字典裏面有沒有目標值減7的數，有就結束了。沒有
就再看第三個數是11， 回頭看看字典裏面有沒有目標值減11的數，只要有就找到答案，就可
回傳值了。這個方法的好處是只用到一個迴圈。
"""

# class Solution:
#     def twoSum(self, nums, target):
        
        
#         dict1 = {}
#         for i in range(len(nums)):
#             if target - nums[i] not in dict1:
#                 dict1[nums[i]] = i
#             else: 
#                 return [i, dict1[target - nums[i]]]

# p = Solution()
# print(p.twoSum([1, 2, 3, 4], 7))











