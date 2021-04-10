"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume 
that nums1 has a size equal to m + n such that it has enough space to hold additional elements 
from nums2.
"""

# 方法一

"""
這題在python有sort列表方法就很輕鬆，注意 
List1 = list2  兩個id一樣
list1[:] = list2  兩個id不一樣, list1可變在slicing
list1 = list1[0:2] list1 的 id 換了
list1[:] = list1[0:2] list1 的 id 沒變, list1可變在slicing
"""

# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         print(id(nums1))
#         nums1 = nums1[:m] + nums2        
#         nums1.sort()
#         print(id(nums1))
        

# p = Solution()
# nums1 = [1,2,3,0,0,0] ; m = 3 ;nums2 = [2,5,6] ; n = 3
# p.merge(nums1, m, nums2, n)

# 方法二

"""
正規的做法，由尾巴開始排序回來，如果 n 先等於0，什麼事都可以不用做，但如果是 m 先等於0，
要把 n 剩下的蓋上去。
"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:

            if nums1[m-1] <= nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n = n - 1
            else:
                nums1[m+n-1], nums1[m-1] = nums1[m-1], nums1[m+n-1]                
                m = m-1
        
        if m==0 and n > 0:
            nums1[:n] = nums2[:n]

        print(nums1)

p = Solution()
nums1 = [1,2,3,0,0,0] ; m = 3 ;nums2 = [2,5,6] ; n = 3
p.merge(nums1, m, nums2, n)








