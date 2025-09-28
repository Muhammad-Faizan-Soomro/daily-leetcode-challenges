# Problem: 976. Largest Perimeter Triangle
# Task:
# - Given an array of integers representing side lengths, 
#   return the largest perimeter of a valid triangle.
# - A valid triangle must satisfy the triangle inequality:
#   sum of any two sides > third side.
#
# Example:
#   nums = [2, 1, 2]
#   Sorted = [1, 2, 2]
#   Largest valid triangle = 1 + 2 + 2 = 5
#
# Approach:
# 1. Sort the array in ascending order.
# 2. Start from the largest three sides and check if they can form a triangle.
# 3. If valid (nums[i] + nums[j] > nums[k]), return their perimeter.
# 4. Otherwise, move one step left and check next triplet.
# 5. If no valid triangle exists, return 0.
#
# Time Complexity: O(n log n)  -> sorting dominates
# Space Complexity: O(1)       -> in-place sorting, constant extra space
#
# Note: Greedy works because larger numbers maximize perimeter,
#       so checking from the largest triplet down ensures correctness.

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Sort side lengths
        nums.sort()
        
        # Step 2: Initialize perimeter (default 0 if no triangle found)
        perimeter = 0
        
        # Step 3: Start checking triplets from the largest side
        k = n - 1
        j = n - 2
        i = n - 3

        while i >= 0:
            # Step 4: Check triangle inequality
            if nums[i] + nums[j] > nums[k]:
                perimeter = nums[i] + nums[j] + nums[k]
                break
            else:
                # Move to next possible triplet
                k -= 1
                j -= 1
                i -= 1

        # Step 5: Return result
        return perimeter
