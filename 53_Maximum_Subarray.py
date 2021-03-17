"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
"""

# 方法一

"""
使用暴力法，雖然邏輯沒錯，但會 Time Limit Exceeded，需要進一步優化。
"""

# class Solution:
#     def maxSubArray(self, nums):
#         cumsums = []       
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 cumsums += [sum(nums[i:j+1])]
        
#         return max(cumsums)

        
# p = Solution()
# nums = [-2,1,-3, 2, 10 ]
# print(p.maxSubArray(nums))

# 方法二

"""
考慮 nums_update 的列表，第i項要看他的第i-1項，如果第i-1項是負的，就寧願選 nums[i] 從新開始。
如果第i-1項是正的，第i項就是第i-1項再加上nums[i]。最後取最大的值就是答案。
nums_update = [-2, 1, -2, 4, 3, 5, 6, 1, 5]
"""

# class Solution:
#     def maxSubArray(self, nums):
#         nums_update = [None]*len(nums)
#         nums_update[0] = nums[0]
#         for i in range(1, len(nums)):
#             nums_update[i] = max(nums_update[i-1] + nums[i], nums[i])
#         return max(nums_update)
# p = Solution()
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(p.maxSubArray(nums))

# 方法三

"""
改寫上面的方法，再優化。
"""

class Solution:
    def maxSubArray(self, nums):
        answer = nums[0]
        temp = nums[0]
        for i in range(1, len(nums)):
            temp = max(temp + nums[i], nums[i])
            answer = max(answer, temp)
        return answer
         
        
p = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(p.maxSubArray(nums))