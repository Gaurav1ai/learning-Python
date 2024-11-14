# Find the Index of the First Occurrence in a String

# my_str="sadbutsad"
# f="sad"
# print(my_str.find(f))


#binary search
# class Solution(object):
#     def searchInsert(self, nums, target):
        
#         left, right = 0, len(nums) - 1

        
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return mid 
#             elif nums[mid] < target:
#                 left = mid + 1  
#             else:
#                 right = mid - 1 
#         return left

s="Hello World"
s=s.strip()
print(s)
words=s.split()
print(words)