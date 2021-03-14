"""
Given a sorted array nums, remove the duplicates in-place such that each element 
appears only once and returns the new length. Do not allocate extra space for another 
array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

# 方法一

"""
使用一個迴圈解決。第一個沒問題，count 是1。找到第二個不一樣時放在第二位，count變2
，依此類推，剩下的用列表的slicing截斷。
"""

# class Solution:
#     def removeDuplicates(self, nums):
#         if nums == []:
#             return 0

#         count = 1
#         for i in range(len(nums)):
#             if nums[i] != nums[count-1]:
#                 nums[count] = nums[i]
#                 count += 1
#         nums = nums[0:count]
#         return count  


# p = Solution()
# nums = [1,1,2,2,4]
# print(p.removeDuplicates(nums))

# 方法二

"""
兩兩由尾巴往回頭掃，兩個如果一樣就刪掉左邊的那一個，再往左前進一格，又一樣再刪掉左邊的，
再往左前進一格，依此類推。返回值就是nums的長度。重要的一點是由左往右兩兩掃會失敗喔! 要從尾巴回推。
"""

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            x = len(nums)-1
            while x:
                y = x-1
                if nums[x] == nums[y]:
                    del(nums[x])
                x -= 1
            return len(nums)

p = Solution()
nums = [1,1,2,2,4,4,5]
print(p.removeDuplicates(nums))

