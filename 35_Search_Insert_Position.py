"""
Given a sorted array of distinct integers and a target value, return the index 
if the target is found. If not, return the index where it would be if it were inserted in order.
"""

# 方法一

"""
如果 target 有在有序列表裡面，使用列表的方法 index 就可解決。 如果target 不在有序列表裡面， 使用一個迴圈
找出哪個值比他大，取代它的位子即可。
"""

class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            for i in range (len(nums)):
                if nums[i] > target:
                    return i
            else:
                return len(nums)

p =Solution()
nums = [1, 3, 5, 6, 7] ; target =7
print(p.searchInsert(nums, target))

# 方法二

"""
對半切，如果 target 在左邊，右括弧就可減一，如果target在右邊，左括弧就可加一。直到左括弧大於右括弧產生矛盾。
選左括弧的index就是答案。
"""

# class Solution:
#     def searchInsert(self, nums, target):
#             left, right = 0, len(nums)-1
#             while left <= right:
#                 mid = round(left + (right - left) / 2)
#                 if target == nums[mid]:
#                     return mid
#                 elif target < nums[mid]:
#                     right = mid -1
#                 else:
#                     left = mid + 1
                    
#             return left
# p =Solution()
# nums = [1, 3, 5, 6, 7] ; target = 4
# print(p.searchInsert(nums, target))