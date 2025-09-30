# Problem: 2221. Find Triangular Sum of an Array
# Task:
# - Given an array `nums`, repeatedly form a new array where each element is:
#     (nums[i] + nums[i+1]) % 10
# - Continue until only one element remains, return that element.
#
# Example:
#   nums = [1, 2, 3, 4, 5]
#   Step 1: [1+2, 2+3, 3+4, 4+5] % 10 = [3, 5, 7, 9]
#   Step 2: [3+5, 5+7, 7+9] % 10 = [8, 2, 6]
#   Step 3: [8+2, 2+6] % 10 = [0, 8]
#   Step 4: [0+8] % 10 = [8]
#   Answer = 8
#
# Approach (Simulation):
# 1. If nums has only 1 element, return it directly.
# 2. Otherwise, repeatedly build the next row using:
#       newNums[i] = (nums[i] + nums[i+1]) % 10
# 3. Replace nums with newNums and repeat until only one element is left.
#
# Time Complexity: O(n^2)   -> each level reduces size by 1, total work ~ n + (n-1) + ... + 1
# Space Complexity: O(n)    -> temporary array for each step
#

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums) 
    
        if n == 1:
            return nums[0]
            
        while len(nums) != 1:
            newNums = []
            for i in range(0, n-1):
                newNums.append((nums[i] + nums[i+1]) % 10)
            
            nums = newNums
            n -= 1
            
        return nums[0]
