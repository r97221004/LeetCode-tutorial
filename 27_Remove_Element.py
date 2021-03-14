"""
Given an array nums and a value val, remove all instances of that value in-place and 
return the new length. Do not allocate extra space for another array, you must do this 
by modifying the input array in-place with O(1) extra memory. The order of elements can
 be changed. It doesn't matter what you leave beyond the new length.
"""

# 方法一

""" 
跟上一題幾乎一模一樣，記得由尾巴往回掃就沒問題了。
"""
class Solution:
    def removeElement(self, nums, val):
        length = len(nums)
        for i in range(length):
            if nums[length-1-i] == val:
                nums.pop(length-1-i)
        return len(nums)


p = Solution()
nums = [3,2,2,3,4,5,3,1] ; val = 3
print(p.removeElement(nums, val))

# 方法二

"""
python 有內建列表的remove方法，可直接套用。
"""

# class Solution:
#     def removeElement(self, nums, val):
#         for i in range(nums.count(val)):
#             nums.remove(val)  
#         return len(nums)

# p = Solution()
# nums = [3,2,2,3,4,5,3,1] ; val = 3
# print(p.removeElement(nums, val))



